# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyKeyValueDatabase.py
from .PersistencyDeployment import PersistencyDeployment

class PersistencyKeyValueDatabase(PersistencyDeployment):

    def __init__(self):
        super().__init__()
        from .PersistencyKeyValuePair import PersistencyKeyValuePair
        self._artop_uri = None
        self._artop_keyValuePair = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_keyValuePair": "PERSISTENCY-KEY-VALUE-PAIR"})

    @property
    def uri_(self):
        return self._artop_uri

    @property
    def keyValuePairs_PersistencyKeyValuePair(self):
        return self._artop_keyValuePair
