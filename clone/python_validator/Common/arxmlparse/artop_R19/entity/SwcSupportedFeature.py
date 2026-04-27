# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcSupportedFeature.py
from .ARObject import ARObject

class SwcSupportedFeature(ARObject):

    def __init__(self):
        super().__init__()
        from .PortAPIOption import PortAPIOption
        self._artop_portApiOption = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_portApiOption": "PORT-API-OPTION"})

    @property
    def ref_portAPIOption_(self):
        return self._artop_portApiOption

    @property
    def portAPIOption_(self):
        if self._artop_portApiOption is not None:
            if hasattr(self._artop_portApiOption, "uuid"):
                return self._artop_portApiOption.uuid
        return
