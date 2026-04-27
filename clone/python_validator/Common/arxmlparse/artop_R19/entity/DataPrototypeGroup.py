# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataPrototypeGroup.py
from .AtpStructureElement import AtpStructureElement

class DataPrototypeGroup(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .InnerDataPrototypeGroupInCompositionInstanceRef import InnerDataPrototypeGroupInCompositionInstanceRef
        from .VariableDataPrototypeInCompositionInstanceRef import VariableDataPrototypeInCompositionInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_dataPrototypeGroupIref = []
        self._artop_implicitDataAccessIref = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataPrototypeGroupIref':"INNER-DATA-PROTOTYPE-GROUP-IN-COMPOSITION-INSTANCE-REF-IREF", 
         '_artop_implicitDataAccessIref':"VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF-IREF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def dataPrototypeGroups_InnerDataPrototypeGroupInCompositionInstanceRef(self):
        return self._artop_dataPrototypeGroupIref

    @property
    def implicitDataAccess_VariableDataPrototypeInCompositionInstanceRef(self):
        return self._artop_implicitDataAccessIref

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
