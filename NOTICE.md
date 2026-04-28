# NOTICE — Autosar_tool

## Status: research / internal demo only

This repository (versions **v0.1** and **v0.2**) is a **research and internal
demonstration project**. It is **not** released under an open-source license,
**not** suitable for redistribution, and **not** approved for commercial use.

The reasons are spelled out below so that anyone forking, cloning, or copying
this code understands the constraints.

---

## 1. Derived from third-party source

Substantial portions of this codebase are **derived from ORIENTAIS Configurator
V25.10** (vendor: iSoft / EasyXMen). Specifically:

| Path | Origin |
|---|---|
| `generator/modules/<Module>/` | Reverse-engineered + decompiled from V25.10's `bswgen.exe` PYZ archive |
| `validator/Bsw/<Module>/` | Reverse-engineered + decompiled from V25.10's `bswval.exe` PYZ archive |
| `samples/Demo_S32K148/` | Copied verbatim from V25.10's bundled demo workspace |
| `schemas/common/*Def.arxml` | Copied verbatim from V25.10's installed schema set |
| `core/Common/arxmlparse/constant/BswPathConstant.py` | All 6870 enum members extracted via `xdis` from V25.10's `BswPathConstant.pyc` |

These artifacts retain whatever rights the original publisher holds. We have no
license to redistribute them and **no clean-room separation** has yet been
performed. This is fine for internal exploration on hardware that is already a
licensed V25.10 user; it is **not** fine for any external distribution, public
demo, paid use, or fork outside that licensed context.

## 2. ARTOP / Sphinx jars (Tier 1 — IDE)

The Eclipse RCP IDE half (under `ide/frameworks/`, currently unpopulated)
depends on:

- **ARTOP 4.5.2** — AUTOSAR Tool Platform metamodel jars
- **Eclipse Sphinx 0.11.2** — EMF workspace lifecycle jars
- **Eclipse RCP runtime** — ~200 jars from the Eclipse p2 repository

ARTOP jars are licensed only to **AUTOSAR member organizations**. Local use is
permitted because the developer is on a licensed workstation; **redistribution
of these jars (e.g. by including them in a public release artifact) is
prohibited**. See [https://www.artop.org](https://www.artop.org) for terms.

Eclipse RCP / Sphinx jars are EPL-2.0 and may be redistributed, but only with
their license headers preserved.

## 3. Patent / contractual considerations

The original ORIENTAIS Configurator may be subject to commercial license terms
between the vendor and end customers. This research project assumes the
developer is operating within their own licensed seat. **Anyone receiving a
copy of this repository must independently verify that they hold an equivalent
license to the upstream V25.10 product** before using, modifying, or
distributing this code.

## 4. Intent of the v0.3 clean-room rewrite

The published roadmap (see `docs/PLAN.md` §9) lists **v0.3** as a clean-room
rewrite milestone. v0.3 is intended to:

1. Remove all V25.10-derived module sources (`generator/modules/<Module>/`,
   `validator/Bsw/<Module>/`).
2. Replace them with implementations written from public AUTOSAR R23-11 ECUC
   schemas only, with no reference to the vendor's `.pyd` or `.pyc` artifacts.
3. Replace V25.10's bundled demo workspace with one we author from scratch.

**Until v0.3 lands and that clean-room scope is verified by an independent
review, this repository is for personal / internal use only.**

## 5. What you may safely treat as our own work

These parts of the repo are written from scratch for this project and carry no
upstream encumbrance:

- All files under `core/Common/` (the pure-Python replacement for V25.10's
  Cython `Common/*.pyd` modules), except the bundled `BswPathConstant.py`
  enum table.
- All files under `tools/`.
- All files under `docs/` (architecture, plan, sprint logs).
- The `ide/README.md` skeleton plan (no Java code yet).
- The `.github/workflows/` CI configuration.
- The `samples/Demo_S32K148_BAD_2170/` and `samples/Demo_S32K148_BAD_2171/`
  test fixtures (the BAD- variants — not the original Demo_S32K148).

These will form the basis of the v0.3 clean-room build.

---

## Trademarks

- **AUTOSAR** is a registered trademark of the AUTOSAR development partnership.
- **ORIENTAIS**, **EasyXMen** are trademarks of their respective owners.
- **Eclipse**, **ARTOP**, **Sphinx** are trademarks of the Eclipse Foundation.

Use of these names in this repository is descriptive only and does not imply
endorsement.

---

## Contact

For questions about the licensing posture of any specific file, open an issue
on the GitHub repository.

---

_Last reviewed: 2026-04-28 (D2)_
