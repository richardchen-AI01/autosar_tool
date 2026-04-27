# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortShaper.py
from .CouplingPortStructuralElement import CouplingPortStructuralElement

class CouplingPortShaper(CouplingPortStructuralElement):

    def __init__(self):
        super().__init__()
        from .CouplingPortFifo import CouplingPortFifo
        self._artop_idleSlope = None
        self._artop_predecessorFifoRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_predecessorFifoRef": "COUPLING-PORT-FIFO"})

    @property
    def idleSlope_(self):
        return self._artop_idleSlope

    @property
    def ref_predecessorFifo_(self):
        return self._artop_predecessorFifoRef

    @property
    def predecessorFifo_(self):
        if self._artop_predecessorFifoRef is not None:
            if hasattr(self._artop_predecessorFifoRef, "uuid"):
                return self._artop_predecessorFifoRef.uuid
        return
