# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataTransformationSet.py
from .ARElement import ARElement

class DataTransformationSet(ARElement):

    def __init__(self):
        super().__init__()
        from .DataTransformation import DataTransformation
        from .TransformationTechnology import TransformationTechnology
        self._artop_dataTransformation = []
        self._artop_transformationTechnology = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataTransformation':"DATA-TRANSFORMATION", 
         '_artop_transformationTechnology':"TRANSFORMATION-TECHNOLOGY"})

    @property
    def dataTransformations_DataTransformation(self):
        return self._artop_dataTransformation

    @property
    def transformationTechnologies_TransformationTechnology(self):
        return self._artop_transformationTechnology
