# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SignalServiceTranslationProps.py
from .Identifiable import Identifiable

class SignalServiceTranslationProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SignalServiceTranslationPropsSet import SignalServiceTranslationPropsSet
        from .ConsumedEventGroup import ConsumedEventGroup
        from .PncMappingIdent import PncMappingIdent
        from .EventHandler import EventHandler
        from .SignalServiceTranslationEventProps import SignalServiceTranslationEventProps
        self._artop_serviceControl = None
        self._artop_signalServiceTranslationPropsSet = None
        self._artop_controlConsumedEventGroupRef = []
        self._artop_controlPncRef = []
        self._artop_controlProvidedEventGroupRef = []
        self._artop_signalServiceTranslationEventProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_signalServiceTranslationPropsSet': '"SIGNAL-SERVICE-TRANSLATION-PROPS-SET"', 
         '_artop_controlConsumedEventGroupRef': '"CONSUMED-EVENT-GROUP"', 
         '_artop_controlPncRef': '"PNC-MAPPING-IDENT"', 
         '_artop_controlProvidedEventGroupRef': '"EVENT-HANDLER"', 
         '_artop_signalServiceTranslationEventProps': '"SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS"'})

    @property
    def serviceControl_(self):
        return self._artop_serviceControl

    @property
    def ref_signalServiceTranslationPropsSet_(self):
        return self._artop_signalServiceTranslationPropsSet

    @property
    def signalServiceTranslationPropsSet_(self):
        if self._artop_signalServiceTranslationPropsSet is not None:
            if hasattr(self._artop_signalServiceTranslationPropsSet, "uuid"):
                return self._artop_signalServiceTranslationPropsSet.uuid
        return

    @property
    def ref_controlConsumedEventGroups_(self):
        return self._artop_controlConsumedEventGroupRef

    @property
    def controlConsumedEventGroups_(self):
        return self._artop_controlConsumedEventGroupRef

    @property
    def ref_controlPncs_(self):
        return self._artop_controlPncRef

    @property
    def controlPncs_(self):
        return self._artop_controlPncRef

    @property
    def ref_controlProvidedEventGroups_(self):
        return self._artop_controlProvidedEventGroupRef

    @property
    def controlProvidedEventGroups_(self):
        return self._artop_controlProvidedEventGroupRef

    @property
    def signalServiceTranslationEventProps_SignalServiceTranslationEventProps(self):
        return self._artop_signalServiceTranslationEventProps
