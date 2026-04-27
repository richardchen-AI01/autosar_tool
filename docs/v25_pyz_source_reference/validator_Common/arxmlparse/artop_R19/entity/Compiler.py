# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Compiler.py
from .Identifiable import Identifiable

class Compiler(Identifiable):

    def __init__(self):
        super().__init__()
        from .Implementation import Implementation
        self._artop_name = None
        self._artop_options = None
        self._artop_vendor = None
        self._artop_version = None
        self._artop_implementation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_implementation": "IMPLEMENTATION"})

    @property
    def name_(self):
        return self._artop_name

    @property
    def options_(self):
        return self._artop_options

    @property
    def vendor_(self):
        return self._artop_vendor

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_implementation_(self):
        return self._artop_implementation

    @property
    def implementation_(self):
        if self._artop_implementation is not None:
            if hasattr(self._artop_implementation, "uuid"):
                return self._artop_implementation.uuid
        return
