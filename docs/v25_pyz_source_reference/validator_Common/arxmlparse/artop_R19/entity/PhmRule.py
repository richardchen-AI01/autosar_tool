# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmRule.py
from .Identifiable import Identifiable

class PhmRule(Identifiable):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .PhmLogicalExpression import PhmLogicalExpression
        from .PhmActionList import PhmActionList
        self._artop_ruleInitState = None
        self._artop_platformHealthManagementContribution = None
        self._artop_expressionRef = None
        self._artop_falseActionListRef = None
        self._artop_trueActionListRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_platformHealthManagementContribution': '"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION"', 
         '_artop_expressionRef': '"PHM-LOGICAL-EXPRESSION"', 
         '_artop_falseActionListRef': '"PHM-ACTION-LIST"', 
         '_artop_trueActionListRef': '"PHM-ACTION-LIST"'})

    @property
    def ruleInitState_(self):
        return self._artop_ruleInitState

    @property
    def ref_platformHealthManagementContribution_(self):
        return self._artop_platformHealthManagementContribution

    @property
    def platformHealthManagementContribution_(self):
        if self._artop_platformHealthManagementContribution is not None:
            if hasattr(self._artop_platformHealthManagementContribution, "uuid"):
                return self._artop_platformHealthManagementContribution.uuid
        return

    @property
    def ref_expression_(self):
        return self._artop_expressionRef

    @property
    def expression_(self):
        if self._artop_expressionRef is not None:
            if hasattr(self._artop_expressionRef, "uuid"):
                return self._artop_expressionRef.uuid
        return

    @property
    def ref_falseActionList_(self):
        return self._artop_falseActionListRef

    @property
    def falseActionList_(self):
        if self._artop_falseActionListRef is not None:
            if hasattr(self._artop_falseActionListRef, "uuid"):
                return self._artop_falseActionListRef.uuid
        return

    @property
    def ref_trueActionList_(self):
        return self._artop_trueActionListRef

    @property
    def trueActionList_(self):
        if self._artop_trueActionListRef is not None:
            if hasattr(self._artop_trueActionListRef, "uuid"):
                return self._artop_trueActionListRef.uuid
        return
