# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SingleLanguageReferrable.py
from .Referrable import Referrable

class SingleLanguageReferrable(Referrable):

    def __init__(self):
        super().__init__()
        from .SingleLanguageLongName import SingleLanguageLongName
        self._artop_longName1 = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_longName1": "SINGLE-LANGUAGE-LONG-NAME"})

    @property
    def ref_longName1_(self):
        return self._artop_longName1

    @property
    def longName1_(self):
        if self._artop_longName1 is not None:
            if hasattr(self._artop_longName1, "uuid"):
                return self._artop_longName1.uuid
        return
