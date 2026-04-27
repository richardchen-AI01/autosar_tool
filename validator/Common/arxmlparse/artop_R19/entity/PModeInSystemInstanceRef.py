# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PModeInSystemInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class PModeInSystemInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnvSwcModeElement import DiagnosticEnvSwcModeElement
        from .System import System
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .AbstractProvidedPortPrototype import AbstractProvidedPortPrototype
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .ModeDeclaration import ModeDeclaration
        self._artop_diagnosticEnvSwcModeElement = None
        self._artop_system = None
        self._artop_contextCompositionRef = None
        self._artop_contextComponentRef = []
        self._artop_contextPPortRef = None
        self._artop_contextModeDeclarationGroupRef = None
        self._artop_targetModeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticEnvSwcModeElement': '"DIAGNOSTIC-ENV-SWC-MODE-ELEMENT"', 
         '_artop_system': '"SYSTEM"', 
         '_artop_contextCompositionRef': '"ROOT-SW-COMPOSITION-PROTOTYPE"', 
         '_artop_contextComponentRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_contextPPortRef': '"ABSTRACT-PROVIDED-PORT-PROTOTYPE"', 
         '_artop_contextModeDeclarationGroupRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_targetModeRef': '"MODE-DECLARATION"'})

    @property
    def ref_diagnosticEnvSwcModeElement_(self):
        return self._artop_diagnosticEnvSwcModeElement

    @property
    def diagnosticEnvSwcModeElement_(self):
        if self._artop_diagnosticEnvSwcModeElement is not None:
            if hasattr(self._artop_diagnosticEnvSwcModeElement, "uuid"):
                return self._artop_diagnosticEnvSwcModeElement.uuid
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
    def ref_contextComposition_(self):
        return self._artop_contextCompositionRef

    @property
    def contextComposition_(self):
        if self._artop_contextCompositionRef is not None:
            if hasattr(self._artop_contextCompositionRef, "uuid"):
                return self._artop_contextCompositionRef.uuid
        return

    @property
    def ref_contextComponents_(self):
        return self._artop_contextComponentRef

    @property
    def contextComponents_(self):
        return self._artop_contextComponentRef

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
    def ref_contextModeDeclarationGroup_(self):
        return self._artop_contextModeDeclarationGroupRef

    @property
    def contextModeDeclarationGroup_(self):
        if self._artop_contextModeDeclarationGroupRef is not None:
            if hasattr(self._artop_contextModeDeclarationGroupRef, "uuid"):
                return self._artop_contextModeDeclarationGroupRef.uuid
        return

    @property
    def ref_targetMode_(self):
        return self._artop_targetModeRef

    @property
    def targetMode_(self):
        if self._artop_targetModeRef is not None:
            if hasattr(self._artop_targetModeRef, "uuid"):
                return self._artop_targetModeRef.uuid
        return
