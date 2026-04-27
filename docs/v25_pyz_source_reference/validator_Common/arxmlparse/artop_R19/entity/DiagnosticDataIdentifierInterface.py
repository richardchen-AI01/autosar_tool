# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDataIdentifierInterface.py
from .DiagnosticAbstractDataIdentifierInterface import DiagnosticAbstractDataIdentifierInterface

class DiagnosticDataIdentifierInterface(DiagnosticAbstractDataIdentifierInterface):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        self._artop_read = None
        self._artop_write = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_read':"CLIENT-SERVER-OPERATION", 
         '_artop_write':"CLIENT-SERVER-OPERATION"})

    @property
    def ref_read_(self):
        return self._artop_read

    @property
    def read_(self):
        if self._artop_read is not None:
            if hasattr(self._artop_read, "uuid"):
                return self._artop_read.uuid
        return

    @property
    def ref_write_(self):
        return self._artop_write

    @property
    def write_(self):
        if self._artop_write is not None:
            if hasattr(self._artop_write, "uuid"):
                return self._artop_write.uuid
        return
