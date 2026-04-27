# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimingExtensionResource.py
from .Identifiable import Identifiable

class TimingExtensionResource(Identifiable):

    def __init__(self):
        super().__init__()
        from .TimingExtension import TimingExtension
        from .AutosarOperationArgumentInstance import AutosarOperationArgumentInstance
        from .TimingModeInstance import TimingModeInstance
        from .AutosarVariableInstance import AutosarVariableInstance
        self._artop_timingExtension = None
        self._artop_timingArgument = []
        self._artop_timingMode = []
        self._artop_timingVariable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_timingExtension': '"TIMING-EXTENSION"', 
         '_artop_timingArgument': '"AUTOSAR-OPERATION-ARGUMENT-INSTANCE"', 
         '_artop_timingMode': '"TIMING-MODE-INSTANCE"', 
         '_artop_timingVariable': '"AUTOSAR-VARIABLE-INSTANCE"'})

    @property
    def ref_timingExtension_(self):
        return self._artop_timingExtension

    @property
    def timingExtension_(self):
        if self._artop_timingExtension is not None:
            if hasattr(self._artop_timingExtension, "uuid"):
                return self._artop_timingExtension.uuid
        return

    @property
    def timingArguments_AutosarOperationArgumentInstance(self):
        return self._artop_timingArgument

    @property
    def timingModes_TimingModeInstance(self):
        return self._artop_timingMode

    @property
    def timingVariables_AutosarVariableInstance(self):
        return self._artop_timingVariable
