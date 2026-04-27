# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyFile.py
from .UploadablePackageElement import UploadablePackageElement

class PersistencyFile(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .PersistencyFileArray import PersistencyFileArray
        self._artop_contentUri = None
        self._artop_fileName = None
        self._artop_updateStrategy = None
        self._artop_persistencyFileArray = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_persistencyFileArray": "PERSISTENCY-FILE-ARRAY"})

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
    def ref_persistencyFileArray_(self):
        return self._artop_persistencyFileArray

    @property
    def persistencyFileArray_(self):
        if self._artop_persistencyFileArray is not None:
            if hasattr(self._artop_persistencyFileArray, "uuid"):
                return self._artop_persistencyFileArray.uuid
        return
