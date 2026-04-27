# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AliasNameAssignment.py
from .ARObject import ARObject

class AliasNameAssignment(ARObject):

    def __init__(self):
        super().__init__()
        from .AliasNameSet import AliasNameSet
        from .MultilanguageLongName import MultilanguageLongName
        from .Identifiable import Identifiable
        from .FlatInstanceDescriptor import FlatInstanceDescriptor
        from .VariationPoint import VariationPoint
        self._artop_shortLabel = None
        self._artop_aliasNameSet = None
        self._artop_label = None
        self._artop_identifiableRef = None
        self._artop_flatInstanceRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_aliasNameSet': '"ALIAS-NAME-SET"', 
         '_artop_label': '"MULTILANGUAGE-LONG-NAME"', 
         '_artop_identifiableRef': '"IDENTIFIABLE"', 
         '_artop_flatInstanceRef': '"FLAT-INSTANCE-DESCRIPTOR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def ref_aliasNameSet_(self):
        return self._artop_aliasNameSet

    @property
    def aliasNameSet_(self):
        if self._artop_aliasNameSet is not None:
            if hasattr(self._artop_aliasNameSet, "uuid"):
                return self._artop_aliasNameSet.uuid
        return

    @property
    def ref_label_(self):
        return self._artop_label

    @property
    def label_(self):
        if self._artop_label is not None:
            if hasattr(self._artop_label, "uuid"):
                return self._artop_label.uuid
        return

    @property
    def ref_identifiable_(self):
        return self._artop_identifiableRef

    @property
    def identifiable_(self):
        if self._artop_identifiableRef is not None:
            if hasattr(self._artop_identifiableRef, "uuid"):
                return self._artop_identifiableRef.uuid
        return

    @property
    def ref_flatInstance_(self):
        return self._artop_flatInstanceRef

    @property
    def flatInstance_(self):
        if self._artop_flatInstanceRef is not None:
            if hasattr(self._artop_flatInstanceRef, "uuid"):
                return self._artop_flatInstanceRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
