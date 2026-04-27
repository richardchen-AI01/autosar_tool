# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInPortInterfaceInstanceRef.py
from .AtpInstanceRef import AtpInstanceRef

class DataPrototypeInPortInterfaceInstanceRef(AtpInstanceRef):

    def __init__(self):
        super().__init__()
        from .DataPrototypeInPortInterfaceRef import DataPrototypeInPortInterfaceRef
        self._artop_dataPrototypeInPortInterfaceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataPrototypeInPortInterfaceRef": "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF"})

    @property
    def ref_dataPrototypeInPortInterfaceRef_(self):
        return self._artop_dataPrototypeInPortInterfaceRef

    @property
    def dataPrototypeInPortInterfaceRef_(self):
        if self._artop_dataPrototypeInPortInterfaceRef is not None:
            if hasattr(self._artop_dataPrototypeInPortInterfaceRef, "uuid"):
                return self._artop_dataPrototypeInPortInterfaceRef.uuid
        return
