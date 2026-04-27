# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SignalServiceTranslationEventProps.py
from .Identifiable import Identifiable

class SignalServiceTranslationEventProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SignalServiceTranslationProps import SignalServiceTranslationProps
        from .SignalServiceTranslationElementProps import SignalServiceTranslationElementProps
        from .AbstractSignalBasedToISignalTriggeringMapping import AbstractSignalBasedToISignalTriggeringMapping
        from .VariableDataPrototypeInSystemInstanceRef import VariableDataPrototypeInSystemInstanceRef
        self._artop_safeTranslation = None
        self._artop_secureTranslation = None
        self._artop_signalServiceTranslationProps = None
        self._artop_elementProps = []
        self._artop_serviceElementMappingRef = []
        self._artop_translationTargetIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_signalServiceTranslationProps': '"SIGNAL-SERVICE-TRANSLATION-PROPS"', 
         '_artop_elementProps': '"SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS"', 
         '_artop_serviceElementMappingRef': '"ABSTRACT-SIGNAL-BASED-TO-I-SIGNAL-TRIGGERING-MAPPING"', 
         '_artop_translationTargetIref': '"VARIABLE-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF"'})

    @property
    def safeTranslation_(self):
        if self._artop_safeTranslation:
            if self._artop_safeTranslation == "true":
                return True
            return False
        else:
            return self._artop_safeTranslation

    @property
    def secureTranslation_(self):
        if self._artop_secureTranslation:
            if self._artop_secureTranslation == "true":
                return True
            return False
        else:
            return self._artop_secureTranslation

    @property
    def ref_signalServiceTranslationProps_(self):
        return self._artop_signalServiceTranslationProps

    @property
    def signalServiceTranslationProps_(self):
        if self._artop_signalServiceTranslationProps is not None:
            if hasattr(self._artop_signalServiceTranslationProps, "uuid"):
                return self._artop_signalServiceTranslationProps.uuid
        return

    @property
    def elementProps_SignalServiceTranslationElementProps(self):
        return self._artop_elementProps

    @property
    def ref_serviceElementMappings_(self):
        return self._artop_serviceElementMappingRef

    @property
    def serviceElementMappings_(self):
        return self._artop_serviceElementMappingRef

    @property
    def ref_translationTarget_(self):
        return self._artop_translationTargetIref

    @property
    def translationTarget_(self):
        if self._artop_translationTargetIref is not None:
            if hasattr(self._artop_translationTargetIref, "uuid"):
                return self._artop_translationTargetIref.uuid
        return
