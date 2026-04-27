# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipMethodProps.py
from .ARObject import ARObject

class SomeipMethodProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SomeipCollectionProps import SomeipCollectionProps
        from .SomeipMethodDeployment import SomeipMethodDeployment
        self._artop_collectionProps = None
        self._artop_methodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_collectionProps':"SOMEIP-COLLECTION-PROPS", 
         '_artop_methodRef':"SOMEIP-METHOD-DEPLOYMENT"})

    @property
    def ref_collectionProps_(self):
        return self._artop_collectionProps

    @property
    def collectionProps_(self):
        if self._artop_collectionProps is not None:
            if hasattr(self._artop_collectionProps, "uuid"):
                return self._artop_collectionProps.uuid
        return

    @property
    def ref_method_(self):
        return self._artop_methodRef

    @property
    def method_(self):
        if self._artop_methodRef is not None:
            if hasattr(self._artop_methodRef, "uuid"):
                return self._artop_methodRef.uuid
        return
