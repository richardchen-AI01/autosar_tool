# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ClientServerInterface.py
from .PortInterface import PortInterface

class ClientServerInterface(PortInterface):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        from .ApplicationError import ApplicationError
        self._artop_operation = []
        self._artop_possibleError = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_operation':"CLIENT-SERVER-OPERATION", 
         '_artop_possibleError':"APPLICATION-ERROR"})

    @property
    def operations_ClientServerOperation(self):
        return self._artop_operation

    @property
    def possibleErrors_ApplicationError(self):
        return self._artop_possibleError
