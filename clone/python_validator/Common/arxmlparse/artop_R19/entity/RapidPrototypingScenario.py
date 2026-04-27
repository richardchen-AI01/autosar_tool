# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RapidPrototypingScenario.py
from .ARElement import ARElement

class RapidPrototypingScenario(ARElement):

    def __init__(self):
        super().__init__()
        from .System import System
        from .RptContainer import RptContainer
        from .RptProfile import RptProfile
        self._artop_hostSystemRef = None
        self._artop_rptContainer = []
        self._artop_rptProfile = []
        self._artop_rptSystemRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_hostSystemRef': '"SYSTEM"', 
         '_artop_rptContainer': '"RPT-CONTAINER"', 
         '_artop_rptProfile': '"RPT-PROFILE"', 
         '_artop_rptSystemRef': '"SYSTEM"'})

    @property
    def ref_hostSystem_(self):
        return self._artop_hostSystemRef

    @property
    def hostSystem_(self):
        if self._artop_hostSystemRef is not None:
            if hasattr(self._artop_hostSystemRef, "uuid"):
                return self._artop_hostSystemRef.uuid
        return

    @property
    def rptContainers_RptContainer(self):
        return self._artop_rptContainer

    @property
    def rptProfiles_RptProfile(self):
        return self._artop_rptProfile

    @property
    def ref_rptSystem_(self):
        return self._artop_rptSystemRef

    @property
    def rptSystem_(self):
        if self._artop_rptSystemRef is not None:
            if hasattr(self._artop_rptSystemRef, "uuid"):
                return self._artop_rptSystemRef.uuid
        return
