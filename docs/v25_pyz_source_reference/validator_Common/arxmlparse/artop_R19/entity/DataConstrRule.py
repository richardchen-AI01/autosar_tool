# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataConstrRule.py
from .ARObject import ARObject

class DataConstrRule(ARObject):

    def __init__(self):
        super().__init__()
        from .DataConstr import DataConstr
        from .PhysConstrs import PhysConstrs
        from .InternalConstrs import InternalConstrs
        self._artop_constrLevel = None
        self._artop_dataConstr = None
        self._artop_physConstrs = None
        self._artop_internalConstrs = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataConstr':"DATA-CONSTR", 
         '_artop_physConstrs':"PHYS-CONSTRS", 
         '_artop_internalConstrs':"INTERNAL-CONSTRS"})

    @property
    def constrLevel_(self):
        if self._artop_constrLevel:
            return int(self._artop_constrLevel)
        return self._artop_constrLevel

    @property
    def ref_dataConstr_(self):
        return self._artop_dataConstr

    @property
    def dataConstr_(self):
        if self._artop_dataConstr is not None:
            if hasattr(self._artop_dataConstr, "uuid"):
                return self._artop_dataConstr.uuid
        return

    @property
    def ref_physConstrs_(self):
        return self._artop_physConstrs

    @property
    def physConstrs_(self):
        if self._artop_physConstrs is not None:
            if hasattr(self._artop_physConstrs, "uuid"):
                return self._artop_physConstrs.uuid
        return

    @property
    def ref_internalConstrs_(self):
        return self._artop_internalConstrs

    @property
    def internalConstrs_(self):
        if self._artop_internalConstrs is not None:
            if hasattr(self._artop_internalConstrs, "uuid"):
                return self._artop_internalConstrs.uuid
        return
