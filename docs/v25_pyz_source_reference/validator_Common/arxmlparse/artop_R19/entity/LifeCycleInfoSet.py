# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LifeCycleInfoSet.py
from .ARElement import ARElement

class LifeCycleInfoSet(ARElement):

    def __init__(self):
        super().__init__()
        from .LifeCycleState import LifeCycleState
        from .LifeCyclePeriod import LifeCyclePeriod
        from .LifeCycleInfo import LifeCycleInfo
        from .LifeCycleStateDefinitionGroup import LifeCycleStateDefinitionGroup
        self._artop_defaultLcStateRef = None
        self._artop_defaultPeriodBegin = None
        self._artop_defaultPeriodEnd = None
        self._artop_lifeCycleInfo = []
        self._artop_usedLifeCycleStateDefinitionGroupRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_defaultLcStateRef': '"LIFE-CYCLE-STATE"', 
         '_artop_defaultPeriodBegin': '"LIFE-CYCLE-PERIOD"', 
         '_artop_defaultPeriodEnd': '"LIFE-CYCLE-PERIOD"', 
         '_artop_lifeCycleInfo': '"LIFE-CYCLE-INFO"', 
         '_artop_usedLifeCycleStateDefinitionGroupRef': '"LIFE-CYCLE-STATE-DEFINITION-GROUP"'})

    @property
    def ref_defaultLcState_(self):
        return self._artop_defaultLcStateRef

    @property
    def defaultLcState_(self):
        if self._artop_defaultLcStateRef is not None:
            if hasattr(self._artop_defaultLcStateRef, "uuid"):
                return self._artop_defaultLcStateRef.uuid
        return

    @property
    def ref_defaultPeriodBegin_(self):
        return self._artop_defaultPeriodBegin

    @property
    def defaultPeriodBegin_(self):
        if self._artop_defaultPeriodBegin is not None:
            if hasattr(self._artop_defaultPeriodBegin, "uuid"):
                return self._artop_defaultPeriodBegin.uuid
        return

    @property
    def ref_defaultPeriodEnd_(self):
        return self._artop_defaultPeriodEnd

    @property
    def defaultPeriodEnd_(self):
        if self._artop_defaultPeriodEnd is not None:
            if hasattr(self._artop_defaultPeriodEnd, "uuid"):
                return self._artop_defaultPeriodEnd.uuid
        return

    @property
    def lifeCycleInfos_LifeCycleInfo(self):
        return self._artop_lifeCycleInfo

    @property
    def ref_usedLifeCycleStateDefinitionGroup_(self):
        return self._artop_usedLifeCycleStateDefinitionGroupRef

    @property
    def usedLifeCycleStateDefinitionGroup_(self):
        if self._artop_usedLifeCycleStateDefinitionGroupRef is not None:
            if hasattr(self._artop_usedLifeCycleStateDefinitionGroupRef, "uuid"):
                return self._artop_usedLifeCycleStateDefinitionGroupRef.uuid
        return
