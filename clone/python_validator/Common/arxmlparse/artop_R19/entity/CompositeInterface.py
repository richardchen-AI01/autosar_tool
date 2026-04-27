# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompositeInterface.py
from .PortInterface import PortInterface

class CompositeInterface(PortInterface):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_command = []
        self._artop_indication = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_command':"CLIENT-SERVER-OPERATION", 
         '_artop_indication':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def commands_ClientServerOperation(self):
        return self._artop_command

    @property
    def indications_VariableDataPrototype(self):
        return self._artop_indication
