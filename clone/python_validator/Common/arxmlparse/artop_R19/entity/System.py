# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\System.py
from .AtpStructureElement import AtpStructureElement
from .ARElement import ARElement

class System(ARElement, AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .Chapter import Chapter
        from .ClientIdDefinitionSet import ClientIdDefinitionSet
        from .FibexElementRefConditional import FibexElementRefConditional
        from .J1939SharedAddressCluster import J1939SharedAddressCluster
        from .SystemMapping import SystemMapping
        from .RootSwCompositionPrototype import RootSwCompositionPrototype
        self._artop_containerIPduHeaderByteOrder = None
        self._artop_ecuExtractVersion = None
        self._artop_pncVectorLength = None
        self._artop_pncVectorOffset = None
        self._artop_systemVersion = None
        self._artop_systemDocumentation = []
        self._artop_clientIdDefinitionSetRef = []
        self._artop_fibexElement = []
        self._artop_j1939SharedAddressCluster = []
        self._artop_mapping = []
        self._artop_rootSoftwareComposition = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_systemDocumentation': '"CHAPTER"', 
         '_artop_clientIdDefinitionSetRef': '"CLIENT-ID-DEFINITION-SET"', 
         '_artop_fibexElement': '"FIBEX-ELEMENT-REF-CONDITIONAL"', 
         '_artop_j1939SharedAddressCluster': '"J-1939-SHARED-ADDRESS-CLUSTER"', 
         '_artop_mapping': '"SYSTEM-MAPPING"', 
         '_artop_rootSoftwareComposition': '"ROOT-SW-COMPOSITION-PROTOTYPE"'})

    @property
    def containerIPduHeaderByteOrder_(self):
        return self._artop_containerIPduHeaderByteOrder

    @property
    def ecuExtractVersion_(self):
        return self._artop_ecuExtractVersion

    @property
    def pncVectorLength_(self):
        return self._artop_pncVectorLength

    @property
    def pncVectorOffset_(self):
        return self._artop_pncVectorOffset

    @property
    def systemVersion_(self):
        return self._artop_systemVersion

    @property
    def systemDocumentations_Chapter(self):
        return self._artop_systemDocumentation

    @property
    def ref_clientIdDefinitionSets_(self):
        return self._artop_clientIdDefinitionSetRef

    @property
    def clientIdDefinitionSets_(self):
        return self._artop_clientIdDefinitionSetRef

    @property
    def fibexElements_FibexElementRefConditional(self):
        return self._artop_fibexElement

    @property
    def j1939SharedAddressClusters_J1939SharedAddressCluster(self):
        return self._artop_j1939SharedAddressCluster

    @property
    def mappings_SystemMapping(self):
        return self._artop_mapping

    @property
    def rootSoftwareCompositions_RootSwCompositionPrototype(self):
        return self._artop_rootSoftwareComposition
