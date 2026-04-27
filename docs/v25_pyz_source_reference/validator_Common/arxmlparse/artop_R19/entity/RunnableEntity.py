# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RunnableEntity.py
from .ExecutableEntity import ExecutableEntity
from .AtpStructureElement import AtpStructureElement

class RunnableEntity(AtpStructureElement, ExecutableEntity):

    def __init__(self):
        super().__init__()
        from .SwcInternalBehavior import SwcInternalBehavior
        from .RunnableEntityArgument import RunnableEntityArgument
        from .AsynchronousServerCallResultPoint import AsynchronousServerCallResultPoint
        from .VariableAccess import VariableAccess
        from .ExternalTriggeringPoint import ExternalTriggeringPoint
        from .InternalTriggeringPoint import InternalTriggeringPoint
        from .ModeAccessPoint import ModeAccessPoint
        from .ModeSwitchPoint import ModeSwitchPoint
        from .ParameterAccess import ParameterAccess
        from .ServerCallPoint import ServerCallPoint
        from .WaitPoint import WaitPoint
        from .VariationPoint import VariationPoint
        self._artop_canBeInvokedConcurrently = None
        self._artop_symbol = None
        self._artop_swcInternalBehavior = None
        self._artop_argument = []
        self._artop_asynchronousServerCallResultPoint = []
        self._artop_dataReadAccess = []
        self._artop_dataReceivePointByArgument = []
        self._artop_dataReceivePointByValue = []
        self._artop_dataSendPoint = []
        self._artop_dataWriteAccess = []
        self._artop_externalTriggeringPoint = []
        self._artop_internalTriggeringPoint = []
        self._artop_modeAccessPoint = []
        self._artop_modeSwitchPoint = []
        self._artop_parameterAccess = []
        self._artop_readLocalVariable = []
        self._artop_serverCallPoint = []
        self._artop_waitPoint = []
        self._artop_writtenLocalVariable = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swcInternalBehavior': '"SWC-INTERNAL-BEHAVIOR"', 
         '_artop_argument': '"RUNNABLE-ENTITY-ARGUMENT"', 
         '_artop_asynchronousServerCallResultPoint': '"ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"', 
         '_artop_dataReadAccess': '"VARIABLE-ACCESS"', 
         '_artop_dataReceivePointByArgument': '"VARIABLE-ACCESS"', 
         '_artop_dataReceivePointByValue': '"VARIABLE-ACCESS"', 
         '_artop_dataSendPoint': '"VARIABLE-ACCESS"', 
         '_artop_dataWriteAccess': '"VARIABLE-ACCESS"', 
         '_artop_externalTriggeringPoint': '"EXTERNAL-TRIGGERING-POINT"', 
         '_artop_internalTriggeringPoint': '"INTERNAL-TRIGGERING-POINT"', 
         '_artop_modeAccessPoint': '"MODE-ACCESS-POINT"', 
         '_artop_modeSwitchPoint': '"MODE-SWITCH-POINT"', 
         '_artop_parameterAccess': '"PARAMETER-ACCESS"', 
         '_artop_readLocalVariable': '"VARIABLE-ACCESS"', 
         '_artop_serverCallPoint': '"SERVER-CALL-POINT"', 
         '_artop_waitPoint': '"WAIT-POINT"', 
         '_artop_writtenLocalVariable': '"VARIABLE-ACCESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def canBeInvokedConcurrently_(self):
        if self._artop_canBeInvokedConcurrently:
            if self._artop_canBeInvokedConcurrently == "true":
                return True
            return False
        else:
            return self._artop_canBeInvokedConcurrently

    @property
    def symbol_(self):
        return self._artop_symbol

    @property
    def ref_swcInternalBehavior_(self):
        return self._artop_swcInternalBehavior

    @property
    def swcInternalBehavior_(self):
        if self._artop_swcInternalBehavior is not None:
            if hasattr(self._artop_swcInternalBehavior, "uuid"):
                return self._artop_swcInternalBehavior.uuid
        return

    @property
    def arguments_RunnableEntityArgument(self):
        return self._artop_argument

    @property
    def asynchronousServerCallResultPoints_AsynchronousServerCallResultPoint(self):
        return self._artop_asynchronousServerCallResultPoint

    @property
    def dataReadAccess_VariableAccess(self):
        return self._artop_dataReadAccess

    @property
    def dataReceivePointByArguments_VariableAccess(self):
        return self._artop_dataReceivePointByArgument

    @property
    def dataReceivePointByValues_VariableAccess(self):
        return self._artop_dataReceivePointByValue

    @property
    def dataSendPoints_VariableAccess(self):
        return self._artop_dataSendPoint

    @property
    def dataWriteAccess_VariableAccess(self):
        return self._artop_dataWriteAccess

    @property
    def externalTriggeringPoints_ExternalTriggeringPoint(self):
        return self._artop_externalTriggeringPoint

    @property
    def internalTriggeringPoints_InternalTriggeringPoint(self):
        return self._artop_internalTriggeringPoint

    @property
    def modeAccessPoints_ModeAccessPoint(self):
        return self._artop_modeAccessPoint

    @property
    def modeSwitchPoints_ModeSwitchPoint(self):
        return self._artop_modeSwitchPoint

    @property
    def parameterAccess_ParameterAccess(self):
        return self._artop_parameterAccess

    @property
    def readLocalVariables_VariableAccess(self):
        return self._artop_readLocalVariable

    @property
    def serverCallPoints_ServerCallPoint(self):
        return self._artop_serverCallPoint

    @property
    def waitPoints_WaitPoint(self):
        return self._artop_waitPoint

    @property
    def writtenLocalVariables_VariableAccess(self):
        return self._artop_writtenLocalVariable

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
