# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInServiceInterfaceRef.py
from .ARObject import ARObject

class DataPrototypeInServiceInterfaceRef(ARObject):

    def __init__(self):
        super().__init__()
        from .DataPrototypeInServiceInterfaceInstanceRef import DataPrototypeInServiceInterfaceInstanceRef
        from .PortInterfaceElementInImplementationDatatypeRef import PortInterfaceElementInImplementationDatatypeRef
        self._artop_dataPrototypeIref = None
        self._artop_elementInImplDatatype = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataPrototypeIref':"DATA-PROTOTYPE-IN-SERVICE-INTERFACE-INSTANCE-REF", 
         '_artop_elementInImplDatatype':"PORT-INTERFACE-ELEMENT-IN-IMPLEMENTATION-DATATYPE-REF"})

    @property
    def ref_dataPrototype_(self):
        return self._artop_dataPrototypeIref

    @property
    def dataPrototype_(self):
        if self._artop_dataPrototypeIref is not None:
            if hasattr(self._artop_dataPrototypeIref, "uuid"):
                return self._artop_dataPrototypeIref.uuid
        return

    @property
    def ref_elementInImplDatatype_(self):
        return self._artop_elementInImplDatatype

    @property
    def elementInImplDatatype_(self):
        if self._artop_elementInImplDatatype is not None:
            if hasattr(self._artop_elementInImplDatatype, "uuid"):
                return self._artop_elementInImplDatatype.uuid
        return
