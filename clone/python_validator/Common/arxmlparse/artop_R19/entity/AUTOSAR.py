# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AUTOSAR.py
from .ARObject import ARObject

class AUTOSAR(ARObject):

    def __init__(self):
        super().__init__()
        from .FileInfoComment import FileInfoComment
        from .AdminData import AdminData
        from .DocumentationBlock import DocumentationBlock
        from .ARPackage import ARPackage
        from .AUTOSARAllExtensionsMapEntry import AUTOSARAllExtensionsMapEntry
        self._artop_mixed = None
        self._artop_mixedoutercontent = None
        self._artop_fileInfoComment = None
        self._artop_adminData = None
        self._artop_introduction = None
        self._artop_arPackage = []
        self._artop_allextensions = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_fileInfoComment': '"FILE-INFO-COMMENT"', 
         '_artop_adminData': '"ADMIN-DATA"', 
         '_artop_introduction': '"DOCUMENTATION-BLOCK"', 
         '_artop_arPackage': '"AR-PACKAGE"'})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def mixedoutercontent_(self):
        return self._artop_mixedoutercontent

    @property
    def ref_fileInfoComment_(self):
        return self._artop_fileInfoComment

    @property
    def fileInfoComment_(self):
        if self._artop_fileInfoComment is not None:
            if hasattr(self._artop_fileInfoComment, "uuid"):
                return self._artop_fileInfoComment.uuid
        return

    @property
    def ref_adminData_(self):
        return self._artop_adminData

    @property
    def adminData_(self):
        if self._artop_adminData is not None:
            if hasattr(self._artop_adminData, "uuid"):
                return self._artop_adminData.uuid
        return

    @property
    def ref_introduction_(self):
        return self._artop_introduction

    @property
    def introduction_(self):
        if self._artop_introduction is not None:
            if hasattr(self._artop_introduction, "uuid"):
                return self._artop_introduction.uuid
        return

    @property
    def arPackages_ARPackage(self):
        return self._artop_arPackage

    @property
    def allExtensions_AUTOSARAllExtensionsMapEntry(self):
        return self._artop_allextensions
