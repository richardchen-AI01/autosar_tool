# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComFindServiceGrantDesign.py
from .GrantDesign import GrantDesign

class ComFindServiceGrantDesign(GrantDesign):

    def __init__(self):
        super().__init__()
        from .RPortPrototypeInExecutableInstanceRef import RPortPrototypeInExecutableInstanceRef
        self._artop_requiredServicePortIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_requiredServicePortIref": "R-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF"})

    @property
    def ref_requiredServicePort_(self):
        return self._artop_requiredServicePortIref

    @property
    def requiredServicePort_(self):
        if self._artop_requiredServicePortIref is not None:
            if hasattr(self._artop_requiredServicePortIref, "uuid"):
                return self._artop_requiredServicePortIref.uuid
        return
