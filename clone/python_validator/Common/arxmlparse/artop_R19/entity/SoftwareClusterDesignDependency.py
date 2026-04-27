# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareClusterDesignDependency.py
from .ARObject import ARObject

class SoftwareClusterDesignDependency(ARObject):

    def __init__(self):
        super().__init__()
        from .SoftwareClusterDesign import SoftwareClusterDesign
        self._artop_dependency = None
        self._artop_softwareClusterDesign = None
        self._artop_dependentSoftwareClusterDesignRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_softwareClusterDesign':"SOFTWARE-CLUSTER-DESIGN", 
         '_artop_dependentSoftwareClusterDesignRef':"SOFTWARE-CLUSTER-DESIGN"})

    @property
    def dependency_(self):
        return self._artop_dependency

    @property
    def ref_softwareClusterDesign_(self):
        return self._artop_softwareClusterDesign

    @property
    def softwareClusterDesign_(self):
        if self._artop_softwareClusterDesign is not None:
            if hasattr(self._artop_softwareClusterDesign, "uuid"):
                return self._artop_softwareClusterDesign.uuid
        return

    @property
    def ref_dependentSoftwareClusterDesign_(self):
        return self._artop_dependentSoftwareClusterDesignRef

    @property
    def dependentSoftwareClusterDesign_(self):
        if self._artop_dependentSoftwareClusterDesignRef is not None:
            if hasattr(self._artop_dependentSoftwareClusterDesignRef, "uuid"):
                return self._artop_dependentSoftwareClusterDesignRef.uuid
        return
