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
 * @file        : NvM_Lcfg.h
 * @licence     : 
 * @date        : 2026-05-04 00:09:17
 * @customer    : iSoft
 * @description : Link time declaration of NvM
 * @generator   : AUTOSAR classic Platform R23-11
 * @toolVersion : for EasyXMen V25.10
 **********************************************************************************************************************/
#ifndef NVM_LCFG_H
#define NVM_LCFG_H

/* =================================================== inclusions =================================================== */
#include "Std_Types.h"
#include "NvM_Cfg.h"
#include "NvM_Types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =============================================== version information ============================================== */

/* ===================================================== macros ===================================================== */
/** Defines used as parameters for the MemIf job buffer */
#define NVM_MEMIF_JOB_MAX_NUM           6U
#define NVM_MEMIF_CLASS1_AND_CLASS2_NUM 3U

/** Defines used as parameters for priority table queue */
#define NVM_PRI_TAB_MAX_NUM 2U

/* ================================================ type definitions ================================================ */

/**
 * @brief     NvM module block Descriptor type
 */
typedef struct
{
    uint8 NvmNvramDeviceId;                         /** Device ID for layer module */
    NvM_BlockManagementType NvmBlockManagementType; /** Block management type */
    uint8 NvmNvBlockNum;              /** Nv block number */
    uint8 NvmRomBlockNum;             /** Rom blcok number */
    uint8 NvMMaxNumOfReadRetries;     /** Max number of read retries */
    uint8 NvMMaxNumOfWriteRetries;    /** Max number of write retries */
    NvM_BlockCRCType NvmBlockCRCType; /** Type of used crc */
    /**
     * Bit 0:NvmWriteBlockOnce
     * Bit 1:NvmBlockWriteProt
     * Bit 2:NvmCalcRamBlockCrc
     * Bit 3:NvmResistantToChangedSw
     * Bit 4:NvmSelectBlockForReadall
     * Bit 5:NvmSelectBlockForWriteall
     * Bit 6:NvMStaticBlockIDCheck
     * Bit 7:NvMWriteVerification
     * Bit 8:NvMBlockUseAutoValidation
     * Bit 9:NvMBlockUseCRCCompMechanism
     * Bit 10:NvMBlockUseSetRamBlockStatus
     * Bit 11:NvMBlockUseSyncMechanism
     * Bit 12:NvMBswMBlockStatusInformation
     */
    uint16 FlagGroup;                    /** Administrative block flag */
    uint16 NvmNvBlockBaseNumber;         /** Base number value */
    uint16 NvmNvBlockLength;             /** Nv block length */
    uint16 NvMWriteVerificationDataSize; /** Max number of write verification */
    NvM_BlockIdType RepairIndex; /** Index of repair buffer */
    /* PRQA S 3432++ */ /* VL_NvM_3432 */
    uint32* NvmBlockCrcBuffAddress; /** Crc buffer address */
    uint8* NvmRamBlockDataAddress; /** Ram buffer address */
    uint8* NvmRomBlockDataAddress; /** Rom buffer address */
    /* PRQA S 3432-- */
    /** Initial callback function pointer */
    NvM_InitBlockCallbackType NvmInitBlockCallback;
    /** Single block callback function pointer */
    NvM_SingleBlockCallbackType NvmSingleBlockCallback;
    /** Read callback function pointer address to copy ram to ram mirror */
    NvM_ReadRamBlockFromNvmCallbackType NvM_ReadRamBlockFromNvm;
    /** Write callback function pointer address to copy ram to ram mirror */
    NvM_WriteRamBlockToNvmCallbackType NvM_WriteRamBlockToNvm;
} NvM_BlockDescriptorType;

/**
 * @brief     NvM module config type
 */
typedef struct
{
    uint8 idle; /* not used */
} NvM_ConfigType;

/* ========================================== internal function definitions ========================================= */

/* =========================================== external data declarations =========================================== */
/**
 * @brief Buffer of RAM block @range NA
 */
/* PRQA S 3132 ++ */ /* VL_QAC_MagicNum */
extern uint8 NvMBlockRamBuffer1[2];
extern uint8 NvMBlockRamBuffer2[1];
extern uint8 NvMBlockRamBuffer3[1];
extern uint8 NvMBlockRamBuffer4[17];
extern uint8 NvMBlockRamBuffer5[4];

extern uint32 NvMCrcBuf_NvMBlock_ConfigID[1];
extern uint32 NvMCrcBuf_NvMBlock_SecurityLevel01[1];
extern uint32 NvMCrcBuf_NvMBlock_SecurityLevel02[1];
extern uint32 NvMCrcBuf_NvMBlock_DIDF190[1];
extern uint32 NvMCrcBuf_NvMBlock_DIDF183[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_0[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_1[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_2[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_3[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_4[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_5[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_6[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_7[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_8[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_9[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_10[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_11[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_12[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_13[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_14[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_15[1];
extern uint32 NvMCrcBuf_NvMBlock_Primary_16[1];
extern uint32 NvMCrcBuf_NvMBlock_AdminData[1];
extern uint32 NvMCrcBuf_NvMBlock_EventStatusData[1];
/* PRQA S 3132 -- */

/* ========================================= external function declarations ========================================= */

#ifdef __cplusplus
}
#endif
#endif

