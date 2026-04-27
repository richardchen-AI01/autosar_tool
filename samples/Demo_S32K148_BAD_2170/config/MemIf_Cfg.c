/**
 * COPYRIGHT
 * ---------------------------------------------------------------------------------------------------------------------
 * Copyright (c) iSOFT INFRASTRUCTURE SOFTWARE CO., LTD. This software is proprietary to
 * iSOFT INFRASTRUCTURE SOFTWARE CO., LTD., and all rights are reserved by iSOFT INFRASTRUCTURE SOFTWARE CO., LTD.
 * Without the express written permission of the company, no organization or individual may copy, install, trial,
 * distribute, or reverse engineer this software. For terms of use and further details, please refer to the End User
 * License Agreement (EULA) or contact us business@i-soft.com.cn for more assistance.
 *
 * This file contains code from iSoft, which is licensed under the LGPL-2.1. However, due to a special exception,
 * you are not required to comply with the provisions of section 6a of LGPL-2.1. Specifically, you may distribute
 * your software, including this file, under terms of your choice, including proprietary licenses, without needing to
 * provide the source code or object code as specified in section 6a. For more details, please refer to the project's
 * LICENSE and EXCEPTION files and the specific exception statement.
 * ---------------------------------------------------------------------------------------------------------------------
 * FILE DESCRIPTION
 * ---------------------------------------------------------------------------------------------------------------------
 * @MCU         : S32K148
 * @file        : MemIf_Cfg.c
 * @licence     : 
 * @date        : 2026-04-27 13:21:42
 * @customer    : iSoft
 * @description : Pre-compile time definitions of MemIf
 * @generator   : AUTOSAR classic Platform R23-11
 * @toolVersion : for EasyXMen V25.10
 **********************************************************************************************************************/

/* =================================================== inclusions =================================================== */
#include "MemIf_Cfg.h"
#include "Fee.h"

/* ============================================ external data definitions =========================================== */
#define MEMIF_START_SEC_CONFIG_DATA_PTR
#include "MemIf_MemMap.h"
/* PRQA S 1531 ++ */ /* VL_MemIf_1531 */
const MemIf_MemFPtrType MemIf_MemFPtr[MEMIF_NUMBER_OF_DEVICES] =
{
	/*<MEMIF_FEE_API/>*/
	{
		/* Fee */
		Fee_Read,
		Fee_Write,
		Fee_EraseImmediateBlock,
		Fee_InvalidateBlock,
		Fee_Cancel,
		Fee_GetStatus,
		Fee_GetJobResult	
	},
};
/* PRQA S 1531 -- */
#define MEMIF_STOP_SEC_CONFIG_DATA_PTR
#include "MemIf_MemMap.h"
