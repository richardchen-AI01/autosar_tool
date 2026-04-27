"""Context — replaces V25.10 Common/Context.pyd.

API surface (see autosar-cfg/_pyd_analysis/Context.md):
  Context class with checkData, loadArtopCache, postLoadArtopCache,
  __moduleRegist, checkVariant, moduleContext, PduInfo, setDict

Used by <Module>Register.getModuleContext(inputProject) → MemIfContext(inputProject)

D1 STATUS: walking-skeleton stub. Real behavior is "load all ARXML in input
project into ARTOP/Sphinx EMF model, hand model containers to per-module
Context subclasses". M2 will wire to actual ARTOP loader.
"""
from __future__ import annotations
from typing import Any, Dict, Optional


class Context:
    """Base class for per-module <Module>Context."""

    moduleContext: Dict[str, 'Context'] = {}

    def __init__(self, inputName: Optional[str] = None) -> None:
        self.input_name = inputName
        # subclass overrides postLoadArtopCache to set self.<Module>

    def checkData(self) -> bool:
        """D1 stub: always pass."""
        return True

    def loadArtopCache(self, project_path: str) -> None:
        """Load all ARXML in project into ARTOP EMF model.
        D1 stub: no-op (M2 will wire to ARTOP)."""
        pass

    def postLoadArtopCache(self) -> None:
        """Subclass overrides to instantiate per-module domain class.
        e.g. MemIfContext.postLoadArtopCache: self.MemIf = MemIf()"""
        pass

    def checkVariant(self) -> bool:
        """D1 stub: always pass."""
        return True

    def setDict(self, key: str, value: Any) -> None:
        """Generic key-value setter, used by some module contexts."""
        if not hasattr(self, '_dict'):
            self._dict: Dict[str, Any] = {}
        self._dict[key] = value


class PduInfo:
    """PduInfo — used by Com / PduR / IpduM contexts. D1 stub."""
    def __init__(self) -> None:
        self.tx_pdus: list = []
        self.rx_pdus: list = []
