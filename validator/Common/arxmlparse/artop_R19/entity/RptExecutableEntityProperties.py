# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RptExecutableEntityProperties.py
from .ARObject import ARObject

class RptExecutableEntityProperties(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_maxRptEventId = None
        self._artop_minRptEventId = None
        self._artop_rptExecutionControl = None
        self._artop_rptServicePoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def maxRptEventId_(self):
        return self._artop_maxRptEventId

    @property
    def minRptEventId_(self):
        return self._artop_minRptEventId

    @property
    def rptExecutionControl_(self):
        return self._artop_rptExecutionControl

    @property
    def rptServicePoint_(self):
        return self._artop_rptServicePoint
