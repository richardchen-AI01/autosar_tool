# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping.py
from .ServiceInstanceToSwClusterDesignPortPrototypeMapping import ServiceInstanceToSwClusterDesignPortPrototypeMapping

class ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping(ServiceInstanceToSwClusterDesignPortPrototypeMapping):

    def __init__(self):
        super().__init__()
        from .PPortPrototypeInSoftwareClusterDesignInstanceRef import PPortPrototypeInSoftwareClusterDesignInstanceRef
        from .ProvidedApServiceInstance import ProvidedApServiceInstance
        self._artop_providedPortPrototypeIref = None
        self._artop_providedServiceInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providedPortPrototypeIref':"P-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF", 
         '_artop_providedServiceInstanceRef':"PROVIDED-AP-SERVICE-INSTANCE"})

    @property
    def ref_providedPortPrototype_(self):
        return self._artop_providedPortPrototypeIref

    @property
    def providedPortPrototype_(self):
        if self._artop_providedPortPrototypeIref is not None:
            if hasattr(self._artop_providedPortPrototypeIref, "uuid"):
                return self._artop_providedPortPrototypeIref.uuid
        return

    @property
    def ref_providedServiceInstance_(self):
        return self._artop_providedServiceInstanceRef

    @property
    def providedServiceInstance_(self):
        if self._artop_providedServiceInstanceRef is not None:
            if hasattr(self._artop_providedServiceInstanceRef, "uuid"):
                return self._artop_providedServiceInstanceRef.uuid
        return
