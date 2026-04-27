# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventOccurrenceExpressionFormula.py
from .FormulaExpression import FormulaExpression

class TDEventOccurrenceExpressionFormula(FormulaExpression):

    def __init__(self):
        super().__init__()
        from .TDEventOccurrenceExpression import TDEventOccurrenceExpression
        from .AutosarOperationArgumentInstance import AutosarOperationArgumentInstance
        from .TimingDescriptionEvent import TimingDescriptionEvent
        from .TimingModeInstance import TimingModeInstance
        from .AutosarVariableInstance import AutosarVariableInstance
        self._artop_tdEventOccurrenceExpression = None
        self._artop_argumentRef = []
        self._artop_eventRef = []
        self._artop_modeRef = []
        self._artop_variableRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_tdEventOccurrenceExpression': '"TD-EVENT-OCCURRENCE-EXPRESSION"', 
         '_artop_argumentRef': '"AUTOSAR-OPERATION-ARGUMENT-INSTANCE"', 
         '_artop_eventRef': '"TIMING-DESCRIPTION-EVENT"', 
         '_artop_modeRef': '"TIMING-MODE-INSTANCE"', 
         '_artop_variableRef': '"AUTOSAR-VARIABLE-INSTANCE"'})

    @property
    def ref_tDEventOccurrenceExpression_(self):
        return self._artop_tdEventOccurrenceExpression

    @property
    def tDEventOccurrenceExpression_(self):
        if self._artop_tdEventOccurrenceExpression is not None:
            if hasattr(self._artop_tdEventOccurrenceExpression, "uuid"):
                return self._artop_tdEventOccurrenceExpression.uuid
        return

    @property
    def ref_arguments_(self):
        return self._artop_argumentRef

    @property
    def arguments_(self):
        return self._artop_argumentRef

    @property
    def ref_events_(self):
        return self._artop_eventRef

    @property
    def events_(self):
        return self._artop_eventRef

    @property
    def ref_modes_(self):
        return self._artop_modeRef

    @property
    def modes_(self):
        return self._artop_modeRef

    @property
    def ref_variables_(self):
        return self._artop_variableRef

    @property
    def variables_(self):
        return self._artop_variableRef
