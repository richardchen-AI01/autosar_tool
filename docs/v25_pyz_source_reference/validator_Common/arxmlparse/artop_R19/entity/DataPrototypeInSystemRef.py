# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeInSystemRef.py
from .ARObject import ARObject

class DataPrototypeInSystemRef(ARObject):

    def __init__(self):
        super().__init__()
        from .DataPrototypeTransformationProps import DataPrototypeTransformationProps
        self._artop_tagId = None
        self._artop_dataPrototypeTransformationProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataPrototypeTransformationProps": "DATA-PROTOTYPE-TRANSFORMATION-PROPS"})

    @property
    def tagId_(self):
        return self._artop_tagId

    @property
    def ref_dataPrototypeTransformationProps_(self):
        return self._artop_dataPrototypeTransformationProps

    @property
    def dataPrototypeTransformationProps_(self):
        if self._artop_dataPrototypeTransformationProps is not None:
            if hasattr(self._artop_dataPrototypeTransformationProps, "uuid"):
                return self._artop_dataPrototypeTransformationProps.uuid
        return
