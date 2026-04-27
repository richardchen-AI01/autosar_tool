# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptSupportData.py
from .ARObject import ARObject

class RptSupportData(ARObject):

    def __init__(self):
        super().__init__()
        from .McSupportData import McSupportData
        from .RptExecutionContext import RptExecutionContext
        from .RptComponent import RptComponent
        from .RptServicePoint import RptServicePoint
        self._artop_mcSupportData = None
        self._artop_executionContext = []
        self._artop_rptComponent = []
        self._artop_rptServicePoint = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_mcSupportData': '"MC-SUPPORT-DATA"', 
         '_artop_executionContext': '"RPT-EXECUTION-CONTEXT"', 
         '_artop_rptComponent': '"RPT-COMPONENT"', 
         '_artop_rptServicePoint': '"RPT-SERVICE-POINT"'})

    @property
    def ref_mcSupportData_(self):
        return self._artop_mcSupportData

    @property
    def mcSupportData_(self):
        if self._artop_mcSupportData is not None:
            if hasattr(self._artop_mcSupportData, "uuid"):
                return self._artop_mcSupportData.uuid
        return

    @property
    def executionContexts_RptExecutionContext(self):
        return self._artop_executionContext

    @property
    def rptComponents_RptComponent(self):
        return self._artop_rptComponent

    @property
    def rptServicePoints_RptServicePoint(self):
        return self._artop_rptServicePoint
