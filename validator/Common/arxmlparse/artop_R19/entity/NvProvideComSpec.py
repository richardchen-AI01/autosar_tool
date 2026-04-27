# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvProvideComSpec.py
from .PPortComSpec import PPortComSpec

class NvProvideComSpec(PPortComSpec):

    def __init__(self):
        super().__init__()
        from .ValueSpecification import ValueSpecification
        from .VariableDataPrototype import VariableDataPrototype
        self._artop_ramBlockInitValue = None
        self._artop_romBlockInitValue = None
        self._artop_variableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ramBlockInitValue':"VALUE-SPECIFICATION", 
         '_artop_romBlockInitValue':"VALUE-SPECIFICATION", 
         '_artop_variableRef':"VARIABLE-DATA-PROTOTYPE"})

    @property
    def ref_ramBlockInitValue_(self):
        return self._artop_ramBlockInitValue

    @property
    def ramBlockInitValue_(self):
        if self._artop_ramBlockInitValue is not None:
            if hasattr(self._artop_ramBlockInitValue, "uuid"):
                return self._artop_ramBlockInitValue.uuid
        return

    @property
    def ref_romBlockInitValue_(self):
        return self._artop_romBlockInitValue

    @property
    def romBlockInitValue_(self):
        if self._artop_romBlockInitValue is not None:
            if hasattr(self._artop_romBlockInitValue, "uuid"):
                return self._artop_romBlockInitValue.uuid
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
