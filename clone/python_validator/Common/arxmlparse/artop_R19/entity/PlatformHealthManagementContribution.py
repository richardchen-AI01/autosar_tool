# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PlatformHealthManagementContribution.py
from .UploadablePackageElement import UploadablePackageElement

class PlatformHealthManagementContribution(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .SupervisionCheckpoint import SupervisionCheckpoint
        from .LocalSupervision import LocalSupervision
        from .GlobalSupervision import GlobalSupervision
        from .HealthChannel import HealthChannel
        from .PhmLogicalExpression import PhmLogicalExpression
        from .PhmRule import PhmRule
        from .PhmActionList import PhmActionList
        from .PhmActionItem import PhmActionItem
        self._artop_checkpoint = []
        self._artop_localSupervision = []
        self._artop_globalSupervision = []
        self._artop_healthChannel = []
        self._artop_logicalExpression = []
        self._artop_rule = []
        self._artop_actionList = []
        self._artop_action = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_checkpoint': '"SUPERVISION-CHECKPOINT"', 
         '_artop_localSupervision': '"LOCAL-SUPERVISION"', 
         '_artop_globalSupervision': '"GLOBAL-SUPERVISION"', 
         '_artop_healthChannel': '"HEALTH-CHANNEL"', 
         '_artop_logicalExpression': '"PHM-LOGICAL-EXPRESSION"', 
         '_artop_rule': '"PHM-RULE"', 
         '_artop_actionList': '"PHM-ACTION-LIST"', 
         '_artop_action': '"PHM-ACTION-ITEM"'})

    @property
    def checkpoints_SupervisionCheckpoint(self):
        return self._artop_checkpoint

    @property
    def localSupervisions_LocalSupervision(self):
        return self._artop_localSupervision

    @property
    def globalSupervisions_GlobalSupervision(self):
        return self._artop_globalSupervision

    @property
    def healthChannels_HealthChannel(self):
        return self._artop_healthChannel

    @property
    def logicalExpressions_PhmLogicalExpression(self):
        return self._artop_logicalExpression

    @property
    def rules_PhmRule(self):
        return self._artop_rule

    @property
    def actionLists_PhmActionList(self):
        return self._artop_actionList

    @property
    def actions_PhmActionItem(self):
        return self._artop_action
