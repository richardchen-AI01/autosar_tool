# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BufferProperties.py
from .ARObject import ARObject

class BufferProperties(ARObject):

    def __init__(self):
        super().__init__()
        from .TransformationTechnology import TransformationTechnology
        from .CompuScale import CompuScale
        self._artop_headerLength = None
        self._artop_inPlace = None
        self._artop_transformationTechnology = None
        self._artop_bufferComputation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_transformationTechnology':"TRANSFORMATION-TECHNOLOGY", 
         '_artop_bufferComputation':"COMPU-SCALE"})

    @property
    def headerLength_(self):
        if self._artop_headerLength:
            return int(self._artop_headerLength)
        return self._artop_headerLength

    @property
    def inPlace_(self):
        if self._artop_inPlace:
            if self._artop_inPlace == "true":
                return True
            return False
        else:
            return self._artop_inPlace

    @property
    def ref_transformationTechnology_(self):
        return self._artop_transformationTechnology

    @property
    def transformationTechnology_(self):
        if self._artop_transformationTechnology is not None:
            if hasattr(self._artop_transformationTechnology, "uuid"):
                return self._artop_transformationTechnology.uuid
        return

    @property
    def ref_bufferComputation_(self):
        return self._artop_bufferComputation

    @property
    def bufferComputation_(self):
        if self._artop_bufferComputation is not None:
            if hasattr(self._artop_bufferComputation, "uuid"):
                return self._artop_bufferComputation.uuid
        return
