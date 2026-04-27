# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmActionList.py
from .Identifiable import Identifiable

class PhmActionList(Identifiable):

    def __init__(self):
        super().__init__()
        from .PlatformHealthManagementContribution import PlatformHealthManagementContribution
        from .PhmActionItem import PhmActionItem
        self._artop_actionListExecution = None
        self._artop_platformHealthManagementContribution = None
        self._artop_actionListItemRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_platformHealthManagementContribution':"PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION", 
         '_artop_actionListItemRef':"PHM-ACTION-ITEM"})

    @property
    def actionListExecution_(self):
        return self._artop_actionListExecution

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
    def ref_actionListItems_(self):
        return self._artop_actionListItemRef

    @property
    def actionListItems_(self):
        return self._artop_actionListItemRef
