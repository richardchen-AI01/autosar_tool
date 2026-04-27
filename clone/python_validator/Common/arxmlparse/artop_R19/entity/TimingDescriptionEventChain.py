# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimingDescriptionEventChain.py
from .TimingDescription import TimingDescription

class TimingDescriptionEventChain(TimingDescription):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEvent import TimingDescriptionEvent
        self._artop_stimulusRef = None
        self._artop_responseRef = None
        self._artop_segmentRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_stimulusRef':"TIMING-DESCRIPTION-EVENT", 
         '_artop_responseRef':"TIMING-DESCRIPTION-EVENT", 
         '_artop_segmentRef':"TIMING-DESCRIPTION-EVENT-CHAIN"})

    @property
    def ref_stimulus_(self):
        return self._artop_stimulusRef

    @property
    def stimulus_(self):
        if self._artop_stimulusRef is not None:
            if hasattr(self._artop_stimulusRef, "uuid"):
                return self._artop_stimulusRef.uuid
        return

    @property
    def ref_response_(self):
        return self._artop_responseRef

    @property
    def response_(self):
        if self._artop_responseRef is not None:
            if hasattr(self._artop_responseRef, "uuid"):
                return self._artop_responseRef.uuid
        return

    @property
    def ref_segments_(self):
        return self._artop_segmentRef

    @property
    def segments_(self):
        return self._artop_segmentRef
