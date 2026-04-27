# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndTransformationComSpecProps.py
from .TransformationComSpecProps import TransformationComSpecProps

class EndToEndTransformationComSpecProps(TransformationComSpecProps):

    def __init__(self):
        super().__init__()
        self._artop_clearFromValidToInvalid = None
        self._artop_disableEndToEndCheck = None
        self._artop_maxDeltaCounter = None
        self._artop_maxErrorStateInit = None
        self._artop_maxErrorStateInvalid = None
        self._artop_maxErrorStateValid = None
        self._artop_maxNoNewOrRepeatedData = None
        self._artop_minOkStateInit = None
        self._artop_minOkStateInvalid = None
        self._artop_minOkStateValid = None
        self._artop_syncCounterInit = None
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
    def disableEndToEndCheck_(self):
        if self._artop_disableEndToEndCheck:
            if self._artop_disableEndToEndCheck == "true":
                return True
            return False
        else:
            return self._artop_disableEndToEndCheck

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
    def syncCounterInit_(self):
        return self._artop_syncCounterInit

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
