# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DocumentationBlock.py
from .ARObject import ARObject

class DocumentationBlock(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryP2 import MsrQueryP2
        from .MultiLanguageParagraph import MultiLanguageParagraph
        from .MultiLanguageVerbatim import MultiLanguageVerbatim
        from .List import List
        from .DefList import DefList
        from .LabeledList import LabeledList
        from .MlFormula import MlFormula
        from .MlFigure import MlFigure
        from .Note import Note
        from .TraceableText import TraceableText
        from .StructuredReq import StructuredReq
        self._artop_mixed = None
        self._artop_msrQueryP2 = []
        self._artop_p = []
        self._artop_verbatim = []
        self._artop_list = []
        self._artop_defList = []
        self._artop_labeledList = []
        self._artop_formula = []
        self._artop_figure = []
        self._artop_note = []
        self._artop_trace = []
        self._artop_structuredReq = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_msrQueryP2': '"MSR-QUERY-P-2"', 
         '_artop_p': '"MULTI-LANGUAGE-PARAGRAPH"', 
         '_artop_verbatim': '"MULTI-LANGUAGE-VERBATIM"', 
         '_artop_list': '"LIST"', 
         '_artop_defList': '"DEF-LIST"', 
         '_artop_labeledList': '"LABELED-LIST"', 
         '_artop_formula': '"ML-FORMULA"', 
         '_artop_figure': '"ML-FIGURE"', 
         '_artop_note': '"NOTE"', 
         '_artop_trace': '"TRACEABLE-TEXT"', 
         '_artop_structuredReq': '"STRUCTURED-REQ"'})

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def msrQueryP2s_MsrQueryP2(self):
        return self._artop_msrQueryP2

    @property
    def ps_MultiLanguageParagraph(self):
        return self._artop_p

    @property
    def verbatims_MultiLanguageVerbatim(self):
        return self._artop_verbatim

    @property
    def lists_List(self):
        return self._artop_list

    @property
    def defLists_DefList(self):
        return self._artop_defList

    @property
    def labeledLists_LabeledList(self):
        return self._artop_labeledList

    @property
    def formulas_MlFormula(self):
        return self._artop_formula

    @property
    def figures_MlFigure(self):
        return self._artop_figure

    @property
    def notes_Note(self):
        return self._artop_note

    @property
    def traces_TraceableText(self):
        return self._artop_trace

    @property
    def structuredReqs_StructuredReq(self):
        return self._artop_structuredReq
