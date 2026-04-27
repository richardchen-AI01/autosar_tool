# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransformationTechnology.py
from .Identifiable import Identifiable

class TransformationTechnology(Identifiable):

    def __init__(self):
        super().__init__()
        from .DataTransformationSet import DataTransformationSet
        from .BufferProperties import BufferProperties
        from .TransformationDescription import TransformationDescription
        from .VariationPoint import VariationPoint
        self._artop_hasInternalState = None
        self._artop_needsOriginalData = None
        self._artop_protocol = None
        self._artop_transformerClass = None
        self._artop_version = None
        self._artop_dataTransformationSet = None
        self._artop_bufferProperties = None
        self._artop_transformationDescription = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dataTransformationSet': '"DATA-TRANSFORMATION-SET"', 
         '_artop_bufferProperties': '"BUFFER-PROPERTIES"', 
         '_artop_transformationDescription': '"TRANSFORMATION-DESCRIPTION"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def hasInternalState_(self):
        if self._artop_hasInternalState:
            if self._artop_hasInternalState == "true":
                return True
            return False
        else:
            return self._artop_hasInternalState

    @property
    def needsOriginalData_(self):
        if self._artop_needsOriginalData:
            if self._artop_needsOriginalData == "true":
                return True
            return False
        else:
            return self._artop_needsOriginalData

    @property
    def protocol_(self):
        return self._artop_protocol

    @property
    def transformerClass_(self):
        return self._artop_transformerClass

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_dataTransformationSet_(self):
        return self._artop_dataTransformationSet

    @property
    def dataTransformationSet_(self):
        if self._artop_dataTransformationSet is not None:
            if hasattr(self._artop_dataTransformationSet, "uuid"):
                return self._artop_dataTransformationSet.uuid
        return

    @property
    def ref_bufferProperties_(self):
        return self._artop_bufferProperties

    @property
    def bufferProperties_(self):
        if self._artop_bufferProperties is not None:
            if hasattr(self._artop_bufferProperties, "uuid"):
                return self._artop_bufferProperties.uuid
        return

    @property
    def transformationDescriptions_TransformationDescription(self):
        return self._artop_transformationDescription

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
