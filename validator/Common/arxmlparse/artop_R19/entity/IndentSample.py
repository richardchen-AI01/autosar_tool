# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\IndentSample.py
from .ARObject import ARObject

class IndentSample(ARObject):

    def __init__(self):
        super().__init__()
        from .LabeledList import LabeledList
        from .LOverviewParagraph import LOverviewParagraph
        self._artop_itemLabelPos = None
        self._artop_labeledList = None
        self._artop_l2 = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_labeledList':"LABELED-LIST", 
         '_artop_l2':"L-OVERVIEW-PARAGRAPH"})

    @property
    def itemLabelPos_(self):
        return self._artop_itemLabelPos

    @property
    def ref_labeledList_(self):
        return self._artop_labeledList

    @property
    def labeledList_(self):
        if self._artop_labeledList is not None:
            if hasattr(self._artop_labeledList, "uuid"):
                return self._artop_labeledList.uuid
        return

    @property
    def l2s_LOverviewParagraph(self):
        return self._artop_l2
