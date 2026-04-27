# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwarePackageStep.py
from .Identifiable import Identifiable

class SoftwarePackageStep(Identifiable):

    def __init__(self):
        super().__init__()
        from .UcmStep import UcmStep
        from .SoftwarePackage import SoftwarePackage
        from .SoftwarePackageStoring import SoftwarePackageStoring
        self._artop_activationSwitch = None
        self._artop_ucmStep = None
        self._artop_preActivateRef = []
        self._artop_processRef = None
        self._artop_transfer = []
        self._artop_verifyRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ucmStep': '"UCM-STEP"', 
         '_artop_preActivateRef': '"SOFTWARE-PACKAGE"', 
         '_artop_processRef': '"SOFTWARE-PACKAGE"', 
         '_artop_transfer': '"SOFTWARE-PACKAGE-STORING"', 
         '_artop_verifyRef': '"SOFTWARE-PACKAGE"'})

    @property
    def activationSwitch_(self):
        if self._artop_activationSwitch:
            if self._artop_activationSwitch == "true":
                return True
            return False
        else:
            return self._artop_activationSwitch

    @property
    def ref_ucmStep_(self):
        return self._artop_ucmStep

    @property
    def ucmStep_(self):
        if self._artop_ucmStep is not None:
            if hasattr(self._artop_ucmStep, "uuid"):
                return self._artop_ucmStep.uuid
        return

    @property
    def ref_preActivates_(self):
        return self._artop_preActivateRef

    @property
    def preActivates_(self):
        return self._artop_preActivateRef

    @property
    def ref_process_(self):
        return self._artop_processRef

    @property
    def process_(self):
        if self._artop_processRef is not None:
            if hasattr(self._artop_processRef, "uuid"):
                return self._artop_processRef.uuid
        return

    @property
    def transfers_SoftwarePackageStoring(self):
        return self._artop_transfer

    @property
    def ref_verifies_(self):
        return self._artop_verifyRef

    @property
    def verifies_(self):
        return self._artop_verifyRef
