# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationCompositeDataTypeSubElementRef.py
from .SubElementRef import SubElementRef

class ApplicationCompositeDataTypeSubElementRef(SubElementRef):

    def __init__(self):
        super().__init__()
        from .ApplicationCompositeElementInPortInterfaceInstanceRef import ApplicationCompositeElementInPortInterfaceInstanceRef
        self._artop_applicationCompositeElementIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_applicationCompositeElementIref": "APPLICATION-COMPOSITE-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF-IREF"})

    @property
    def ref_applicationCompositeElement_(self):
        return self._artop_applicationCompositeElementIref

    @property
    def applicationCompositeElement_(self):
        if self._artop_applicationCompositeElementIref is not None:
            if hasattr(self._artop_applicationCompositeElementIref, "uuid"):
                return self._artop_applicationCompositeElementIref.uuid
        return
