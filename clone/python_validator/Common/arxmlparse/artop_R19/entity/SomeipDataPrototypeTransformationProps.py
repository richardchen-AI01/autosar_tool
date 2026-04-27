# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipDataPrototypeTransformationProps.py
from .ARElement import ARElement

class SomeipDataPrototypeTransformationProps(ARElement):

    def __init__(self):
        super().__init__()
        from .DataPrototypeInServiceInterfaceRef import DataPrototypeInServiceInterfaceRef
        from .SwDataDefProps import SwDataDefProps
        from .ApSomeipTransformationProps import ApSomeipTransformationProps
        self._artop_dataPrototype = []
        self._artop_networkRepresentation = None
        self._artop_someipTransformationPropsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataPrototype':"DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF", 
         '_artop_networkRepresentation':"SW-DATA-DEF-PROPS", 
         '_artop_someipTransformationPropsRef':"AP-SOMEIP-TRANSFORMATION-PROPS"})

    @property
    def dataPrototypes_DataPrototypeInServiceInterfaceRef(self):
        return self._artop_dataPrototype

    @property
    def ref_networkRepresentation_(self):
        return self._artop_networkRepresentation

    @property
    def networkRepresentation_(self):
        if self._artop_networkRepresentation is not None:
            if hasattr(self._artop_networkRepresentation, "uuid"):
                return self._artop_networkRepresentation.uuid
        return

    @property
    def ref_someipTransformationProps_(self):
        return self._artop_someipTransformationPropsRef

    @property
    def someipTransformationProps_(self):
        if self._artop_someipTransformationPropsRef is not None:
            if hasattr(self._artop_someipTransformationPropsRef, "uuid"):
                return self._artop_someipTransformationPropsRef.uuid
        return
