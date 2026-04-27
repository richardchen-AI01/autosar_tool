# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping.py
from .ServiceInstanceToSwClusterDesignPortPrototypeMapping import ServiceInstanceToSwClusterDesignPortPrototypeMapping

class RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping(ServiceInstanceToSwClusterDesignPortPrototypeMapping):

    def __init__(self):
        super().__init__()
        from .RPortPrototypeInSoftwareClusterDesignInstanceRef import RPortPrototypeInSoftwareClusterDesignInstanceRef
        from .ProvidedApServiceInstance import ProvidedApServiceInstance
        self._artop_requiredPortPrototypeIref = None
        self._artop_requiredServiceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_requiredPortPrototypeIref':"R-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF", 
         '_artop_requiredServiceInstanceRef':"PROVIDED-AP-SERVICE-INSTANCE"})

    @property
    def ref_requiredPortPrototype_(self):
        return self._artop_requiredPortPrototypeIref

    @property
    def requiredPortPrototype_(self):
        if self._artop_requiredPortPrototypeIref is not None:
            if hasattr(self._artop_requiredPortPrototypeIref, "uuid"):
                return self._artop_requiredPortPrototypeIref.uuid
        return

    @property
    def ref_requiredServiceInstance_(self):
        return self._artop_requiredServiceInstanceRef

    @property
    def requiredServiceInstance_(self):
        if self._artop_requiredServiceInstanceRef is not None:
            if hasattr(self._artop_requiredServiceInstanceRef, "uuid"):
                return self._artop_requiredServiceInstanceRef.uuid
        return
