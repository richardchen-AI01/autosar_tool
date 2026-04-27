# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmLogicalExpression.py
from .Identifiable import Identifiable

class PhmLogicalExpression(Identifiable):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .HealthChannel import HealthChannel
        self._artop_logicalOperator = None
        self._artop_platformHealthManagementContribution = None
        self._artop_healthChannelArgumentRef = []
        self._artop_logicalExpressionArgumentRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_platformHealthManagementContribution':"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION", 
         '_artop_healthChannelArgumentRef':"HEALTH-CHANNEL", 
         '_artop_logicalExpressionArgumentRef':"PHM-LOGICAL-EXPRESSION"})

    @property
    def logicalOperator_(self):
        return self._artop_logicalOperator

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
    def ref_healthChannelArguments_(self):
        return self._artop_healthChannelArgumentRef

    @property
    def healthChannelArguments_(self):
        return self._artop_healthChannelArgumentRef

    @property
    def ref_logicalExpressionArguments_(self):
        return self._artop_logicalExpressionArgumentRef

    @property
    def logicalExpressionArguments_(self):
        return self._artop_logicalExpressionArgumentRef
