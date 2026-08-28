# RNbench — Instruments Registry
**Compiled:** 2026-08-26, from S01 session records.
**Updated:** 2026-08-28, from direct photographic evidence (serial/compliance labels, an Anritsu boot screen) and direct confirmation (HP 6611C calibration date, PPK2 calibration type) supplied by Radianode.
**Purpose:** per-instrument model, serial, firmware, and calibration date, per RN-EVID-001 §06 (session metadata block: "PPK2 serial/firmware", "Scope serial/firmware", "Anritsu serial/firmware") and RN-PROTO-003 §3.5 ("PER-SESSION INSTRUMENT RECORD — MANDATORY: instrument model and serial; last calibration date; ...").
**This file compiles only what has actually been stated, measured, or photographically verified in this engagement. Nothing below is inferred or assumed beyond what is explicitly flagged as such. Fields not yet established are marked explicitly — these require someone at Radianode to physically check the instrument (serial plate, calibration sticker, About/firmware screen) and report back; they are not derivable from anything supplied so far.**
---
## Nordic PPK2
| Field | Value |
|---|---|
| Serial | D439F20BA129 |
| Power Profiler software | v4.4.1 |
| Host software (nRF Connect for Desktop) | v5.3.2 |
| On-device firmware | **Not established.** Not displayed in the About screen at time of checking. Explicitly not inferred (per session record). |
| Calibration type | **Confirmed by Radianode, 2026-08-28:** this unit uses manufacturer/factory calibration only, with no field recalibration path. |
| Last calibration date | **Not established.** Factory-calibrated units typically carry no field-accessible calibration date or certificate distinct from the manufacture date — none has been supplied for this specific unit. |
## HP 6611C (System DC Power Supply, 0–8V/0–5A)
| Field | Value |
|---|---|
| Model | HP 6611C |
| Lab asset tag | TQP 12921 |
| Additional property tag (rear label) | LE-010-22132 — a second, different lab asset/property tag found on the same rear label as the compliance marking below. Not a manufacturer serial. |
| Manufacturer serial number | **US37450671** — read from the rear compliance label as `HP6611C#US37450671`. Flagged as **very likely** rather than certain: the `Model#Serial` format after the `#` matches HP/Agilent/Keysight's standard compliance-label convention, but the label does not explicitly say "Serial No." the way the Keysight scope's label does. |
| Last calibration date | **5 December 2025**, supplied by Radianode 2026-08-28 (completes the previously-recorded year, "2025"). |
| Calibrated by | Keysight Technologies |
## Anritsu MS2712E Spectrum Master
| Field | Value |
|---|---|
| Model | MS2712E/9/27/31/42/43/44/62/63/65/66/67/90/411/541/542/546, read from the unit's own boot screen |
| Serial number | **Not established.** Not shown on the boot screen; used extensively throughout BC-3 characterization, but only the bare model name/options string has appeared in any record so far. |
| Firmware / boot version | **Confirmed for this specific unit** via a live boot-screen photograph, 2026-08-28: Boot Build V3.28, OS Build V4.61, Application Package V4.50. (An earlier, unrelated document had referenced this exact "boot V3.28, OS V4.61, application V4.50" figure for "an Anritsu instrument" during the original band survey, explicitly caveated at the time as unconfirmed for this specific unit. The 2026-08-28 boot-screen photo resolves that: this is now a direct, unit-specific reading, not an assumption carried over from the earlier document.) |
| Last calibration date | **Not established.** |
## Bench DMM
| Field | Value |
|---|---|
| Model | **Mastech MS8268** — confirmed via a front-panel photograph, 2026-08-28. Resolves the earlier naming mismatch: the published report's Investigation Scope table names this instrument "Mastech MS8268," while this registry previously carried only the generic "Mastech DMM" per the equipment inventory it was compiled from. Photographic confirmation ties the two to the same unit. |
| Serial number | **Not established.** Not visible from the front panel; would require checking the battery compartment or rear of the unit. |
| Firmware | Not applicable / not established. |
| Last calibration date | **Not established.** |
## Oscilloscope (Keysight DSOX1102G)
| Field | Value |
|---|---|
| Model | Keysight DSOX1102G |
| Serial number | **CN57136218** — read from the rear compliance/serial label, 2026-08-28. |
| Firmware | **Not established.** The rear label is the compliance/serial label, not the scope's own Help → About screen — firmware version is still not visible from what's been photographed. |
| Last calibration date | **Not established.** |
---
## What's needed to complete this file
For each **Not established** field above, someone at Radianode needs to physically:
1. Check the instrument's serial plate/label (usually rear or bottom panel) — distinct from any lab asset tag. (Remaining: Anritsu serial; DMM serial, from the battery compartment or rear.)
2. Check the instrument's own firmware/version display, typically under an "About," "System," or "Info" menu. (Remaining: PPK2 on-device firmware; Keysight scope firmware, via Help → About rather than the rear label.)
3. Check for a calibration sticker (often shows last-cal and next-due dates) or pull the instrument's calibration certificate/record if Radianode maintains one. (Remaining: Anritsu; DMM; Keysight scope. The PPK2 is factory-calibrated only with no field-accessible date, and HP 6611C's precise date is now recorded as 5 December 2025.)

Once supplied, this file should be updated in place (not re-created) so it remains the single current reference, per RN-PROTO-003 §3.5's per-session instrument record requirement.
---
*Filed under RNbench. Reflects information stated across S01 session records as of 2026-08-26, updated 2026-08-28 with direct photographic evidence and direct confirmation supplied by Radianode. No value in this file has been inferred, estimated, or assumed from indirect sources beyond what is explicitly flagged as such (the HP 6611C manufacturer serial reading).*
