# ERS-2026-002 — Supporting Repository

Reproducibility and traceability repository for **ERS-2026-002 v1.0**,
"Measurement Chain Readiness for Instrument-Grade Energy Characterisation of
Cellular IoT Devices."

Referenced from the report's Reproducibility Statement:
`github.com/radianode/ers-2026-002`

## Repository contents

This structure maps directly to the "Repository Contents" table published in
the report.

| Report line item | Location here |
|---|---|
| Instrument configuration records | `instruments/REGISTRY.md` — populated; several fields still marked "Not established" pending physical verification |
| Measured component values | `data/measured-components.csv` — attenuators dated (BC-3, 23 Aug 2026); reference load value present but undated, see note in file |
| Raw instrument captures | `data/raw-captures/session-S02-gain-sweep/` and `data/raw-captures/current-measurement-PPK2/` |
| Session records | `data/session-records/` |
| Correction history | `docs/CORRECTIONS.md` |
| Figure generation scripts | `figures/scripts/` |

## Structure

```
.
├── README.md
├── LICENSE                          MIT — figures/scripts/ (code)
├── LICENSE-DATA                     CC BY 4.0 — data/, instruments/ (measured evidence)
├── docs/
│   └── CORRECTIONS.md              Full B.1–B.4 correction history
├── figures/
│   ├── scripts/                    One script per published figure
│   │   ├── fig01_current_validation.py
│   │   ├── fig02_rf_chain.py
│   │   ├── fig03_gain_repeatability.py
│   │   └── fig04_attribution.py
│   └── output/                     Rendered PNGs as published in the report
│       ├── FIG01_ppk2_validation.png
│       ├── FIG02_rf_chain.png
│       ├── FIG03_gain_repeatability.png
│       └── FIG04_attribution.png
└── data/
    ├── S02_gain_sweep_processed.csv    Table X from Section 03
    ├── measured-components.csv         Reference load + attenuator values, dated where possible
    ├── raw-captures/
    │   ├── session-S02-gain-sweep/     5× spectrum analyser JPEG + .spa pairs
    │   └── current-measurement-PPK2/   5× PPK2/HP6611C capture screenshots + index
    ├── session-records/
    │   └── S02_ambient_log.csv         Temperature/humidity log, session S02
    └── photos/                         Assembly and component evidence photos
        ├── rf-chain_divider-assembly_callbox-side.png
        ├── rf-chain_callbox-rear-panel_tx1-rx1.png
        ├── rf-chain_common-port_anritsu.png
        ├── BC3_attenuators-and-divider_20260823.jpg
        ├── BC3_sma-cables-connectors_20260823.jpg
        ├── BC4_sim7080g-hat_20260821.jpg
        └── BC4_ppk2-hat-attach_20260826.jpg
└── instruments/
    └── REGISTRY.md                     Per-instrument serial/firmware/calibration
```

## Licensing

Code and data in this repository are licensed separately, reflecting their
different nature:

- **`figures/scripts/`** (the figure-generation code) — [MIT License](LICENSE).
- **`data/`, `instruments/`, `docs/CORRECTIONS.md`** (measured evidence,
  instrument records, and the correction history) — [CC BY 4.0](LICENSE-DATA).

## Regenerating the figures

Each script in `figures/scripts/` is self-contained and writes its output PNG
into the working directory. Requirements:

```
pip install matplotlib pillow numpy
```

`fig02_rf_chain.py` also reads the three photos in `data/photos/` via a
relative path already set correctly in the script. `fig03_gain_repeatability.py`
additionally requires `numpy`.

### Font dependency

All four scripts render with **Liberation Sans** so figures match the
published PNGs exactly. Each script now checks a list of common install
locations (Linux system paths, macOS `/Library/Fonts/`, and a vendored
`figures/scripts/fonts/` folder you can populate yourself) and falls back to
**Arial** — Liberation Sans's metric-compatible equivalent — if none is
found, rather than silently letting matplotlib pick an arbitrary sans-serif.

To install Liberation Sans for an exact match to the published figures:

- **Debian/Ubuntu:** `sudo apt install fonts-liberation`
- **macOS (Homebrew):** `brew install --cask font-liberation`
- **Windows / any OS, no install needed:** download the two `.ttf` files
  (`LiberationSans-Regular.ttf`, `LiberationSans-Bold.ttf`) from the
  [Liberation Fonts project](https://github.com/liberationfonts/liberation-fonts)
  and place them in `figures/scripts/fonts/` — the scripts pick them up
  automatically from there.

**Reproducibility verification.** All four scripts were run from a clean
virtual environment (no Liberation Sans installed, Arial fallback engaged)
and diffed against `figures/output/`. Every figure reproduced at identical
pixel dimensions, with only 1.2–5.0% of pixels differing — concentrated in
text glyph shapes, consistent with the expected Arial/Liberation Sans
font-rendering difference rather than any discrepancy in the underlying data,
layout, or chart geometry. Run with Liberation Sans installed to reproduce
the published PNGs exactly.

## Session records — convention for future sessions

`data/session-records/S02_ambient_log.csv` covers session S02 only. As
future ERS-2026-002 addenda (or other reports reusing this repo pattern) add
sessions, each new session should get:

- its own subfolder under `data/raw-captures/`, named for that session, and
- its own ambient log under `data/session-records/`, named
  `S<NN>_ambient_log.csv` (e.g. `S03_ambient_log.csv`) — matching the
  convention already used for S02.

## Status

- **Resolved (2026-08-28):** the "Mastech DMM" naming ambiguity is confirmed
  as **Mastech MS8268**, matching the published report; HP 6611C and
  Keysight DSOX1102G serial numbers are recorded; Anritsu MS2712E firmware
  (boot/OS/application versions) is confirmed for this specific unit via a
  direct boot-screen photograph. See `instruments/REGISTRY.md` for the full
  detail and confidence caveats (the HP 6611C serial reading is flagged
  "very likely" rather than certain — see the registry entry).
- **Still open, pending a physical check by Radianode** (not inferred or
  assumed — see `instruments/REGISTRY.md`'s "What's needed to complete this
  file" section): PPK2 on-device firmware and calibration date; HP 6611C's
  precise calibration date (currently only "2025"); Anritsu serial number
  and calibration date; DMM serial number and calibration date; Keysight
  oscilloscope firmware version and calibration date.
- **Still open:** `data/measured-components.csv`'s reference load
  measurement (216–217 Ω) has no confirmed date. The attenuators are dated
  from the BC-3 photo filename (23 Aug 2026); nothing ties the reference
  load measurement to that same session, so its date is not assumed to
  match.
- **Deliberately not cited in the report:** `data/raw-captures/current-measurement-PPK2/`
  includes two repeat PPK2 source-meter captures (`ATT-02`, 18.32 mA;
  `ATT-03`, 18.31 mA) alongside the original 18.25 mA capture (`ATT-01`)
  cited in Section 01. These remain in the repo as raw evidence only — the
  source-meter setpoint consistency across all three captures was not
  confirmed, so they are not presented as clean repeats in the published
  report or in any figure here.
