# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939ControllerApplication.py
from .ARElement import ARElement

class J1939ControllerApplication(ARElement):

    def __init__(self):
        super().__init__()
        from .ComponentInSystemInstanceRef import ComponentInSystemInstanceRef
        self._artop_functionId = None
        self._artop_swComponentPrototypeIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swComponentPrototypeIref": "COMPONENT-IN-SYSTEM-INSTANCE-REF-IREF"})

    @property
    def functionId_(self):
        return self._artop_functionId

    @property
    def ref_swComponentPrototype_(self):
        return self._artop_swComponentPrototypeIref

    @property
    def swComponentPrototype_(self):
        if self._artop_swComponentPrototypeIref is not None:
            if hasattr(self._artop_swComponentPrototypeIref, "uuid"):
                return self._artop_swComponentPrototypeIref.uuid
        return
