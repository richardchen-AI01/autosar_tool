# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DeterministicClientResourceNeeds.py
from .Identifiable import Identifiable

class DeterministicClientResourceNeeds(Identifiable):

    def __init__(self):
        super().__init__()
        from .ProcessDesign import ProcessDesign
        from .DeterministicClientResource import DeterministicClientResource
        self._artop_hardwarePlatform = None
        self._artop_processDesign = None
        self._artop_initResource = None
        self._artop_runResource = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_processDesign':"PROCESS-DESIGN", 
         '_artop_initResource':"DETERMINISTIC-CLIENT-RESOURCE", 
         '_artop_runResource':"DETERMINISTIC-CLIENT-RESOURCE"})

    @property
    def hardwarePlatform_(self):
        return self._artop_hardwarePlatform

    @property
    def ref_processDesign_(self):
        return self._artop_processDesign

    @property
    def processDesign_(self):
        if self._artop_processDesign is not None:
            if hasattr(self._artop_processDesign, "uuid"):
                return self._artop_processDesign.uuid
        return

    @property
    def ref_initResource_(self):
        return self._artop_initResource

    @property
    def initResource_(self):
        if self._artop_initResource is not None:
            if hasattr(self._artop_initResource, "uuid"):
                return self._artop_initResource.uuid
        return

    @property
    def ref_runResource_(self):
        return self._artop_runResource

    @property
    def runResource_(self):
        if self._artop_runResource is not None:
            if hasattr(self._artop_runResource, "uuid"):
                return self._artop_runResource.uuid
        return
