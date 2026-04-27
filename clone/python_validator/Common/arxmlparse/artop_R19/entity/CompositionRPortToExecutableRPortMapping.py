# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CompositionRPortToExecutableRPortMapping.py
from .CompositionPortToExecutablePortMapping import CompositionPortToExecutablePortMapping

class CompositionRPortToExecutableRPortMapping(CompositionPortToExecutablePortMapping):

    def __init__(self):
        super().__init__()
        from .RPortPrototypeInExecutableInstanceRef import RPortPrototypeInExecutableInstanceRef
        from .RPortPrototypeInSoftwareClusterDesignInstanceRef import RPortPrototypeInSoftwareClusterDesignInstanceRef
        self._artop_executableRequiredPortIref = None
        self._artop_swClusterDesignRequiredPortIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_executableRequiredPortIref':"R-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF", 
         '_artop_swClusterDesignRequiredPortIref':"R-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF"})

    @property
    def ref_executableRequiredPort_(self):
        return self._artop_executableRequiredPortIref

    @property
    def executableRequiredPort_(self):
        if self._artop_executableRequiredPortIref is not None:
            if hasattr(self._artop_executableRequiredPortIref, "uuid"):
                return self._artop_executableRequiredPortIref.uuid
        return

    @property
    def ref_swClusterDesignRequiredPort_(self):
        return self._artop_swClusterDesignRequiredPortIref

    @property
    def swClusterDesignRequiredPort_(self):
        if self._artop_swClusterDesignRequiredPortIref is not None:
            if hasattr(self._artop_swClusterDesignRequiredPortIref, "uuid"):
                return self._artop_swClusterDesignRequiredPortIref.uuid
        return
