# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildActionManifest.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint
from .ARElement import ARElement

class BuildActionManifest(ARElement, AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .BuildAction import BuildAction
        from .BuildActionEnvironment import BuildActionEnvironment
        self._artop_startActionRef = []
        self._artop_tearDownActionRef = []
        self._artop_buildAction = []
        self._artop_buildActionEnvironment = []
        self._artop_dynamicActionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_startActionRef': '"BUILD-ACTION"', 
         '_artop_tearDownActionRef': '"BUILD-ACTION"', 
         '_artop_buildAction': '"BUILD-ACTION"', 
         '_artop_buildActionEnvironment': '"BUILD-ACTION-ENVIRONMENT"', 
         '_artop_dynamicActionRef': '"BUILD-ACTION"'})

    @property
    def ref_startActions_(self):
        return self._artop_startActionRef

    @property
    def startActions_(self):
        return self._artop_startActionRef

    @property
    def ref_tearDownActions_(self):
        return self._artop_tearDownActionRef

    @property
    def tearDownActions_(self):
        return self._artop_tearDownActionRef

    @property
    def buildActions_BuildAction(self):
        return self._artop_buildAction

    @property
    def buildActionEnvironments_BuildActionEnvironment(self):
        return self._artop_buildActionEnvironment

    @property
    def ref_dynamicActions_(self):
        return self._artop_dynamicActionRef

    @property
    def dynamicActions_(self):
        return self._artop_dynamicActionRef
