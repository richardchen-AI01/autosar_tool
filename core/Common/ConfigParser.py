"""ConfigParser — stub (D6 will fill).

V25.10 has this as Common/ConfigParser.pyd (Cython native). MemIf does not call into
this module directly — only some peripheral helpers in non-MemIf paths use it.
For D1 we provide an empty module so any framework-level wildcard imports
don't fail.

API surface from PE strings: see autosar-cfg/_pyd_analysis/ConfigParser.md
"""
