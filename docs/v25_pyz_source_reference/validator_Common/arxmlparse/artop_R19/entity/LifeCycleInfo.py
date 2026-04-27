# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LifeCycleInfo.py
from .ARObject import ARObject

class LifeCycleInfo(ARObject):

    def __init__(self):
        super().__init__()
        from .LifeCycleInfoSet import LifeCycleInfoSet
        from .Referrable import Referrable
        from .LifeCycleState import LifeCycleState
        from .LifeCyclePeriod import LifeCyclePeriod
        from .DocumentationBlock import DocumentationBlock
        self._artop_lifeCycleInfoSet = None
        self._artop_lcObjectRef = None
        self._artop_lcStateRef = None
        self._artop_periodBegin = None
        self._artop_periodEnd = None
        self._artop_remark = None
        self._artop_useInsteadRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_lifeCycleInfoSet': '"LIFE-CYCLE-INFO-SET"', 
         '_artop_lcObjectRef': '"REFERRABLE"', 
         '_artop_lcStateRef': '"LIFE-CYCLE-STATE"', 
         '_artop_periodBegin': '"LIFE-CYCLE-PERIOD"', 
         '_artop_periodEnd': '"LIFE-CYCLE-PERIOD"', 
         '_artop_remark': '"DOCUMENTATION-BLOCK"', 
         '_artop_useInsteadRef': '"REFERRABLE"'})

    @property
    def ref_lifeCycleInfoSet_(self):
        return self._artop_lifeCycleInfoSet

    @property
    def lifeCycleInfoSet_(self):
        if self._artop_lifeCycleInfoSet is not None:
            if hasattr(self._artop_lifeCycleInfoSet, "uuid"):
                return self._artop_lifeCycleInfoSet.uuid
        return

    @property
    def ref_lcObject_(self):
        return self._artop_lcObjectRef

    @property
    def lcObject_(self):
        if self._artop_lcObjectRef is not None:
            if hasattr(self._artop_lcObjectRef, "uuid"):
                return self._artop_lcObjectRef.uuid
        return

    @property
    def ref_lcState_(self):
        return self._artop_lcStateRef

    @property
    def lcState_(self):
        if self._artop_lcStateRef is not None:
            if hasattr(self._artop_lcStateRef, "uuid"):
                return self._artop_lcStateRef.uuid
        return

    @property
    def ref_periodBegin_(self):
        return self._artop_periodBegin

    @property
    def periodBegin_(self):
        if self._artop_periodBegin is not None:
            if hasattr(self._artop_periodBegin, "uuid"):
                return self._artop_periodBegin.uuid
        return

    @property
    def ref_periodEnd_(self):
        return self._artop_periodEnd

    @property
    def periodEnd_(self):
        if self._artop_periodEnd is not None:
            if hasattr(self._artop_periodEnd, "uuid"):
                return self._artop_periodEnd.uuid
        return

    @property
    def ref_remark_(self):
        return self._artop_remark

    @property
    def remark_(self):
        if self._artop_remark is not None:
            if hasattr(self._artop_remark, "uuid"):
                return self._artop_remark.uuid
        return

    @property
    def ref_useInsteads_(self):
        return self._artop_useInsteadRef

    @property
    def useInsteads_(self):
        return self._artop_useInsteadRef
