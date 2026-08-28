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
NAVY2 = "#2C4A66"
COPPER = "#B56A2D"
GRID = "#D4D9DE"

# box is 482x124pt = 3.89:1 aspect. Build to match, wide and short.
fig, ax = plt.subplots(figsize=(11.6, 2.98), dpi=220)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

groups = ["Source meter\nmeasured", "Source meter\ncalculated",
          "Ampere meter\nmeasured", "Ampere meter\ntheoretical", "Supply\nindicated"]
vals = [18.25, 18.15, 18.14, 18.18, 18.27]
colors = [NAVY, NAVY2, NAVY, NAVY2, "#7A8B99"]

x = range(len(groups))
bars = ax.bar(x, vals, color=colors, width=0.6, zorder=3)

ax.set_ylim(17.9, 18.4)
ax.set_ylabel("Current (mA)", fontsize=15, color=NAVY)
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=14, color=NAVY)
ax.tick_params(axis='y', labelsize=13, colors=NAVY)
ax.grid(axis='y', color=GRID, linewidth=0.9, zorder=0)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
for spine in ['left', 'bottom']:
    ax.spines[spine].set_color(GRID)

for i, v in enumerate(vals):
    ax.text(i, v + 0.014, f"{v:.2f}", ha='center', fontsize=14, color=NAVY, fontweight='bold')

ax.annotate("", xy=(2, 18.145), xytext=(3, 18.175),
            arrowprops=dict(arrowstyle='-', color=COPPER, lw=1.6, linestyle=(0,(3,2))))
ax.text(2.5, 18.36, "0.22% deviation (ampere meter mode)", ha='center', fontsize=13,
        color=COPPER, fontweight='bold')

plt.tight_layout()
plt.savefig("FIG01_ppk2_validation.png", facecolor="white", bbox_inches='tight', pad_inches=0.08)
print("done")
