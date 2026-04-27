# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UserDefinedTransformationISignalProps.py
from .TransformationISignalProps import TransformationISignalProps

class UserDefinedTransformationISignalProps(TransformationISignalProps):

    def __init__(self):
        super().__init__()
        from .UserDefinedTransformationISignalPropsConditional import UserDefinedTransformationISignalPropsConditional
        self._artop_userDefinedTransformationISignalPropsVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_userDefinedTransformationISignalPropsVariant": "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"})

    @property
    def UserDefinedTransformationISignalPropsVariants_UserDefinedTransformationISignalPropsConditional(self):
        return self._artop_userDefinedTransformationISignalPropsVariant
