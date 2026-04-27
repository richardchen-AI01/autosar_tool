# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwDataDefProps.py
from .ARObject import ARObject

class SwDataDefProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SwDataDefPropsConditional import SwDataDefPropsConditional
        self._artop_swDataDefPropsVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swDataDefPropsVariant": "SW-DATA-DEF-PROPS-CONDITIONAL"})

    @property
    def SwDataDefPropsVariants_SwDataDefPropsConditional(self):
        return self._artop_swDataDefPropsVariant
