# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MsrQueryArg.py
from .ARObject import ARObject

class MsrQueryArg(ARObject):

    def __init__(self):
        super().__init__()
        from .MsrQueryProps import MsrQueryProps
        self._artop_arg = None
        self._artop_si = None
        self._artop_msrQueryProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_msrQueryProps": "MSR-QUERY-PROPS"})

    @property
    def arg_(self):
        return self._artop_arg

    @property
    def si_(self):
        return self._artop_si

    @property
    def ref_msrQueryProps_(self):
        return self._artop_msrQueryProps

    @property
    def msrQueryProps_(self):
        if self._artop_msrQueryProps is not None:
            if hasattr(self._artop_msrQueryProps, "uuid"):
                return self._artop_msrQueryProps.uuid
        return
