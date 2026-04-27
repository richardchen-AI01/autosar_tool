# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PPortPrototype.py
from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype

class PPortPrototype(AbstractProvidedPortPrototype):

    def __init__(self):
        super().__init__()
        from .PortInterface import PortInterface
        self._artop_providedInterfaceTref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_providedInterfaceTref": "PORT-INTERFACE"})

    @property
    def ref_providedInterface_(self):
        return self._artop_providedInterfaceTref

    @property
    def providedInterface_(self):
        if self._artop_providedInterfaceTref is not None:
            if hasattr(self._artop_providedInterfaceTref, "uuid"):
                return self._artop_providedInterfaceTref.uuid
        return
