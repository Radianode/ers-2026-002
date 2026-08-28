# Correction History — ERS-2026-002

Referenced from the Reproducibility Statement of ERS-2026-002 v1.0.
Publishing this history is deliberate: it is the clearest available demonstration
that the report's findings survived challenge, rather than being presented as
correct on first attempt.

---

## B.1 — Extrapolated full-band RF sweep

An earlier draft interpretation extended the observed RF-chain behaviour beyond
the frequencies directly measured during characterisation, later identified as
an unsupported extrapolation.

**Correction:** quantitative RF claims are restricted to frequencies and port
configurations directly measured. Full-band characterisation remains deferred
and is not claimed anywhere in the published report.

---

## B.2 — Assembled-chain verification

An earlier draft treated the assembled RF chain as verified based principally
on physical configuration and component-level measurements, which do not by
themselves establish delivered power at the DUT connector.

**Correction:** component-level and assembled-chain measurements are now
distinguished. The five-point gain sweep (session S02) is retained as evidence
of RF-level response under the assembled configuration; no unsupported
DUT-port insertion-loss value is inferred from component measurements alone.

---

## B.3 — Board-level current versus module current

An earlier interpretation associated measured board-level current with the
module's power-saving behaviour.

**Correction:** the 2.06 mA figure is identified as a board-level measurement
that includes carrier/HAT circuitry, and is not presented as intrinsic module
current. The 3.2 µA figure remains a vendor-published module PSM reference.
The two are not directly comparable as like-for-like currents; the ~644×
ratio is presented as an attribution boundary, not a measured module value.
