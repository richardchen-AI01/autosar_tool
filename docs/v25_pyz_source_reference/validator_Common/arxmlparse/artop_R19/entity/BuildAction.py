# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BuildAction.py
from .BuildActionEntity import BuildActionEntity

class BuildAction(BuildActionEntity):

    def __init__(self):
        super().__init__()
        from .BuildActionManifest import BuildActionManifest
        from .BuildActionIoElement import BuildActionIoElement
        from .BuildActionEnvironment import BuildActionEnvironment
        from .VariationPoint import VariationPoint
        self._artop_buildActionManifest = None
        self._artop_predecessorActionRef = []
        self._artop_followUpActionRef = []
        self._artop_createdData = []
        self._artop_inputData = []
        self._artop_modifiedData = []
        self._artop_requiredEnvironmentRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_buildActionManifest': '"BUILD-ACTION-MANIFEST"', 
         '_artop_predecessorActionRef': '"BUILD-ACTION"', 
         '_artop_followUpActionRef': '"BUILD-ACTION"', 
         '_artop_createdData': '"BUILD-ACTION-IO-ELEMENT"', 
         '_artop_inputData': '"BUILD-ACTION-IO-ELEMENT"', 
         '_artop_modifiedData': '"BUILD-ACTION-IO-ELEMENT"', 
         '_artop_requiredEnvironmentRef': '"BUILD-ACTION-ENVIRONMENT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_buildActionManifest_(self):
        return self._artop_buildActionManifest

    @property
    def buildActionManifest_(self):
        if self._artop_buildActionManifest is not None:
            if hasattr(self._artop_buildActionManifest, "uuid"):
                return self._artop_buildActionManifest.uuid
        return

    @property
    def ref_predecessorActions_(self):
        return self._artop_predecessorActionRef

    @property
    def predecessorActions_(self):
        return self._artop_predecessorActionRef

    @property
    def ref_followUpActions_(self):
        return self._artop_followUpActionRef

    @property
    def followUpActions_(self):
        return self._artop_followUpActionRef

    @property
    def createdDatas_BuildActionIoElement(self):
        return self._artop_createdData

    @property
    def inputDatas_BuildActionIoElement(self):
        return self._artop_inputData

    @property
    def modifiedDatas_BuildActionIoElement(self):
        return self._artop_modifiedData

    @property
    def ref_requiredEnvironment_(self):
        return self._artop_requiredEnvironmentRef

    @property
    def requiredEnvironment_(self):
        if self._artop_requiredEnvironmentRef is not None:
            if hasattr(self._artop_requiredEnvironmentRef, "uuid"):
                return self._artop_requiredEnvironmentRef.uuid
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
