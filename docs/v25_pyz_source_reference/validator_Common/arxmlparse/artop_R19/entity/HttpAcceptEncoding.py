# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HttpAcceptEncoding.py
from .ARObject import ARObject

class HttpAcceptEncoding(ARObject):

    def __init__(self):
        super().__init__()
        from .RestHttpPortPrototypeMapping import RestHttpPortPrototypeMapping
        self._artop_acceptEncoding = None
        self._artop_restHttpPortPrototypeMapping = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_restHttpPortPrototypeMapping": "REST-HTTP-PORT-PROTOTYPE-MAPPING"})

    @property
    def acceptEncoding_(self):
        return self._artop_acceptEncoding

    @property
    def ref_restHttpPortPrototypeMapping_(self):
        return self._artop_restHttpPortPrototypeMapping

    @property
    def restHttpPortPrototypeMapping_(self):
        if self._artop_restHttpPortPrototypeMapping is not None:
            if hasattr(self._artop_restHttpPortPrototypeMapping, "uuid"):
                return self._artop_restHttpPortPrototypeMapping.uuid
        return
