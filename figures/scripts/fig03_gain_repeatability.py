import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rcParams
import numpy as np

# Liberation Sans is metric-compatible with Arial, so figures render
# identically to the published PNGs wherever it's installed. Checked
# across common Linux/macOS locations plus a vendored copy at
# figures/scripts/fonts/ (add the two .ttf files there yourself if you
# want an exact match without a system install — see README). Falls
# back to Arial, Liberation Sans's metric-compatible equivalent, rather
# than letting matplotlib silently pick an arbitrary sans-serif.
_LIBERATION_CANDIDATES = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/liberation-fonts/LiberationSans-Regular.ttf",
    "/usr/share/fonts/liberation-fonts/LiberationSans-Bold.ttf",
    "/Library/Fonts/Liberation Sans Regular.ttf",
    "/Library/Fonts/Liberation Sans Bold.ttf",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "LiberationSans-Regular.ttf"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "LiberationSans-Bold.ttf"),
]
_found_liberation = False
for _f in _LIBERATION_CANDIDATES:
    if os.path.exists(_f):
        fm.fontManager.addfont(_f)
        _found_liberation = True

if _found_liberation:
    rcParams['font.family'] = 'Liberation Sans'
else:
    print(
        "Liberation Sans not found on this system — falling back to Arial "
        "(metric-compatible). See README 'Font dependency' for how to install "
        "Liberation Sans for an exact match to the published figures."
    )
    rcParams['font.family'] = 'Arial'

NAVY = "#12263A"
NAVY2 = "#2C4A66"
COPPER = "#B56A2D"
GRID = "#AEB8C2"   # darker grid than before for more contrast

fig = plt.figure(figsize=(11.6, 3.75), dpi=260)
fig.patch.set_facecolor("white")

fig.text(0.5, 0.94, "FIGURE 3   TX Gain-Step Response and Session Repeatability",
          ha='center', fontsize=15, color=NAVY, fontweight='bold', va='top')

# LEFT PANEL
ax = fig.add_axes([0.075, 0.24, 0.38, 0.58])
gains = np.array([60, 55, 50, 45, 40])
levels = np.array([-80.512, -85.576, -90.840, -95.040, -99.776])
ax.set_facecolor("white")
ax.scatter(gains, levels, color=NAVY, s=100, zorder=4, edgecolors='white', linewidths=0.8, label="Measured (S02, 27 Aug 2026)")
slope, intercept = 0.960, -138.35
fit_x = np.array([38, 62])
fit_y = slope*fit_x + intercept
ax.plot(fit_x, fit_y, color=NAVY, lw=2.6, zorder=3, label="Linear fit: slope 0.960, R\u00b2 0.9985")
ideal_y = levels[0] - (gains[0] - fit_x)
ax.plot(fit_x, ideal_y, color=COPPER, lw=2.2, linestyle=(0,(4,2)), zorder=2, label="Ideal unity-slope response")
ax.invert_xaxis()
ax.set_xlabel("Configured TX Gain (dB)", fontsize=13.5, color=NAVY, fontweight='bold')
ax.set_ylabel("Measured Level (dBm)", fontsize=13.5, color=NAVY, fontweight='bold')
ax.tick_params(labelsize=12, colors=NAVY, width=1.2)
for spine in ax.spines.values():
    spine.set_color(NAVY)
    spine.set_linewidth(1.1)
ax.grid(color=GRID, linewidth=0.9, zorder=0)
ax.legend(fontsize=10.5, loc='upper right', frameon=True, facecolor='white', edgecolor=GRID, labelcolor=NAVY)
ax.set_title("Gain-Step Response (S02)", fontsize=14, color=NAVY, fontweight='bold', pad=8)

fig.text(0.265, 0.03, "Cumulative 60\u219240 dB: 19.26 dB measured vs 20.00 dB configured (\u22120.74 dB)",
          ha='center', fontsize=11, color=COPPER, fontweight='bold')

# RIGHT PANEL
ax2 = fig.add_axes([0.585, 0.24, 0.38, 0.42])
cats = ["60 dB", "45 dB"]
y_pos = [1, 0]
s00 = {"60 dB": -82.24, "45 dB": -95.78}
s02 = {"60 dB": -80.51, "45 dB": -95.04}
for i, cat in enumerate(cats):
    y = y_pos[i]
    ax2.plot([s00[cat], s02[cat]], [y, y], color=NAVY2, lw=4.5, zorder=1, solid_capstyle='round', alpha=0.55)
    ax2.scatter([s00[cat]], [y], color=NAVY2, s=220, zorder=3, edgecolors='white', linewidths=1.0, label="S00 (original)" if i==0 else None)
    ax2.scatter([s02[cat]], [y], color=NAVY, s=220, zorder=3, edgecolors='white', linewidths=1.0, label="S02 (27 Aug 2026)" if i==0 else None)
    diff = s02[cat]-s00[cat]
    mid = (s00[cat]+s02[cat])/2
    ax2.text(mid, y+0.30, f"{diff:+.2f} dB", ha='center', fontsize=14, color=COPPER, fontweight='bold')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(cats, fontsize=15, color=NAVY, fontweight='bold')
ax2.set_ylim(-0.6, 1.6)
ax2.invert_xaxis()
ax2.set_xlabel("Measured Level (dBm)", fontsize=13.5, color=NAVY, fontweight='bold')
ax2.tick_params(labelsize=12, colors=NAVY, width=1.2)
ax2.grid(axis='x', color=GRID, linewidth=0.9, zorder=0)
for spine in ['top', 'right', 'left']:
    ax2.spines[spine].set_visible(False)
ax2.spines['bottom'].set_color(NAVY)
ax2.spines['bottom'].set_linewidth(1.1)
ax2.legend(fontsize=11, frameon=False, labelcolor=NAVY, loc='upper center', bbox_to_anchor=(0.5, 1.24), ncol=2)
ax2.set_title("Session-to-Session Repeatability (verified endpoints only)", fontsize=12, color=NAVY, fontweight='bold', pad=34)

plt.savefig("FIG03_gain_repeatability.png", facecolor="white", dpi=260)
print("done")
