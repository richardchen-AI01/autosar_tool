# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoftwareActivationDependencyCompareCondition.py
from .SoftwareActivationDependencyFormulaPart import SoftwareActivationDependencyFormulaPart

class SoftwareActivationDependencyCompareCondition(SoftwareActivationDependencyFormulaPart):

    def __init__(self):
        super().__init__()
        from .SoftwareActivationDependency import SoftwareActivationDependency
        self._artop_compareType = None
        self._artop_considerBuildNumber = None
        self._artop_version = None
        self._artop_softwareActivationDependencyRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_softwareActivationDependencyRef": "SOFTWARE-ACTIVATION-DEPENDENCY"})

    @property
    def compareType_(self):
        return self._artop_compareType

    @property
    def considerBuildNumber_(self):
        if self._artop_considerBuildNumber:
            if self._artop_considerBuildNumber == "true":
                return True
            return False
        else:
            return self._artop_considerBuildNumber

    @property
    def version_(self):
        return self._artop_version

    @property
    def ref_softwareActivationDependency_(self):
        return self._artop_softwareActivationDependencyRef

    @property
    def softwareActivationDependency_(self):
        if self._artop_softwareActivationDependencyRef is not None:
            if hasattr(self._artop_softwareActivationDependencyRef, "uuid"):
                return self._artop_softwareActivationDependencyRef.uuid
        return
