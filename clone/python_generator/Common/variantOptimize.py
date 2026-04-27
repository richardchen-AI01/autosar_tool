# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\variantOptimize.py
import re, sys
from Common import logger
variant_format = "_VT_\\w+"
g_pattern_block = "(/\\*\\s*#\\s*" + variant_format + "\\s*start \\*/)([\\s\\S]*?)(\\s*/\\* #\\s*" + variant_format + "\\s*stop \\*/)"
g_pattern_variant_identiffier = "/\\*\\s*#\\s*" + variant_format + ".*\\*/"
g_pattern_variable = "(\\w+_VT_\\w+).*="
g_pattern_macro = "#define (\\w+_VT_\\w+) \\w+"
g_pattern_extern = "extern\\s+const\\s+\\w+ConfigType\\s+(\\w+_Config_\\w+);"
g_variant_mappings = {}

def pbs_get_matche_objs(content, pattern):
    unique_matches = {}
    unique_results = []
    variant_mappings = {}
    matches = list(re.finditer(pattern, content, flags=(re.M | re.I | re.S)))
    for match in matches:
        matched_string = match.group(2)
        symbol_with_variant = re.search(g_pattern_variable, matched_string)
        if not symbol_with_variant:
            symbol_with_variant = re.search(g_pattern_macro, matched_string)
        symbol = symbol_with_variant.group(1)
        content_with_no_variant = matched_string.replace(symbol, "")
        if content_with_no_variant not in unique_matches:
            unique_matches[content_with_no_variant] = symbol
            unique_results.append(match)
        else:
            variant_mappings[symbol] = unique_matches[content_with_no_variant]
    else:
        return (
         matches, unique_results, variant_mappings)


def pbs_update_files(matches, unique_matches, variant_mappings, pattern, content):
    original_length = len(matches)
    current_length = len(unique_matches)

    def replace_with_unique_variant_body(counter):

        def inner(_):
            if counter[0] < len(unique_matches) and unique_matches[counter[0]] is not None:
                result = unique_matches[counter[0]].group(0)
            else:
                result = ""
            counter[0] += 1
            return result

        return inner

    if current_length < original_length:
        empty_match = None
        unique_matches.extend([empty_match] * (original_length - current_length))
    else:
        return
        if matches:
            counter = [
             0]
            updated_content = re.sub(pattern, (replace_with_unique_variant_body(counter)), content, flags=(re.M | re.I | re.S))
            for item in variant_mappings:
                updated_content = updated_content.replace(item, variant_mappings[item])
            else:
                return updated_content

        return


def pbs_config_collector(map):
    global g_variant_mappings
    for key, value in map.items():
        if "_Config_" in key:
            g_variant_mappings[key] = value


def pbs_process_pbcfg_c(content, file):
    matches, unique_matches, variant_mappings = pbs_get_matche_objs(content, g_pattern_block)
    content_with_no_vaiant_identifier = content
    pbs_config_collector(variant_mappings)
    updated_content = None
    while variant_mappings:
        updated_content = pbs_update_files(matches, unique_matches, variant_mappings, g_pattern_block, content)
        matches, unique_matches, variant_mappings = pbs_get_matche_objs(updated_content, g_pattern_block)
        pbs_config_collector(variant_mappings)

    if updated_content is not None:
        content_with_no_vaiant_identifier = re.sub(g_pattern_variant_identiffier, "", updated_content, flags=(re.M | re.I))
        logger.info(f"已更新文件: {file}")
    else:
        logger.info(f"未找到匹配项，未更新文件: {file}")
    return content_with_no_vaiant_identifier


def pbs_process_pbcfg_h(content, file):

    def replace_match(match):
        if match.group(1) in g_variant_mappings:
            content_new = g_variant_mappings[match.group(1)]
            del g_variant_mappings[match.group(1)]
            return "#define {} {}".format(match.group(1), content_new)
        return match.group(0)

    modified_content = re.sub(g_pattern_extern, replace_match, content)
    return modified_content


def pbs_pbcfg_file_optimize(content, file_path):
    if file_path.endswith(".c"):
        updated_content = pbs_process_pbcfg_c(content, file_path)
    else:
        updated_content = pbs_process_pbcfg_h(content, file_path)
    return updated_content


def scanTxt(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"文件 {file} 未找到。")
        sys.exit(-1)
    except Exception as e:
        try:
            print(f"发生错误: {e}")
            sys.exit(-1)
        finally:
            e = None
            del e

    else:
        return content


def writeTxt(file, str):
    f = open(file, "w", encoding="utf-8")
    f.write(str)
    f.close()


def testVariant():
    g_c_file_path = "D:\\workspace\\r23_bsw\\config\\Com_PBCfg.c"
    g_h_file_path = "D:\\workspace\\r23_bsw\\config\\Com_PBCfg.h"
    content = scanTxt(g_c_file_path)
    content = pbs_pbcfg_file_optimize(content, g_c_file_path)
    writeTxt(g_c_file_path, content)
    content = scanTxt(g_h_file_path)
    content = pbs_pbcfg_file_optimize(content, g_h_file_path)
    writeTxt(g_h_file_path, content)
