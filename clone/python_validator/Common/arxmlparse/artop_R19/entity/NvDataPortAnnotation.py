# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvDataPortAnnotation.py
from .GeneralAnnotation import GeneralAnnotation

class NvDataPortAnnotation(GeneralAnnotation):

    def __init__(self):
        super().__init__()
        from .PortPrototype import PortPrototype
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_portPrototype = None
        self._artop_variableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_portPrototype':"PORT-PROTOTYPE", 
         '_artop_variableRef':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def ref_portPrototype_(self):
        return self._artop_portPrototype

    @property
    def portPrototype_(self):
        if self._artop_portPrototype is not None:
            if hasattr(self._artop_portPrototype, "uuid"):
                return self._artop_portPrototype.uuid
        return

    @property
    def ref_variable_(self):
        return self._artop_variableRef

    @property
    def variable_(self):
        if self._artop_variableRef is not None:
            if hasattr(self._artop_variableRef, "uuid"):
                return self._artop_variableRef.uuid
        return
