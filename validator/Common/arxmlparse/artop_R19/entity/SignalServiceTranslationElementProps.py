# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SignalServiceTranslationElementProps.py
from .Identifiable import Identifiable

class SignalServiceTranslationElementProps(Identifiable):

    def __init__(self):
        super().__init__()
        from .SignalServiceTranslationEventProps import SignalServiceTranslationEventProps
        from .DataPrototypeReference import DataPrototypeReference
        from .DataFilter import DataFilter
        self._artop_transmissionTrigger = None
        self._artop_signalServiceTranslationEventProps = None
        self._artop_element = None
        self._artop_filter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_signalServiceTranslationEventProps':"SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS", 
         '_artop_element':"DATA-PROTOTYPE-REFERENCE", 
         '_artop_filter':"DATA-FILTER"})

    @property
    def transmissionTrigger_(self):
        if self._artop_transmissionTrigger:
            if self._artop_transmissionTrigger == "true":
                return True
            return False
        else:
            return self._artop_transmissionTrigger

    @property
    def ref_signalServiceTranslationEventProps_(self):
        return self._artop_signalServiceTranslationEventProps

    @property
    def signalServiceTranslationEventProps_(self):
        if self._artop_signalServiceTranslationEventProps is not None:
            if hasattr(self._artop_signalServiceTranslationEventProps, "uuid"):
                return self._artop_signalServiceTranslationEventProps.uuid
        return

    @property
    def ref_element_(self):
        return self._artop_element

    @property
    def element_(self):
        if self._artop_element is not None:
            if hasattr(self._artop_element, "uuid"):
                return self._artop_element.uuid
        return

    @property
    def ref_filter_(self):
        return self._artop_filter

    @property
    def filter_(self):
        if self._artop_filter is not None:
            if hasattr(self._artop_filter, "uuid"):
                return self._artop_filter.uuid
        return
