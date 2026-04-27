# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompositionPPortToExecutablePPortMapping.py
from .CompositionPortToExecutablePortMapping import CompositionPortToExecutablePortMapping

class CompositionPPortToExecutablePPortMapping(CompositionPortToExecutablePortMapping):

    def __init__(self):
        super().__init__()
        from .PPortPrototypeInExecutableInstanceRef import PPortPrototypeInExecutableInstanceRef
        from .PPortPrototypeInSoftwareClusterDesignInstanceRef import PPortPrototypeInSoftwareClusterDesignInstanceRef
        self._artop_executableProvidedPortIref = None
        self._artop_swClusterDesignProvidedPortIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_executableProvidedPortIref':"P-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_swClusterDesignProvidedPortIref':"P-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF"})

    @property
    def ref_executableProvidedPort_(self):
        return self._artop_executableProvidedPortIref

    @property
    def executableProvidedPort_(self):
        if self._artop_executableProvidedPortIref is not None:
            if hasattr(self._artop_executableProvidedPortIref, "uuid"):
                return self._artop_executableProvidedPortIref.uuid
        return

    @property
    def ref_swClusterDesignProvidedPort_(self):
        return self._artop_swClusterDesignProvidedPortIref

    @property
    def swClusterDesignProvidedPort_(self):
        if self._artop_swClusterDesignProvidedPortIref is not None:
            if hasattr(self._artop_swClusterDesignProvidedPortIref, "uuid"):
                return self._artop_swClusterDesignProvidedPortIref.uuid
        return
