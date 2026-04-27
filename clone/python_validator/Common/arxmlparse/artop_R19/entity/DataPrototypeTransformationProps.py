# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeTransformationProps.py
from .ARObject import ARObject

class DataPrototypeTransformationProps(ARObject):

    def __init__(self):
        super().__init__()
        from .TransformationISignalPropsContent import TransformationISignalPropsContent
        from .DataPrototypeReference import DataPrototypeReference
        from .DataPrototypeInSystemRef import DataPrototypeInSystemRef
        from .SwDataDefProps import SwDataDefProps
        from .TransformationProps import TransformationProps
        self._artop_transformationISignalPropsContent = None
        self._artop_dataProtototypeInPortInterfaceRef = None
        self._artop_dataPrototypeRef = None
        self._artop_networkRepresentationProps = None
        self._artop_transformationPropsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_transformationISignalPropsContent': '"TRANSFORMATION-I-SIGNAL-PROPS-CONTENT"', 
         '_artop_dataProtototypeInPortInterfaceRef': '"DATA-PROTOTYPE-REFERENCE"', 
         '_artop_dataPrototypeRef': '"DATA-PROTOTYPE-IN-SYSTEM-REF"', 
         '_artop_networkRepresentationProps': '"SW-DATA-DEF-PROPS"', 
         '_artop_transformationPropsRef': '"TRANSFORMATION-PROPS"'})

    @property
    def ref_transformationISignalPropsContent_(self):
        return self._artop_transformationISignalPropsContent

    @property
    def transformationISignalPropsContent_(self):
        if self._artop_transformationISignalPropsContent is not None:
            if hasattr(self._artop_transformationISignalPropsContent, "uuid"):
                return self._artop_transformationISignalPropsContent.uuid
        return

    @property
    def ref_dataProtototypeInPortInterfaceRef_(self):
        return self._artop_dataProtototypeInPortInterfaceRef

    @property
    def dataProtototypeInPortInterfaceRef_(self):
        if self._artop_dataProtototypeInPortInterfaceRef is not None:
            if hasattr(self._artop_dataProtototypeInPortInterfaceRef, "uuid"):
                return self._artop_dataProtototypeInPortInterfaceRef.uuid
        return

    @property
    def ref_dataPrototypeRef_(self):
        return self._artop_dataPrototypeRef

    @property
    def dataPrototypeRef_(self):
        if self._artop_dataPrototypeRef is not None:
            if hasattr(self._artop_dataPrototypeRef, "uuid"):
                return self._artop_dataPrototypeRef.uuid
        return

    @property
    def ref_networkRepresentationProps_(self):
        return self._artop_networkRepresentationProps

    @property
    def networkRepresentationProps_(self):
        if self._artop_networkRepresentationProps is not None:
            if hasattr(self._artop_networkRepresentationProps, "uuid"):
                return self._artop_networkRepresentationProps.uuid
        return

    @property
    def ref_transformationProps_(self):
        return self._artop_transformationPropsRef

    @property
    def transformationProps_(self):
        if self._artop_transformationPropsRef is not None:
            if hasattr(self._artop_transformationPropsRef, "uuid"):
                return self._artop_transformationPropsRef.uuid
        return
