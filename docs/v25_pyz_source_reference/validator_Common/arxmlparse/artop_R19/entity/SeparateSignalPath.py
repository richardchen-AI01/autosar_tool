# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SeparateSignalPath.py
from .SignalPathConstraint import SignalPathConstraint

class SeparateSignalPath(SignalPathConstraint):

    def __init__(self):
        super().__init__()
        from .SwcToSwcOperationArguments import SwcToSwcOperationArguments
        from .SwcToSwcSignal import SwcToSwcSignal
        self._artop_operation = []
        self._artop_signal = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_operation':"SWC-TO-SWC-OPERATION-ARGUMENTS", 
         '_artop_signal':"SWC-TO-SWC-SIGNAL"})

    @property
    def operations_SwcToSwcOperationArguments(self):
        return self._artop_operation

    @property
    def signals_SwcToSwcSignal(self):
        return self._artop_signal
