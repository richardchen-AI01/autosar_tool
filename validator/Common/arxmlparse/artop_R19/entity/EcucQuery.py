# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcucQuery.py
from .Identifiable import Identifiable

class EcucQuery(Identifiable):

    def __init__(self):
        super().__init__()
        from .EcucQueryExpression import EcucQueryExpression
        self._artop_ecucQueryExpression = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecucQueryExpression": "ECUC-QUERY-EXPRESSION"})

    @property
    def ref_ecucQueryExpression_(self):
        return self._artop_ecucQueryExpression

    @property
    def ecucQueryExpression_(self):
        if self._artop_ecucQueryExpression is not None:
            if hasattr(self._artop_ecucQueryExpression, "uuid"):
                return self._artop_ecucQueryExpression.uuid
        return
