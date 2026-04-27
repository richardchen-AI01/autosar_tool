# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RteEventInEcuInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class RteEventInEcuInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .McDataAccessDetails import McDataAccessDetails
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RTEEvent import RTEEvent
        self._artop_mcDataAccessDetails = None
        self._artop_system = None
        self._artop_contextRootCompositionRef = None
        self._artop_contextAtomicComponentRef = None
        self._artop_targetRteEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_mcDataAccessDetails': '"MC-DATA-ACCESS-DETAILS"', 
         '_artop_system': '"SYSTEM"', 
         '_artop_contextRootCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextAtomicComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetRteEventRef': '"RTE-EVENT"'})

    @property
    def ref_mcDataAccessDetails_(self):
        return self._artop_mcDataAccessDetails

    @property
    def mcDataAccessDetails_(self):
        if self._artop_mcDataAccessDetails is not None:
            if hasattr(self._artop_mcDataAccessDetails, "uuid"):
                return self._artop_mcDataAccessDetails.uuid
        return

    @property
    def ref_base_(self):
        return self._artop_system

    @property
    def base_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_contextRootComposition_(self):
        return self._artop_contextRootCompositionRef

    @property
    def contextRootComposition_(self):
        if self._artop_contextRootCompositionRef is not None:
            if hasattr(self._artop_contextRootCompositionRef, "uuid"):
                return self._artop_contextRootCompositionRef.uuid
        return

    @property
    def ref_contextAtomicComponent_(self):
        return self._artop_contextAtomicComponentRef

    @property
    def contextAtomicComponent_(self):
        if self._artop_contextAtomicComponentRef is not None:
            if hasattr(self._artop_contextAtomicComponentRef, "uuid"):
                return self._artop_contextAtomicComponentRef.uuid
        return

    @property
    def ref_targetRteEvent_(self):
        return self._artop_targetRteEventRef

    @property
    def targetRteEvent_(self):
        if self._artop_targetRteEventRef is not None:
            if hasattr(self._artop_targetRteEventRef, "uuid"):
                return self._artop_targetRteEventRef.uuid
        return
