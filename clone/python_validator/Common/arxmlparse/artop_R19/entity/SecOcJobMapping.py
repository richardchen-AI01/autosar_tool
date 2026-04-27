# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SecOcJobMapping.py
from .Identifiable import Identifiable

class SecOcJobMapping(Identifiable):

    def __init__(self):
        super().__init__()
        from .SecOcDeployment import SecOcDeployment
        from .SecOcJobRequirement import SecOcJobRequirement
        self._artop_secOcDeployment = None
        self._artop_secOcJobRequirementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_secOcDeployment':"SEC-OC-DEPLOYMENT", 
         '_artop_secOcJobRequirementRef':"SEC-OC-JOB-REQUIREMENT"})

    @property
    def ref_secOcDeployment_(self):
        return self._artop_secOcDeployment

    @property
    def secOcDeployment_(self):
        if self._artop_secOcDeployment is not None:
            if hasattr(self._artop_secOcDeployment, "uuid"):
                return self._artop_secOcDeployment.uuid
        return

    @property
    def ref_secOcJobRequirement_(self):
        return self._artop_secOcJobRequirementRef

    @property
    def secOcJobRequirement_(self):
        if self._artop_secOcJobRequirementRef is not None:
            if hasattr(self._artop_secOcJobRequirementRef, "uuid"):
                return self._artop_secOcJobRequirementRef.uuid
        return
