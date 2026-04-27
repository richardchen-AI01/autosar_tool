# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AtomicSwComponentType.py
from .SwComponentType import SwComponentType

class AtomicSwComponentType(SwComponentType):

    def __init__(self):
        super().__init__()
        from .SwcInternalBehavior import SwcInternalBehavior
        from .SymbolProps import SymbolProps
        self._artop_internalBehavior = []
        self._artop_symbolProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_internalBehavior':"SWC-INTERNAL-BEHAVIOR", 
         '_artop_symbolProps':"SYMBOL-PROPS"})

    @property
    def internalBehaviors_SwcInternalBehavior(self):
        return self._artop_internalBehavior

    @property
    def ref_symbolProps_(self):
        return self._artop_symbolProps

    @property
    def symbolProps_(self):
        if self._artop_symbolProps is not None:
            if hasattr(self._artop_symbolProps, "uuid"):
                return self._artop_symbolProps.uuid
        return
