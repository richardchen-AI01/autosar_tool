# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyFileArray.py
from .PersistencyDeployment import PersistencyDeployment

class PersistencyFileArray(PersistencyDeployment):

    def __init__(self):
        super().__init__()
        from .PersistencyFile import PersistencyFile
        self._artop_uri = None
        self._artop_file = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_file": "PERSISTENCY-FILE"})

    @property
    def uri_(self):
        return self._artop_uri

    @property
    def files_PersistencyFile(self):
        return self._artop_file
