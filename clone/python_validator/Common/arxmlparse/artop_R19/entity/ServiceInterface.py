# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceInterface.py
from .PortInterface import PortInterface

class ServiceInterface(PortInterface):

    def __init__(self):
        super().__init__()
        from .VariableDataPrototype import VariableDataPrototype
        from .Field import Field
        from .ClientServerOperation import ClientServerOperation
        self._artop_majorVersion = None
        self._artop_minorVersion = None
        self._artop_event = []
        self._artop_field = []
        self._artop_method = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_event':"VARIABLE-DATA-PROTOTYPE", 
         '_artop_field':"FIELD", 
         '_artop_method':"CLIENT-SERVER-OPERATION"})

    @property
    def majorVersion_(self):
        return self._artop_majorVersion

    @property
    def minorVersion_(self):
        return self._artop_minorVersion

    @property
    def events_VariableDataPrototype(self):
        return self._artop_event

    @property
    def fields_Field(self):
        return self._artop_field

    @property
    def methods_ClientServerOperation(self):
        return self._artop_method
