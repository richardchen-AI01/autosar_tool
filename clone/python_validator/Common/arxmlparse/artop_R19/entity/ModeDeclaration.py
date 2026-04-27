# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeDeclaration.py
from .AtpStructureElement import AtpStructureElement

class ModeDeclaration(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .ModeDeclarationGroup import ModeDeclarationGroup
        from .VariationPoint import VariationPoint
        self._artop_value = None
        self._artop_modeDeclarationGroup = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_modeDeclarationGroup':"MODE-DECLARATION-GROUP", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def value_(self):
        return self._artop_value

    @property
    def ref_modeDeclarationGroup_(self):
        return self._artop_modeDeclarationGroup

    @property
    def modeDeclarationGroup_(self):
        if self._artop_modeDeclarationGroup is not None:
            if hasattr(self._artop_modeDeclarationGroup, "uuid"):
                return self._artop_modeDeclarationGroup.uuid
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
