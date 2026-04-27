# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PRPortPrototype.py
from .AbstractRequiredPortPrototype import AbstractRequiredPortPrototype
from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype

class PRPortPrototype(AbstractProvidedPortPrototype, AbstractRequiredPortPrototype):

    def __init__(self):
        super().__init__()
        from .PortInterface import PortInterface
        self._artop_providedRequiredInterfaceTref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_providedRequiredInterfaceTref": "PORT-INTERFACE"})

    @property
    def ref_providedRequiredInterface_(self):
        return self._artop_providedRequiredInterfaceTref

    @property
    def providedRequiredInterface_(self):
        if self._artop_providedRequiredInterfaceTref is not None:
            if hasattr(self._artop_providedRequiredInterfaceTref, "uuid"):
                return self._artop_providedRequiredInterfaceTref.uuid
        return
