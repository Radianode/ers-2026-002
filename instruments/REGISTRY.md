# RNbench — Instruments Registry
**Purpose:** per-instrument model, serial, firmware, and calibration date, per RN-EVID-001 §06 (session metadata block: "PPK2 serial/firmware", "Scope serial/firmware", "Anritsu serial/firmware") and RN-PROTO-003 §3.5 ("PER-SESSION INSTRUMENT RECORD — MANDATORY: instrument model and serial; last calibration date; ...").
**This file compiles only what has actually been stated, measured, or verified. Nothing below is inferred or assumed. Fields not yet established are marked explicitly.**
---
## Nordic PPK2
| Field | Value |
|---|---|
| Serial | D439F20BA129 |
| Power Profiler software | v4.4.1 |
| Host software (nRF Connect for Desktop) | v5.3.2 |
| On-device firmware | Not established |
| Calibration type | Manufacturer/factory calibration only; no field recalibration path |
| Last calibration date | Not established |
## HP 6611C (System DC Power Supply, 0–8V/0–5A)
| Field | Value |
|---|---|
| Model | HP 6611C |
| Lab asset tag | TQP 12921 |
| Manufacturer serial number | US37450671 (read from rear compliance label) |
| Last calibration date | 5 December 2025 |
| Calibrated by | Keysight Technologies |
## Anritsu MS2712E Spectrum Master
| Field | Value |
|---|---|
| Model | MS2712E/9/27/31/42/43/44/62/63/65/66/67/90/411/541/542/546 |
| Serial number | Not established |
| Firmware / boot version | Boot Build V3.28, OS Build V4.61, Application Package V4.50 |
| Last calibration date | Not established |
## Bench DMM
| Field | Value |
|---|---|
| Model | Mastech MS8268 |
| Serial number | Not established |
| Firmware | Not applicable |
| Last calibration date | Not established |
## Oscilloscope (Keysight DSOX1102G)
| Field | Value |
|---|---|
| Model | Keysight DSOX1102G |
| Serial number | CN57136218 |
| Firmware | Not established |
| Last calibration date | Not established |
---
## What's needed to complete this file
For each **Not established** field above, someone at Radianode needs to physically:
1. Check the instrument's serial plate/label (usually rear or bottom panel) — distinct from any lab asset tag.
2. Check the instrument's own firmware/version display, typically under an "About," "System," or "Info" menu.
3. Check for a calibration sticker or pull the instrument's calibration certificate/record if Radianode maintains one.

Once supplied, update this file in place (not re-created) so it remains the single current reference, per RN-PROTO-003 §3.5.
---
*Filed under RNbench. No value in this file has been inferred, estimated, or assumed from indirect sources.*
