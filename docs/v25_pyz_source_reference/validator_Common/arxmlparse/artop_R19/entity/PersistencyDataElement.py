# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyDataElement.py
from .AutosarDataPrototype import AutosarDataPrototype

class PersistencyDataElement(AutosarDataPrototype):

    def __init__(self):
        super().__init__()
        from .PersistencyKeyValueDatabaseInterface import PersistencyKeyValueDatabaseInterface
        self._artop_updateStrategy = None
        self._artop_persistencyKeyValueDatabaseInterface = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_persistencyKeyValueDatabaseInterface": "PERSISTENCY-KEY-VALUE-DATABASE-INTERFACE"})

    @property
    def updateStrategy_(self):
        return self._artop_updateStrategy

    @property
    def ref_persistencyKeyValueDatabaseInterface_(self):
        return self._artop_persistencyKeyValueDatabaseInterface

    @property
    def persistencyKeyValueDatabaseInterface_(self):
        if self._artop_persistencyKeyValueDatabaseInterface is not None:
            if hasattr(self._artop_persistencyKeyValueDatabaseInterface, "uuid"):
                return self._artop_persistencyKeyValueDatabaseInterface.uuid
        return
