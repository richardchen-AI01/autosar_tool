# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyFileProxyInterface.py
from .PersistencyInterface import PersistencyInterface

class PersistencyFileProxyInterface(PersistencyInterface):

    def __init__(self):
        super().__init__()
        from .PersistencyFileProxy import PersistencyFileProxy
        self._artop_encoding = None
        self._artop_maxNumberOfFiles = None
        self._artop_fileProxy = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_fileProxy": "PERSISTENCY-FILE-PROXY"})

    @property
    def encoding_(self):
        return self._artop_encoding

    @property
    def maxNumberOfFiles_(self):
        return self._artop_maxNumberOfFiles

    @property
    def fileProxies_PersistencyFileProxy(self):
        return self._artop_fileProxy
