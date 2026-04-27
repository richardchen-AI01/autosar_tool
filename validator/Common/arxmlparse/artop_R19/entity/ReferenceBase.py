# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReferenceBase.py
from .ARObject import ARObject

class ReferenceBase(ARObject):

    def __init__(self):
        super().__init__()
        from .ARPackage import ARPackage
        self._artop_shortLabel = None
        self._artop_isDefault = None
        self._artop_isGlobal = None
        self._artop_baseIsThisPackage = None
        self._artop_globalElement = None
        self._artop_arPackage = None
        self._artop_globalInPackageRef = []
        self._artop_packageRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_arPackage':"AR-PACKAGE", 
         '_artop_globalInPackageRef':"AR-PACKAGE", 
         '_artop_packageRef':"AR-PACKAGE"})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def isDefault_(self):
        if self._artop_isDefault:
            if self._artop_isDefault == "true":
                return True
            return False
        else:
            return self._artop_isDefault

    @property
    def isGlobal_(self):
        if self._artop_isGlobal:
            if self._artop_isGlobal == "true":
                return True
            return False
        else:
            return self._artop_isGlobal

    @property
    def baseIsThisPackage_(self):
        if self._artop_baseIsThisPackage:
            if self._artop_baseIsThisPackage == "true":
                return True
            return False
        else:
            return self._artop_baseIsThisPackage

    @property
    def globalElement_(self):
        return self._artop_globalElement

    @property
    def ref_aRPackage_(self):
        return self._artop_arPackage

    @property
    def aRPackage_(self):
        if self._artop_arPackage is not None:
            if hasattr(self._artop_arPackage, "uuid"):
                return self._artop_arPackage.uuid
        return

    @property
    def ref_globalInPackages_(self):
        return self._artop_globalInPackageRef

    @property
    def globalInPackages_(self):
        return self._artop_globalInPackageRef

    @property
    def ref_package_(self):
        return self._artop_packageRef

    @property
    def package_(self):
        if self._artop_packageRef is not None:
            if hasattr(self._artop_packageRef, "uuid"):
                return self._artop_packageRef.uuid
        return
