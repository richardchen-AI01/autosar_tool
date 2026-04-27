# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventSwcInternalBehavior.py
from .TDEventSwc import TDEventSwc

class TDEventSwcInternalBehavior(TDEventSwc):

    def __init__(self):
        super().__init__()
        from .RunnableEntity import RunnableEntity
        from .VariableAccess import VariableAccess
        self._artop_tdEventSwcInternalBehaviorType = None
        self._artop_runnableRef = None
        self._artop_variableAccessRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_runnableRef':"RUNNABLE-ENTITY", 
         '_artop_variableAccessRef':"VARIABLE-ACCESS"})

    @property
    def tdEventSwcInternalBehaviorType_(self):
        return self._artop_tdEventSwcInternalBehaviorType

    @property
    def ref_runnable_(self):
        return self._artop_runnableRef

    @property
    def runnable_(self):
        if self._artop_runnableRef is not None:
            if hasattr(self._artop_runnableRef, "uuid"):
                return self._artop_runnableRef.uuid
        return

    @property
    def ref_variableAccess_(self):
        return self._artop_variableAccessRef

    @property
    def variableAccess_(self):
        if self._artop_variableAccessRef is not None:
            if hasattr(self._artop_variableAccessRef, "uuid"):
                return self._artop_variableAccessRef.uuid
        return
