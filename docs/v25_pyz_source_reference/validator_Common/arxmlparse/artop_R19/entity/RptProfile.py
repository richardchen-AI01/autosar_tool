# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptProfile.py
from .Identifiable import Identifiable

class RptProfile(Identifiable):

    def __init__(self):
        super().__init__()
        from .RapidPrototypingScenario import RapidPrototypingScenario
        self._artop_maxServicePointId = None
        self._artop_minServicePointId = None
        self._artop_servicePointSymbolPost = None
        self._artop_servicePointSymbolPre = None
        self._artop_stimEnabler = None
        self._artop_rapidPrototypingScenario = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_rapidPrototypingScenario": "RAPID-PROTOTYPING-SCENARIO"})

    @property
    def maxServicePointId_(self):
        return self._artop_maxServicePointId

    @property
    def minServicePointId_(self):
        return self._artop_minServicePointId

    @property
    def servicePointSymbolPost_(self):
        return self._artop_servicePointSymbolPost

    @property
    def servicePointSymbolPre_(self):
        return self._artop_servicePointSymbolPre

    @property
    def stimEnabler_(self):
        return self._artop_stimEnabler

    @property
    def ref_rapidPrototypingScenario_(self):
        return self._artop_rapidPrototypingScenario

    @property
    def rapidPrototypingScenario_(self):
        if self._artop_rapidPrototypingScenario is not None:
            if hasattr(self._artop_rapidPrototypingScenario, "uuid"):
                return self._artop_rapidPrototypingScenario.uuid
        return
