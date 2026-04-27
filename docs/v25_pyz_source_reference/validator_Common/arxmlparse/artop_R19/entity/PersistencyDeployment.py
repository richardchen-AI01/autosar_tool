# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PersistencyDeployment.py
from .UploadablePackageElement import UploadablePackageElement

class PersistencyDeployment(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .PersistencyRedundancyHandling import PersistencyRedundancyHandling
        self._artop_maximumAllowedSize = None
        self._artop_minimumSustainedSize = None
        self._artop_updateStrategy = None
        self._artop_redundancyHandling = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_redundancyHandling": "PERSISTENCY-REDUNDANCY-HANDLING"})

    @property
    def maximumAllowedSize_(self):
        return self._artop_maximumAllowedSize

    @property
    def minimumSustainedSize_(self):
        return self._artop_minimumSustainedSize

    @property
    def updateStrategy_(self):
        return self._artop_updateStrategy

    @property
    def redundancyHandlings_PersistencyRedundancyHandling(self):
        return self._artop_redundancyHandling
