# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingPortScheduler.py
from .CouplingPortStructuralElement import CouplingPortStructuralElement

class CouplingPortScheduler(CouplingPortStructuralElement):

    def __init__(self):
        super().__init__()
        from .CouplingPortStructuralElement import CouplingPortStructuralElement
        self._artop_portScheduler = None
        self._artop_predecessorRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_predecessorRef": "COUPLING-PORT-STRUCTURAL-ELEMENT"})

    @property
    def portScheduler_(self):
        return self._artop_portScheduler

    @property
    def ref_predecessors_(self):
        return self._artop_predecessorRef

    @property
    def predecessors_(self):
        return self._artop_predecessorRef
