# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryP2.py
from .ARObject import ARObject

class MsrQueryP2(ARObject):

    def __init__(self):
        super().__init__()
        from .DocumentationBlock import DocumentationBlock
        from .MsrQueryProps import MsrQueryProps
        self._artop_documentationBlock = None
        self._artop_msrQueryProps = None
        self._artop_msrQueryResultP2 = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_documentationBlock':"DOCUMENTATION-BLOCK", 
         '_artop_msrQueryProps':"MSR-QUERY-PROPS", 
         '_artop_msrQueryResultP2':"DOCUMENTATION-BLOCK"})

    @property
    def ref_documentationBlock_(self):
        return self._artop_documentationBlock

    @property
    def documentationBlock_(self):
        if self._artop_documentationBlock is not None:
            if hasattr(self._artop_documentationBlock, "uuid"):
                return self._artop_documentationBlock.uuid
        return

    @property
    def ref_msrQueryProps_(self):
        return self._artop_msrQueryProps

    @property
    def msrQueryProps_(self):
        if self._artop_msrQueryProps is not None:
            if hasattr(self._artop_msrQueryProps, "uuid"):
                return self._artop_msrQueryProps.uuid
        return

    @property
    def ref_msrQueryResultP2_(self):
        return self._artop_msrQueryResultP2

    @property
    def msrQueryResultP2_(self):
        if self._artop_msrQueryResultP2 is not None:
            if hasattr(self._artop_msrQueryResultP2, "uuid"):
                return self._artop_msrQueryResultP2.uuid
        return
