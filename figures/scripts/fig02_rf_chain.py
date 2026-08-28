import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch, Rectangle
import matplotlib.image as mpimg

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

# box is 482x142pt = 3.39:1 aspect
fig = plt.figure(figsize=(11.6, 3.42), dpi=220)
fig.patch.set_facecolor("white")

# ---- top ~62%: diagram ----
axd = fig.add_axes([0.01, 0.40, 0.98, 0.58])
axd.set_xlim(0, 10)
axd.set_ylim(0, 5)
axd.axis('off')

def box(ax, x, y, w, h, text, fc="white", ec=NAVY, tc=NAVY, fs=9.5, bold=True):
    r = Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=1.4, zorder=3)
    ax.add_patch(r)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fs,
            color=tc, fontweight='bold' if bold else 'normal', zorder=4, linespacing=1.25)

def arrow(ax, x0, y0, x1, y1, color=NAVY, lw=1.5):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=11,
                         color=color, linewidth=lw, zorder=2)
    ax.add_patch(a)

box(axd, 0.1, 3.3, 1.6, 1.1, "Amarisoft\nCallbox TX1", fs=8.6)
box(axd, 0.1, 0.6, 1.6, 1.1, "Amarisoft\nCallbox RX1", fs=8.6)
box(axd, 2.2, 3.3, 1.5, 1.1, "30 dB pad\n(30.15 dB)", fc="#FBF1DE", ec=COPPER, fs=8.0)
box(axd, 2.2, 0.6, 1.5, 1.1, "20 dB pad\n(20.28 dB)", fc="#FBF1DE", ec=COPPER, fs=8.0)
arrow(axd, 1.7, 3.85, 2.2, 3.85)
arrow(axd, 1.7, 1.15, 2.2, 1.15)
box(axd, 4.2, 1.6, 1.9, 1.8, "Wilkinson divider\n(reverse as combiner)\nimbalance 0.38 dB", fs=7.4)
arrow(axd, 3.7, 3.85, 4.2, 2.9)
arrow(axd, 3.7, 1.15, 4.2, 2.1)
box(axd, 6.6, 2.05, 1.4, 1.0, "Common\nport", fs=8.2)
arrow(axd, 6.1, 2.55, 6.6, 2.55)
box(axd, 8.4, 2.0, 1.0, 1.1, "Anritsu\nMS2712E", fc="#FBF3EE", ec=COPPER, fs=7.4)
arrow(axd, 8.0, 2.55, 8.4, 2.55, color=COPPER)

axd.text(4.7, 4.75, "Conducted RF chain \u2014 configured for characterisation (Sections 02\u201303)",
          ha='center', fontsize=10.5, color=NAVY, fontweight='bold')

# ---- bottom ~35%: three photo thumbnails ----
photo_paths = [
    "../../data/photos/rf-chain_divider-assembly_callbox-side.png",
    "../../data/photos/rf-chain_callbox-rear-panel_tx1-rx1.png",
    "../../data/photos/rf-chain_common-port_anritsu.png",
]
captions = [
    "Divider assembly, Callbox-side",
    "Callbox rear panel, TX1/RX1",
    "Common port at Anritsu",
]
for i, (p, cap) in enumerate(zip(photo_paths, captions)):
    ax = fig.add_axes([0.015 + i*0.329, 0.09, 0.30, 0.32])
    try:
        img = mpimg.imread(p)
        ax.imshow(img)
    except Exception as e:
        pass
    ax.axis('off')
    for spine in ax.spines.values():
        spine.set_visible(True)
    ax.text(0.5, -0.16, cap, transform=ax.transAxes, ha='center', va='top', fontsize=7.0, color=NAVY)

plt.savefig("FIG02_rf_chain.png", facecolor="white", dpi=220)
print("done")
