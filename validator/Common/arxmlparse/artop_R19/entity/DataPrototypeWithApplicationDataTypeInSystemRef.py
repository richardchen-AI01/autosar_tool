# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeWithApplicationDataTypeInSystemRef.py
from .DataPrototypeInSystemRef import DataPrototypeInSystemRef

class DataPrototypeWithApplicationDataTypeInSystemRef(DataPrototypeInSystemRef):

    def __init__(self):
        super().__init__()
        from .ApplicationDataPrototypeInSystemInstanceRef import ApplicationDataPrototypeInSystemInstanceRef
        self._artop_dataPrototypeIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataPrototypeIref": "APPLICATION-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF-IREF"})

    @property
    def ref_dataPrototype_(self):
        return self._artop_dataPrototypeIref

    @property
    def dataPrototype_(self):
        if self._artop_dataPrototypeIref is not None:
            if hasattr(self._artop_dataPrototypeIref, "uuid"):
                return self._artop_dataPrototypeIref.uuid
        return
