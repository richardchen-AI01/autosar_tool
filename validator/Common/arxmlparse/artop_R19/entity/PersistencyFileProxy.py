# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyFileProxy.py
from .Identifiable import Identifiable

class PersistencyFileProxy(Identifiable):

    def __init__(self):
        super().__init__()
        from .PersistencyFileProxyInterface import PersistencyFileProxyInterface
        self._artop_contentUri = None
        self._artop_fileName = None
        self._artop_updateStrategy = None
        self._artop_persistencyFileProxyInterface = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_persistencyFileProxyInterface": "PERSISTENCY-FILE-PROXY-INTERFACE"})

    @property
    def contentUri_(self):
        return self._artop_contentUri

    @property
    def fileName_(self):
        return self._artop_fileName

    @property
    def updateStrategy_(self):
        return self._artop_updateStrategy

    @property
    def ref_persistencyFileProxyInterface_(self):
        return self._artop_persistencyFileProxyInterface

    @property
    def persistencyFileProxyInterface_(self):
        if self._artop_persistencyFileProxyInterface is not None:
            if hasattr(self._artop_persistencyFileProxyInterface, "uuid"):
                return self._artop_persistencyFileProxyInterface.uuid
        return
