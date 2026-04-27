# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Process.py
from .AbstractExecutionContext import AbstractExecutionContext

class Process(AbstractExecutionContext):

    def __init__(self):
        super().__init__()
        from .ProcessDesign import ProcessDesign
        from .DeterministicClient import DeterministicClient
        from .Executable import Executable
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .StateDependentStartupConfig import StateDependentStartupConfig
        self._artop_logTraceDefaultLogLevel = None
        self._artop_logTraceFilePath = None
        self._artop_logTraceLogMode = None
        self._artop_logTraceProcessDesc = None
        self._artop_logTraceProcessId = None
        self._artop_numberOfRestartAttempts = None
        self._artop_preMapping = None
        self._artop_designRef = None
        self._artop_deterministicClientRef = None
        self._artop_executableRef = None
        self._artop_processStateMachine = None
        self._artop_stateDependentStartupConfig = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_designRef': '"PROCESS-DESIGN"', 
         '_artop_deterministicClientRef': '"DETERMINISTIC-CLIENT"', 
         '_artop_executableRef': '"EXECUTABLE"', 
         '_artop_processStateMachine': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_stateDependentStartupConfig': '"STATE-DEPENDENT-STARTUP-CONFIG"'})

    @property
    def logTraceDefaultLogLevel_(self):
        return self._artop_logTraceDefaultLogLevel

    @property
    def logTraceFilePath_(self):
        return self._artop_logTraceFilePath

    @property
    def logTraceLogMode_(self):
        return self._artop_logTraceLogMode

    @property
    def logTraceProcessDesc_(self):
        return self._artop_logTraceProcessDesc

    @property
    def logTraceProcessId_(self):
        return self._artop_logTraceProcessId

    @property
    def numberOfRestartAttempts_(self):
        return self._artop_numberOfRestartAttempts

    @property
    def preMapping_(self):
        if self._artop_preMapping:
            if self._artop_preMapping == "true":
                return True
            return False
        else:
            return self._artop_preMapping

    @property
    def ref_design_(self):
        return self._artop_designRef

    @property
    def design_(self):
        if self._artop_designRef is not None:
            if hasattr(self._artop_designRef, "uuid"):
                return self._artop_designRef.uuid
        return

    @property
    def ref_deterministicClient_(self):
        return self._artop_deterministicClientRef

    @property
    def deterministicClient_(self):
        if self._artop_deterministicClientRef is not None:
            if hasattr(self._artop_deterministicClientRef, "uuid"):
                return self._artop_deterministicClientRef.uuid
        return

    @property
    def ref_executable_(self):
        return self._artop_executableRef

    @property
    def executable_(self):
        if self._artop_executableRef is not None:
            if hasattr(self._artop_executableRef, "uuid"):
                return self._artop_executableRef.uuid
        return

    @property
    def ref_processStateMachine_(self):
        return self._artop_processStateMachine

    @property
    def processStateMachine_(self):
        if self._artop_processStateMachine is not None:
            if hasattr(self._artop_processStateMachine, "uuid"):
                return self._artop_processStateMachine.uuid
        return

    @property
    def stateDependentStartupConfigs_StateDependentStartupConfig(self):
        return self._artop_stateDependentStartupConfig
