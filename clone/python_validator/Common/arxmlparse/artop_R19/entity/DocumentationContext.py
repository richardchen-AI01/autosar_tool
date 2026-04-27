# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DocumentationContext.py
from .MultilanguageReferrable import MultilanguageReferrable

class DocumentationContext(MultilanguageReferrable):

    def __init__(self):
        super().__init__()
        from .Documentation import Documentation
        from .AnyInstanceRef import AnyInstanceRef
        from .Identifiable import Identifiable
        self._artop_documentation = None
        self._artop_featureIref = None
        self._artop_identifiableRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_documentation':"DOCUMENTATION", 
         '_artop_featureIref':"ANY-INSTANCE-REF-IREF", 
         '_artop_identifiableRef':"IDENTIFIABLE"})

    @property
    def ref_documentation_(self):
        return self._artop_documentation

    @property
    def documentation_(self):
        if self._artop_documentation is not None:
            if hasattr(self._artop_documentation, "uuid"):
                return self._artop_documentation.uuid
        return

    @property
    def ref_feature_(self):
        return self._artop_featureIref

    @property
    def feature_(self):
        if self._artop_featureIref is not None:
            if hasattr(self._artop_featureIref, "uuid"):
                return self._artop_featureIref.uuid
        return

    @property
    def ref_identifiable_(self):
        return self._artop_identifiableRef

    @property
    def identifiable_(self):
        if self._artop_identifiableRef is not None:
            if hasattr(self._artop_identifiableRef, "uuid"):
                return self._artop_identifiableRef.uuid
        return
