# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventOccurrenceExpression.py
from .ARObject import ARObject

class TDEventOccurrenceExpression(ARObject):

    def __init__(self):
        super().__init__()
        from .TimingDescriptionEvent import TimingDescriptionEvent
        from .AutosarOperationArgumentInstance import AutosarOperationArgumentInstance
        from .TDEventOccurrenceExpressionFormula import TDEventOccurrenceExpressionFormula
        from .TimingModeInstance import TimingModeInstance
        from .AutosarVariableInstance import AutosarVariableInstance
        self._artop_timingDescriptionEvent = None
        self._artop_argument = []
        self._artop_formula = None
        self._artop_mode = []
        self._artop_variable = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_timingDescriptionEvent': '"TIMING-DESCRIPTION-EVENT"', 
         '_artop_argument': '"AUTOSAR-OPERATION-ARGUMENT-INSTANCE"', 
         '_artop_formula': '"TD-EVENT-OCCURRENCE-EXPRESSION-FORMULA"', 
         '_artop_mode': '"TIMING-MODE-INSTANCE"', 
         '_artop_variable': '"AUTOSAR-VARIABLE-INSTANCE"'})

    @property
    def ref_timingDescriptionEvent_(self):
        return self._artop_timingDescriptionEvent

    @property
    def timingDescriptionEvent_(self):
        if self._artop_timingDescriptionEvent is not None:
            if hasattr(self._artop_timingDescriptionEvent, "uuid"):
                return self._artop_timingDescriptionEvent.uuid
        return

    @property
    def arguments_AutosarOperationArgumentInstance(self):
        return self._artop_argument

    @property
    def ref_formula_(self):
        return self._artop_formula

    @property
    def formula_(self):
        if self._artop_formula is not None:
            if hasattr(self._artop_formula, "uuid"):
                return self._artop_formula.uuid
        return

    @property
    def modes_TimingModeInstance(self):
        return self._artop_mode

    @property
    def variables_AutosarVariableInstance(self):
        return self._artop_variable
