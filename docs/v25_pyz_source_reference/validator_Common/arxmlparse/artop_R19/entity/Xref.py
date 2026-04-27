# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Xref.py
from .ARObject import ARObject

class Xref(ARObject):

    def __init__(self):
        super().__init__()
        from .SingleLanguageLongName import SingleLanguageLongName
        from .Referrable import Referrable
        self._artop_resolutionPolicy = None
        self._artop_showContent = None
        self._artop_showResourceAliasName = None
        self._artop_showResourceCategory = None
        self._artop_showResourceLongName = None
        self._artop_showResourceNumber = None
        self._artop_showResourcePage = None
        self._artop_showResourceShortName = None
        self._artop_showResourceType = None
        self._artop_showSee = None
        self._artop_label1 = None
        self._artop_referrableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_label1':"SINGLE-LANGUAGE-LONG-NAME", 
         '_artop_referrableRef':"REFERRABLE"})

    @property
    def resolutionPolicy_(self):
        return self._artop_resolutionPolicy

    @property
    def showContent_(self):
        return self._artop_showContent

    @property
    def showResourceAliasName_(self):
        return self._artop_showResourceAliasName

    @property
    def showResourceCategory_(self):
        return self._artop_showResourceCategory

    @property
    def showResourceLongName_(self):
        return self._artop_showResourceLongName

    @property
    def showResourceNumber_(self):
        return self._artop_showResourceNumber

    @property
    def showResourcePage_(self):
        return self._artop_showResourcePage

    @property
    def showResourceShortName_(self):
        return self._artop_showResourceShortName

    @property
    def showResourceType_(self):
        return self._artop_showResourceType

    @property
    def showSee_(self):
        return self._artop_showSee

    @property
    def ref_label1_(self):
        return self._artop_label1

    @property
    def label1_(self):
        if self._artop_label1 is not None:
            if hasattr(self._artop_label1, "uuid"):
                return self._artop_label1.uuid
        return

    @property
    def ref_referrable_(self):
        return self._artop_referrableRef

    @property
    def referrable_(self):
        if self._artop_referrableRef is not None:
            if hasattr(self._artop_referrableRef, "uuid"):
                return self._artop_referrableRef.uuid
        return
