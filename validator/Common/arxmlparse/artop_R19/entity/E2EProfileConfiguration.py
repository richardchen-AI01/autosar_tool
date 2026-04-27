# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\E2EProfileConfiguration.py
from .Identifiable import Identifiable

class E2EProfileConfiguration(Identifiable):

    def __init__(self):
        super().__init__()
        from .E2EProfileConfigurationSet import E2EProfileConfigurationSet
        self._artop_clearFromValidToInvalid = None
        self._artop_dataIdMode = None
        self._artop_maxDeltaCounter = None
        self._artop_maxErrorStateInit = None
        self._artop_maxErrorStateInvalid = None
        self._artop_maxErrorStateValid = None
        self._artop_minOkStateInit = None
        self._artop_minOkStateInvalid = None
        self._artop_minOkStateValid = None
        self._artop_profileName = None
        self._artop_windowSizeInit = None
        self._artop_windowSizeInvalid = None
        self._artop_windowSizeValid = None
        self._artop_e2EProfileConfigurationSet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_e2EProfileConfigurationSet": "E-2-E-PROFILE-CONFIGURATION-SET"})

    @property
    def clearFromValidToInvalid_(self):
        if self._artop_clearFromValidToInvalid:
            if self._artop_clearFromValidToInvalid == "true":
                return True
            return False
        else:
            return self._artop_clearFromValidToInvalid

    @property
    def dataIdMode_(self):
        return self._artop_dataIdMode

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
    def minOkStateInit_(self):
        return self._artop_minOkStateInit

    @property
    def minOkStateInvalid_(self):
        return self._artop_minOkStateInvalid

    @property
    def minOkStateValid_(self):
        return self._artop_minOkStateValid

    @property
    def profileName_(self):
        return self._artop_profileName

    @property
    def windowSizeInit_(self):
        return self._artop_windowSizeInit

    @property
    def windowSizeInvalid_(self):
        return self._artop_windowSizeInvalid

    @property
    def windowSizeValid_(self):
        return self._artop_windowSizeValid

    @property
    def ref_e2EProfileConfigurationSet_(self):
        return self._artop_e2EProfileConfigurationSet

    @property
    def e2EProfileConfigurationSet_(self):
        if self._artop_e2EProfileConfigurationSet is not None:
            if hasattr(self._artop_e2EProfileConfigurationSet, "uuid"):
                return self._artop_e2EProfileConfigurationSet.uuid
        return
