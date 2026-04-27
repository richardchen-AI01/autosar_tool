# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DependencyOnArtifact.py
from .Identifiable import Identifiable

class DependencyOnArtifact(Identifiable):

    def __init__(self):
        super().__init__()
        from .AutosarEngineeringObject import AutosarEngineeringObject
        from .VariationPoint import VariationPoint
        self._artop_usage = None
        self._artop_artifactDescriptor = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_artifactDescriptor':"AUTOSAR-ENGINEERING-OBJECT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def usage_(self):
        return self._artop_usage

    @property
    def ref_artifactDescriptor_(self):
        return self._artop_artifactDescriptor

    @property
    def artifactDescriptor_(self):
        if self._artop_artifactDescriptor is not None:
            if hasattr(self._artop_artifactDescriptor, "uuid"):
                return self._artop_artifactDescriptor.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
