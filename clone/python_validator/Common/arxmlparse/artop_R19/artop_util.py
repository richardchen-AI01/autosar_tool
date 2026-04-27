# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\artop_util.py


def get_attribute_value(container, attribute_path_enum, variant_value=None):
    from .all_class_mulit import all_class_mulit
    from .entity import NumericalValueVariationPoint
    from .parse_file import has_rte
    attribute_path = attribute_path_enum.value
    if attribute_path.startswith("/AUTOSAR/Rte"):
        if not has_rte:
            attribute_path = attribute_path.replace("/AUTOSAR/Rte", "/AUTOSAR/iRte")
    mulit_tuple = all_class_mulit.get(attribute_path, None)
    if container:
        if attribute_path:
            if hasattr(container, "parameterValues_EcucParameterValue"):
                list_parameter_value = container.parameterValues_EcucParameterValue
                if list_parameter_value:
                    res_value = []
                    for parameter_value in list_parameter_value:
                        if parameter_value.ref_definition_ == attribute_path:
                            attribute_value = parameter_value._artop_value
                            if attribute_value is not None:
                                if isinstance(attribute_value, NumericalValueVariationPoint):
                                    attribute_value = attribute_value.mixed_
                                if mulit_tuple is not None:
                                    if mulit_tuple[1] != 1:
                                        res_value.append(attribute_value)
                                return attribute_value
                            if res_value:
                                if mulit_tuple is not None:
                                    if mulit_tuple[1] != 1:
                                        return res_value

            if hasattr(container, "referenceValues_EcucAbstractReferenceValue"):
                list_reference_value = container.referenceValues_EcucAbstractReferenceValue
                if list_reference_value:
                    res_value = []
                    for reference_value in list_reference_value:
                        if reference_value.ref_definition_ == attribute_path:
                            attribute_value = reference_value._artop_valueRef
                        if attribute_value is not None:
                            if isinstance(attribute_value, dict):
                                if mulit_tuple is not None:
                                    if mulit_tuple[1] != 1:
                                        if variant_value is not None:
                                            rel_obj = attribute_value.get(variant_value, None)
                                            rel_obj_default = attribute_value.get(-1, None)
                                            if rel_obj is not None:
                                                res_value.append(rel_obj)
                                        elif rel_obj_default is not None:
                                            res_value.append(rel_obj_default)
                                    else:
                                        res_value.extend(list(attribute_value.values()))
                                else:
                                    if variant_value is not None:
                                        rel_obj = attribute_value.get(variant_value, None)
                                        rel_obj_default = attribute_value.get(-1, None)
                                        if rel_obj is not None:
                                            return rel_obj
                                        if rel_obj_default is not None:
                                            return rel_obj_default
                                    else:
                                        return next(iter(attribute_value.values()), None)
                            elif mulit_tuple is not None:
                                if mulit_tuple[1] != 1:
                                    res_value.append(attribute_value)
                            return attribute_value

                    if res_value and mulit_tuple is not None:
                        if mulit_tuple[1] != 1:
                            return res_value
    if mulit_tuple is not None:
        if mulit_tuple[1] != 1:
            return []
    return


def get_subcontainer(container, attribute_path_enum=None, variant_value=None):
    from enum import Enum
    from .parse_file import has_rte
    res_subcontainer = []
    if container:
        if hasattr(container, "subContainers_EcucContainerValue"):
            list_subcontainer = container.subContainers_EcucContainerValue
            if list_subcontainer:
                if attribute_path_enum:
                    attribute_path = attribute_path_enum
                    if isinstance(attribute_path_enum, Enum):
                        attribute_path = attribute_path_enum.value
                    elif attribute_path.startswith("/AUTOSAR/Rte"):
                        if not has_rte:
                            attribute_path = attribute_path.replace("/AUTOSAR/Rte", "/AUTOSAR/iRte")
                    for subcontainer in list_subcontainer:
                        if isinstance(attribute_path_enum, Enum):
                            if subcontainer.ref_definition_ == attribute_path:
                                if subcontainer.v_id == -1:
                                    res_subcontainer.append(subcontainer)
                                else:
                                    if variant_value is not None and subcontainer.v_id == variant_value:
                                        res_subcontainer.append(subcontainer)
                                    else:
                                        if variant_value is None:
                                            res_subcontainer.append(subcontainer)

                    if subcontainer.ref_definition_.split("/")[-1] == attribute_path:
                        if subcontainer.v_id == -1:
                            res_subcontainer.append(subcontainer)
                        elif subcontainer.v_id == variant_value:
                            res_subcontainer.append(subcontainer)
                        elif variant_value is None:
                            res_subcontainer.append(subcontainer)
                else:
                    res_subcontainer.extend(list_subcontainer)
    return res_subcontainer


def get_parentContainer(fatherUuid):
    from .parse_file import uuid_elements
    return uuid_elements.get(fatherUuid, None)


def get_wholeIndex(container, variant_value=None):
    from .parse_file import def_elements
    def_container_list = def_elements.get(container.ref_definition_)
    if variant_value is None:
        list_same_def = def_container_list
    else:
        list_same_def = [def_container for def_container in def_container_list if not def_container.v_id == -1 if def_container.v_id == variant_value]
    index = list_same_def.index(container)
    return index
