# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwComponentDocumentation.py
from .ARObject import ARObject

class SwComponentDocumentation(ARObject):

    def __init__(self):
        super().__init__()
        from .Chapter import Chapter
        from .VariationPoint import VariationPoint
        self._artop_swFeatureDef = None
        self._artop_swFeatureDesc = None
        self._artop_swTestDesc = None
        self._artop_swCalibrationNotes = None
        self._artop_swMaintenanceNotes = None
        self._artop_swDiagnosticsNotes = None
        self._artop_swCarbDoc = None
        self._artop_chapter = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swFeatureDef': '"CHAPTER"', 
         '_artop_swFeatureDesc': '"CHAPTER"', 
         '_artop_swTestDesc': '"CHAPTER"', 
         '_artop_swCalibrationNotes': '"CHAPTER"', 
         '_artop_swMaintenanceNotes': '"CHAPTER"', 
         '_artop_swDiagnosticsNotes': '"CHAPTER"', 
         '_artop_swCarbDoc': '"CHAPTER"', 
         '_artop_chapter': '"CHAPTER"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_swFeatureDef_(self):
        return self._artop_swFeatureDef

    @property
    def swFeatureDef_(self):
        if self._artop_swFeatureDef is not None:
            if hasattr(self._artop_swFeatureDef, "uuid"):
                return self._artop_swFeatureDef.uuid
        return

    @property
    def ref_swFeatureDesc_(self):
        return self._artop_swFeatureDesc

    @property
    def swFeatureDesc_(self):
        if self._artop_swFeatureDesc is not None:
            if hasattr(self._artop_swFeatureDesc, "uuid"):
                return self._artop_swFeatureDesc.uuid
        return

    @property
    def ref_swTestDesc_(self):
        return self._artop_swTestDesc

    @property
    def swTestDesc_(self):
        if self._artop_swTestDesc is not None:
            if hasattr(self._artop_swTestDesc, "uuid"):
                return self._artop_swTestDesc.uuid
        return

    @property
    def ref_swCalibrationNotes_(self):
        return self._artop_swCalibrationNotes

    @property
    def swCalibrationNotes_(self):
        if self._artop_swCalibrationNotes is not None:
            if hasattr(self._artop_swCalibrationNotes, "uuid"):
                return self._artop_swCalibrationNotes.uuid
        return

    @property
    def ref_swMaintenanceNotes_(self):
        return self._artop_swMaintenanceNotes

    @property
    def swMaintenanceNotes_(self):
        if self._artop_swMaintenanceNotes is not None:
            if hasattr(self._artop_swMaintenanceNotes, "uuid"):
                return self._artop_swMaintenanceNotes.uuid
        return

    @property
    def ref_swDiagnosticsNotes_(self):
        return self._artop_swDiagnosticsNotes

    @property
    def swDiagnosticsNotes_(self):
        if self._artop_swDiagnosticsNotes is not None:
            if hasattr(self._artop_swDiagnosticsNotes, "uuid"):
                return self._artop_swDiagnosticsNotes.uuid
        return

    @property
    def ref_swCarbDoc_(self):
        return self._artop_swCarbDoc

    @property
    def swCarbDoc_(self):
        if self._artop_swCarbDoc is not None:
            if hasattr(self._artop_swCarbDoc, "uuid"):
                return self._artop_swCarbDoc.uuid
        return

    @property
    def chapters_Chapter(self):
        return self._artop_chapter

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
