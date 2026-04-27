# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationError.py
from .Identifiable import Identifiable

class ApplicationError(Identifiable):

    def __init__(self):
        super().__init__()
        from .ClientServerInterface import ClientServerInterface
        self._artop_errorCode = None
        self._artop_clientServerInterface = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_clientServerInterface": "CLIENT-SERVER-INTERFACE"})

    @property
    def errorCode_(self):
        if self._artop_errorCode:
            return int(self._artop_errorCode)
        return self._artop_errorCode

    @property
    def ref_clientServerInterface_(self):
        return self._artop_clientServerInterface

    @property
    def clientServerInterface_(self):
        if self._artop_clientServerInterface is not None:
            if hasattr(self._artop_clientServerInterface, "uuid"):
                return self._artop_clientServerInterface.uuid
        return
