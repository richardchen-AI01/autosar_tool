# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndTransformationDescription.py
from .TransformationDescription import TransformationDescription

class EndToEndTransformationDescription(TransformationDescription):

    def __init__(self):
        super().__init__()
        self._artop_clearFromValidToInvalid = None
        self._artop_counterOffset = None
        self._artop_crcOffset = None
        self._artop_dataIdMode = None
        self._artop_dataIdNibbleOffset = None
        self._artop_maxDeltaCounter = None
        self._artop_maxErrorStateInit = None
        self._artop_maxErrorStateInvalid = None
        self._artop_maxErrorStateValid = None
        self._artop_maxNoNewOrRepeatedData = None
        self._artop_minOkStateInit = None
        self._artop_minOkStateInvalid = None
        self._artop_minOkStateValid = None
        self._artop_offset = None
        self._artop_profileBehavior = None
        self._artop_profileName = None
        self._artop_syncCounterInit = None
        self._artop_upperHeaderBitsToShift = None
        self._artop_windowSize = None
        self._artop_windowSizeInit = None
        self._artop_windowSizeInvalid = None
        self._artop_windowSizeValid = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def clearFromValidToInvalid_(self):
        if self._artop_clearFromValidToInvalid:
            if self._artop_clearFromValidToInvalid == "true":
                return True
            return False
        else:
            return self._artop_clearFromValidToInvalid

    @property
    def counterOffset_(self):
        return self._artop_counterOffset

    @property
    def crcOffset_(self):
        return self._artop_crcOffset

    @property
    def dataIdMode_(self):
        return self._artop_dataIdMode

    @property
    def dataIdNibbleOffset_(self):
        return self._artop_dataIdNibbleOffset

    @property
    def maxDeltaCounter_(self):
        return self._artop_maxDeltaCounter

    @property
    def maxErrorStateInit_(self):
        return self._artop_maxErrorStateInit

    @property
    def maxErrorStateInvalid_(self):
        return self._artop_maxErrorStateInvalid

    @property
    def maxErrorStateValid_(self):
        return self._artop_maxErrorStateValid

    @property
    def maxNoNewOrRepeatedData_(self):
        return self._artop_maxNoNewOrRepeatedData

    @property
    def minOkStateInit_(self):
        return self._artop_minOkStateInit

    @property
    def minOkStateInvalid_(self):
        return self._artop_minOkStateInvalid

    @property
    def minOkStateValid_(self):
        return self._artop_minOkStateValid

    @property
    def offset_(self):
        return self._artop_offset

    @property
    def profileBehavior_(self):
        return self._artop_profileBehavior

    @property
    def profileName_(self):
        return self._artop_profileName

    @property
    def syncCounterInit_(self):
        return self._artop_syncCounterInit

    @property
    def upperHeaderBitsToShift_(self):
        return self._artop_upperHeaderBitsToShift

    @property
    def windowSize_(self):
        return self._artop_windowSize

    @property
    def windowSizeInit_(self):
        return self._artop_windowSizeInit

    @property
    def windowSizeInvalid_(self):
        return self._artop_windowSizeInvalid

    @property
    def windowSizeValid_(self):
        return self._artop_windowSizeValid
