# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RPortPrototypeInSoftwareClusterDesignInstanceRef.py
from .AbstractPortPrototypeInSoftwareClusterDesignInstanceRef import AbstractPortPrototypeInSoftwareClusterDesignInstanceRef

class RPortPrototypeInSoftwareClusterDesignInstanceRef(AbstractPortPrototypeInSoftwareClusterDesignInstanceRef):

    def __init__(self):
        super().__init__()
        from .SoftwareClusterDesign import SoftwareClusterDesign
        from .RootSwClusterDesignComponentPrototype import RootSwClusterDesignComponentPrototype
        from .SwComponentPrototype import SwComponentPrototype
        from .RPortPrototype import RPortPrototype
        self._artop_softwareClusterDesign = None
        self._artop_contextRootSwClusterDesignComponentPrototypeRef = None
        self._artop_contextSwComponentPrototypeRef = []
        self._artop_targetRPortPrototypeRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_softwareClusterDesign': '"SOFTWARE-CLUSTER-DESIGN"', 
         '_artop_contextRootSwClusterDesignComponentPrototypeRef': '"ROOT-SW-CLUSTER-DESIGN-COMPONENT-PROTOTYPE"', 
         '_artop_contextSwComponentPrototypeRef': '"SW-COMPONENT-PROTOTYPE"', 
         '_artop_targetRPortPrototypeRef': '"R-PORT-PROTOTYPE"'})

    @property
    def ref_base_(self):
        return self._artop_softwareClusterDesign

    @property
    def base_(self):
        if self._artop_softwareClusterDesign is not None:
            if hasattr(self._artop_softwareClusterDesign, "uuid"):
                return self._artop_softwareClusterDesign.uuid
        return

    @property
    def ref_contextRootSwClusterDesignComponentPrototype_(self):
        return self._artop_contextRootSwClusterDesignComponentPrototypeRef

    @property
    def contextRootSwClusterDesignComponentPrototype_(self):
        if self._artop_contextRootSwClusterDesignComponentPrototypeRef is not None:
            if hasattr(self._artop_contextRootSwClusterDesignComponentPrototypeRef, "uuid"):
                return self._artop_contextRootSwClusterDesignComponentPrototypeRef.uuid
        return

    @property
    def ref_contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def contextSwComponentPrototypes_(self):
        return self._artop_contextSwComponentPrototypeRef

    @property
    def ref_targetRPortPrototype_(self):
        return self._artop_targetRPortPrototypeRef

    @property
    def targetRPortPrototype_(self):
        if self._artop_targetRPortPrototypeRef is not None:
            if hasattr(self._artop_targetRPortPrototypeRef, "uuid"):
                return self._artop_targetRPortPrototypeRef.uuid
        return
