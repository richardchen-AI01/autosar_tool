# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ComFieldGrantDesign.py
from .GrantDesign import GrantDesign

class ComFieldGrantDesign(GrantDesign):

    def __init__(self):
        super().__init__()
        from .FieldInExecutableInstanceRef import FieldInExecutableInstanceRef
        self._artop_role = None
        self._artop_fieldIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_fieldIref": "FIELD-IN-EXECUTABLE-INSTANCE-REF"})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_field_(self):
        return self._artop_fieldIref

    @property
    def field_(self):
        if self._artop_fieldIref is not None:
            if hasattr(self._artop_fieldIref, "uuid"):
                return self._artop_fieldIref.uuid
        return
