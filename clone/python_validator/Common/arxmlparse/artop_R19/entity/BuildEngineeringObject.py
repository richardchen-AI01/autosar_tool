# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildEngineeringObject.py
from .EngineeringObject import EngineeringObject

class BuildEngineeringObject(EngineeringObject):

    def __init__(self):
        super().__init__()
        from .BuildActionIoElement import BuildActionIoElement
        self._artop_fileType = None
        self._artop_intendedFilename = None
        self._artop_parentCategory = None
        self._artop_parentShortLabel = None
        self._artop_shortLabelPattern = None
        self._artop_fileTypePattern = None
        self._artop_buildActionIoElement = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_buildActionIoElement": "BUILD-ACTION-IO-ELEMENT"})

    @property
    def fileType_(self):
        return self._artop_fileType

    @property
    def intendedFilename_(self):
        return self._artop_intendedFilename

    @property
    def parentCategory_(self):
        return self._artop_parentCategory

    @property
    def parentShortLabel_(self):
        return self._artop_parentShortLabel

    @property
    def shortLabelPattern_(self):
        return self._artop_shortLabelPattern

    @property
    def fileTypePattern_(self):
        return self._artop_fileTypePattern

    @property
    def ref_buildActionIoElement_(self):
        return self._artop_buildActionIoElement

    @property
    def buildActionIoElement_(self):
        if self._artop_buildActionIoElement is not None:
            if hasattr(self._artop_buildActionIoElement, "uuid"):
                return self._artop_buildActionIoElement.uuid
        return
