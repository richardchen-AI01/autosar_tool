# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PModeGroupInAtomicSwcInstanceRef.py
from .ModeGroupInAtomicSwcInstanceRef import ModeGroupInAtomicSwcInstanceRef

class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):

    def __init__(self):
        super().__init__()
        from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .AtomicSwComponentType import AtomicSwComponentType
        self._artop_contextPPortRef = None
        self._artop_targetModeGroupRef = None
        self._artop_atomicSwComponentType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_contextPPortRef':"ABSTRACT-PROVIDED-PORT-PROTOTYPE", 
         '_artop_targetModeGroupRef':"MODE-DECLARATION-GROUP-PROTOTYPE", 
         '_artop_atomicSwComponentType':"ATOMIC-SW-COMPONENT-TYPE"})

    @property
    def ref_contextPPort_(self):
        return self._artop_contextPPortRef

    @property
    def contextPPort_(self):
        if self._artop_contextPPortRef is not None:
            if hasattr(self._artop_contextPPortRef, "uuid"):
                return self._artop_contextPPortRef.uuid
        return

    @property
    def ref_targetModeGroup_(self):
        return self._artop_targetModeGroupRef

    @property
    def targetModeGroup_(self):
        if self._artop_targetModeGroupRef is not None:
            if hasattr(self._artop_targetModeGroupRef, "uuid"):
                return self._artop_targetModeGroupRef.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_atomicSwComponentType

    @property
    def base_(self):
        if self._artop_atomicSwComponentType is not None:
            if hasattr(self._artop_atomicSwComponentType, "uuid"):
                return self._artop_atomicSwComponentType.uuid
        return
