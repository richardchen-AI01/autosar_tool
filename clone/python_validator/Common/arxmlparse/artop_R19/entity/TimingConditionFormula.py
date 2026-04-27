# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimingConditionFormula.py
from .FormulaExpression import FormulaExpression

class TimingConditionFormula(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .TimingCondition import TimingCondition
        from .AutosarOperationArgumentInstance import AutosarOperationArgumentInstance
        from .TimingDescriptionEvent import TimingDescriptionEvent
        from .TimingModeInstance import TimingModeInstance
        from .AutosarVariableInstance import AutosarVariableInstance
        self._artop_timingCondition = None
        self._artop_timingArgumentRef = []
        self._artop_timingConditionRef = []
        self._artop_timingEventRef = []
        self._artop_timingModeRef = []
        self._artop_timingVariableRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_timingCondition': '"TIMING-CONDITION"', 
         '_artop_timingArgumentRef': '"AUTOSAR-OPERATION-ARGUMENT-INSTANCE"', 
         '_artop_timingConditionRef': '"TIMING-CONDITION"', 
         '_artop_timingEventRef': '"TIMING-DESCRIPTION-EVENT"', 
         '_artop_timingModeRef': '"TIMING-MODE-INSTANCE"', 
         '_artop_timingVariableRef': '"AUTOSAR-VARIABLE-INSTANCE"'})

    @property
    def ref_timingCondition_(self):
        return self._artop_timingCondition

    @property
    def timingCondition_(self):
        if self._artop_timingCondition is not None:
            if hasattr(self._artop_timingCondition, "uuid"):
                return self._artop_timingCondition.uuid
        return

    @property
    def ref_timingArguments_(self):
        return self._artop_timingArgumentRef

    @property
    def timingArguments_(self):
        return self._artop_timingArgumentRef

    @property
    def ref_timingConditions_(self):
        return self._artop_timingConditionRef

    @property
    def timingConditions_(self):
        return self._artop_timingConditionRef

    @property
    def ref_timingEvents_(self):
        return self._artop_timingEventRef

    @property
    def timingEvents_(self):
        return self._artop_timingEventRef

    @property
    def ref_timingModes_(self):
        return self._artop_timingModeRef

    @property
    def timingModes_(self):
        return self._artop_timingModeRef

    @property
    def ref_timingVariables_(self):
        return self._artop_timingVariableRef

    @property
    def timingVariables_(self):
        return self._artop_timingVariableRef
