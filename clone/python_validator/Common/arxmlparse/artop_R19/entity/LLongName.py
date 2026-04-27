# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LLongName.py
from .MixedContentForLongName import MixedContentForLongName
from .LanguageSpecific import LanguageSpecific

class LLongName(LanguageSpecific, MixedContentForLongName):

    def __init__(self):
        super().__init__()
        from .MultilanguageLongName import MultilanguageLongName
        self._artop_blueprintValue = None
        self._artop_multilanguageLongName = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_multilanguageLongName": "MULTILANGUAGE-LONG-NAME"})

    @property
    def blueprintValue_(self):
        return self._artop_blueprintValue

    @property
    def ref_multilanguageLongName_(self):
        return self._artop_multilanguageLongName

    @property
    def multilanguageLongName_(self):
        if self._artop_multilanguageLongName is not None:
            if hasattr(self._artop_multilanguageLongName, "uuid"):
                return self._artop_multilanguageLongName.uuid
        return
