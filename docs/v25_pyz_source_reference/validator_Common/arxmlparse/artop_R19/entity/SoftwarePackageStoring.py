# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwarePackageStoring.py
from .ARObject import ARObject

class SoftwarePackageStoring(ARObject):

    def __init__(self):
        super().__init__()
        from .SoftwarePackageStep import SoftwarePackageStep
        from .SoftwarePackage import SoftwarePackage
        self._artop_storing = None
        self._artop_softwarePackageStep = None
        self._artop_transferRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_softwarePackageStep':"SOFTWARE-PACKAGE-STEP", 
         '_artop_transferRef':"SOFTWARE-PACKAGE"})

    @property
    def storing_(self):
        return self._artop_storing

    @property
    def ref_softwarePackageStep_(self):
        return self._artop_softwarePackageStep

    @property
    def softwarePackageStep_(self):
        if self._artop_softwarePackageStep is not None:
            if hasattr(self._artop_softwarePackageStep, "uuid"):
                return self._artop_softwarePackageStep.uuid
        return

    @property
    def ref_transfers_(self):
        return self._artop_transferRef

    @property
    def transfers_(self):
        return self._artop_transferRef
