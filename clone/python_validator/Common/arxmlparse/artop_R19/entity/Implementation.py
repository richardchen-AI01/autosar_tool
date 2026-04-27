# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Implementation.py
from .ARElement import ARElement

class Implementation(ARElement):

    def __init__(self):
        super().__init__()
        from .BuildActionManifestRefConditional import BuildActionManifestRefConditional
        from .Code import Code
        from .Compiler import Compiler
        from .DependencyOnArtifact import DependencyOnArtifact
        from .HwElement import HwElement
        from .Linker import Linker
        from .McSupportData import McSupportData
        from .ResourceConsumption import ResourceConsumption
        from .SwcBswMapping import SwcBswMapping
        self._artop_programmingLanguage = None
        self._artop_swVersion = None
        self._artop_usedCodeGenerator = None
        self._artop_vendorId = None
        self._artop_buildActionManifest = []
        self._artop_codeDescriptor = []
        self._artop_compiler = []
        self._artop_generatedArtifact = []
        self._artop_hwElementRef = []
        self._artop_linker = []
        self._artop_mcSupport = None
        self._artop_requiredArtifact = []
        self._artop_requiredGeneratorTool = []
        self._artop_resourceConsumption = None
        self._artop_swcBswMappingRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_buildActionManifest': '"BUILD-ACTION-MANIFEST-REF-CONDITIONAL"', 
         '_artop_codeDescriptor': '"CODE"', 
         '_artop_compiler': '"COMPILER"', 
         '_artop_generatedArtifact': '"DEPENDENCY-ON-ARTIFACT"', 
         '_artop_hwElementRef': '"HW-ELEMENT"', 
         '_artop_linker': '"LINKER"', 
         '_artop_mcSupport': '"MC-SUPPORT-DATA"', 
         '_artop_requiredArtifact': '"DEPENDENCY-ON-ARTIFACT"', 
         '_artop_requiredGeneratorTool': '"DEPENDENCY-ON-ARTIFACT"', 
         '_artop_resourceConsumption': '"RESOURCE-CONSUMPTION"', 
         '_artop_swcBswMappingRef': '"SWC-BSW-MAPPING"'})

    @property
    def programmingLanguage_(self):
        return self._artop_programmingLanguage

    @property
    def swVersion_(self):
        return self._artop_swVersion

    @property
    def usedCodeGenerator_(self):
        return self._artop_usedCodeGenerator

    @property
    def vendorId_(self):
        return self._artop_vendorId

    @property
    def buildActionManifests_BuildActionManifestRefConditional(self):
        return self._artop_buildActionManifest

    @property
    def codeDescriptors_Code(self):
        return self._artop_codeDescriptor

    @property
    def compilers_Compiler(self):
        return self._artop_compiler

    @property
    def generatedArtifacts_DependencyOnArtifact(self):
        return self._artop_generatedArtifact

    @property
    def ref_hwElements_(self):
        return self._artop_hwElementRef

    @property
    def hwElements_(self):
        return self._artop_hwElementRef

    @property
    def linkers_Linker(self):
        return self._artop_linker

    @property
    def ref_mcSupport_(self):
        return self._artop_mcSupport

    @property
    def mcSupport_(self):
        if self._artop_mcSupport is not None:
            if hasattr(self._artop_mcSupport, "uuid"):
                return self._artop_mcSupport.uuid
        return

    @property
    def requiredArtifacts_DependencyOnArtifact(self):
        return self._artop_requiredArtifact

    @property
    def requiredGeneratorTools_DependencyOnArtifact(self):
        return self._artop_requiredGeneratorTool

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return

    @property
    def ref_swcBswMapping_(self):
        return self._artop_swcBswMappingRef

    @property
    def swcBswMapping_(self):
        if self._artop_swcBswMappingRef is not None:
            if hasattr(self._artop_swcBswMappingRef, "uuid"):
                return self._artop_swcBswMappingRef.uuid
        return
