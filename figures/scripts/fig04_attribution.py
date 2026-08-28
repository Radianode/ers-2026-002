import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rcParams

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
COPPER = "#B56A2D"
GRID = "#D4D9DE"

# box 482x125pt = 3.86:1
fig, ax = plt.subplots(figsize=(11.6, 3.0), dpi=220)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

labels = ["Module datasheet\nPSM floor", "Board-level measured\nbaseline"]
vals = [3.2, 2.06e3]
colors = ["#7A8B99", NAVY]

y = [0, 1]
ax.barh(y, vals, color=colors, height=0.55, zorder=3)
ax.set_xscale('log')
ax.set_xlim(1, 1e4)
ax.set_xlabel("Current (\u00b5A, log scale)", fontsize=15, color=NAVY)
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=15, color=NAVY)
ax.tick_params(labelsize=13, colors=NAVY)
ax.grid(axis='x', which='both', color=GRID, linewidth=0.7, zorder=0)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_color(GRID)

ax.text(vals[0]*1.5, 0, "3.2 \u00b5A", va='center', fontsize=15, color=NAVY, fontweight='bold')
ax.text(vals[1]*1.15, 1, "2.06 mA", va='center', fontsize=15, color=NAVY, fontweight='bold')

ax.annotate("", xy=(vals[1], 0.5), xytext=(vals[0], 0.5),
            arrowprops=dict(arrowstyle='<->', color=COPPER, lw=1.8))
ax.text(60, 0.62, "~644\u00d7 attribution boundary", fontsize=14, color=COPPER, fontweight='bold', ha='center')

plt.tight_layout()
plt.savefig("FIG04_attribution.png", facecolor="white", bbox_inches='tight', pad_inches=0.08)
print("done")
