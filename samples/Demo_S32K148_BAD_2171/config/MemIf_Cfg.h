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
 * @file        : MemIf_Cfg.h
 * @licence     : 
 * @date        : 2026-04-27 13:21:42
 * @customer    : iSoft
 * @description : Pre-compile time definitions of MemIf
 * @generator   : AUTOSAR classic Platform R23-11
 * @toolVersion : for EasyXMen V25.10
 **********************************************************************************************************************/

#ifndef MEMIF_CFG_H
#define MEMIF_CFG_H

/* =================================================== inclusions =================================================== */
#include "MemIf_Types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* ===================================================== macros ===================================================== */
/* PRQA S 5004 ++ */ /* VL_MemIf_5004 */
/** Switches the development error detection and notification on or off.
 * True: detection and notification is enabled.
 * False (Default): detection and notification is disabled. */
/** MemIf/MemIfGeneral/MemIfDevErrorDetect */
#define MEMIF_DEV_ERROR_DETECT STD_OFF

/** Concrete number of underlying memory abstraction modules.
 * Calculation Formula: Count number of configured EA and FEE modules. */
/** MemIf/MemIfGeneral/MemIfNumberOfDevices */
#define MEMIF_NUMBER_OF_DEVICES 2u

/** Pre-processor switch to enable / disable the API to read out the modules version information.
 * True: Version info API enabled.
 * False (Default):  Version info API disabled. */
/** MemIf/MemIfGeneral/MemIfVersionInfoApi */
#define MEMIF_VERSION_INFO_API STD_OFF

/** Module version string (vendor probe param). */
/** MemIf/MemIfGeneral/MemIfModuleVersion */
#define MEMIF_MODULE_VERSION "TEST_PROBE_42_V25_10"

/**
 * @brief Read function pointer type for MemHwA API services
 */
typedef Std_ReturnType (
    *MemIf_ReadFPtrType)(uint16 BlockNumber, uint16 BlockOffset, uint8* DataBufferPtr, uint16 Length);
/**
 * @brief Write function pointer type for MemHwA API services
 */
typedef Std_ReturnType (*MemIf_WriteFPtrType)(uint16 BlockNumber, uint8 const* DataBufferPtr);
/**
 * @brief EraseImmediateBlock function pointer type for MemHwA API services
 */
typedef Std_ReturnType (*MemIf_EraseImmediateBlockFPtrType)(uint16 BlockNumber);
/**
 * @brief InvalidateBlock function pointer type for MemHwA API services
 */
typedef Std_ReturnType (*MemIf_InvalidateBlockFPtrType)(uint16 BlockNumber);
/**
 * @brief Cancel function pointer type for MemHwA API services
 */
typedef void (*MemIf_CancelFPtrType)(void);
/**
 * @brief GetStatus function pointer type for MemHwA API services
 */
typedef MemIf_StatusType (*MemIf_GetStatusFPtrType)(void);
/**
 * @brief GetJobResult function pointer type for MemHwA API services
 */
typedef MemIf_JobResultType (*MemIf_GetJobResultFPtrType)(void);

/**
 * @brief configuration structure for MemHwA API services
 */
typedef struct
{
    MemIf_ReadFPtrType Read;
    MemIf_WriteFPtrType Write;
    MemIf_EraseImmediateBlockFPtrType EraseImmediateBlock;
    MemIf_InvalidateBlockFPtrType InvalidateBlock;
    MemIf_CancelFPtrType Cancel;
    MemIf_GetStatusFPtrType GetStatus;
    MemIf_GetJobResultFPtrType GetJobResult;
} MemIf_MemFPtrType;

/* =========================================== external data declarations =========================================== */
extern const MemIf_MemFPtrType MemIf_MemFPtr[MEMIF_NUMBER_OF_DEVICES];

/* Macro mappings of driver API calls */
/**
 * @brief       Invokes the "Read" function of the underlying memory abstraction module selected by the parameter
 *              DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @param[in]   BlockNumber: number of logic block
 * @param[in]   BlockOffset: Read address offset inside the block
 * @param[in]   Length: Number of bytes to read
 * @param[out]  DataBufferPtr: Pointer to data buffer
 * @return      Std_ReturnType
 * @retval      E_OK    : The requested job has been accepted by the module
 * @retval      E_NOT_OK: The requested job has not been accepted by the module.
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61233
 */
#define MemIf_Read(DeviceIndex, BlockNumber, BlockOffset, DataBufferPtr, Length) MemIf_MemFPtr[DeviceIndex].Read(BlockNumber, BlockOffset, DataBufferPtr, Length)

/**
 * @brief       Invokes the "Write" function of the underlying memory abstraction module selected by the parameter
 *              DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @param[in]   BlockNumber: number of logic block
 * @param[in]   DataBufferPtr: Pointer to data buffer
 * @return      Std_ReturnType
 * @retval      E_OK    : The requested job has been accepted by the module
 * @retval      E_NOT_OK: The requested job has not been accepted by the module.
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61232
 */
#define MemIf_Write(DeviceIndex, BlockNumber, DataBufferPtr) MemIf_MemFPtr[DeviceIndex].Write(BlockNumber, DataBufferPtr)

/**
 * @brief       Invokes the "EraseImmediateBlock" function of the underlying memory abstraction module selected by the
 *              parameter DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @param[in]   BlockNumber: number of logic block
 * @return      Std_ReturnType
 * @retval      E_OK    : The requested job has been accepted by the module
 * @retval      E_NOT_OK: The requested job has not been accepted by the module.
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61226
 */
#define MemIf_EraseImmediateBlock(DeviceIndex, BlockNumber) MemIf_MemFPtr[DeviceIndex].EraseImmediateBlock(BlockNumber)

/**
 * @brief       Invokes the "InvalidateBlock" function of the underlying memory abstraction module selected by the
 *              parameter DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @param[in]   BlockNumber: number of logic block
 * @return      Std_ReturnType
 * @retval      E_OK    : The requested job has been accepted by the module
 * @retval      E_NOT_OK: The requested job has not been accepted by the module.
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61228
 */
#define MemIf_InvalidateBlock(DeviceIndex, BlockNumber) MemIf_MemFPtr[DeviceIndex].InvalidateBlock(BlockNumber)

/**
 * @brief       Invokes the "GetJobResult" function of the underlying memory abstraction module selected by the
 *              parameter DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @return      MemIf_StatusType
 * @retval      MEMIF_JOB_OK: The job has been finished successfully
 * @retval      MEMIF_JOB_FAILED: The job has not been finished successfully
 * @retval      MEMIF_JOB_PENDING: The job has not yet been finished.
 * @retval      MEMIF_JOB_CANCELED: The job has been canceled.
 * @retval      MEMIF_BLOCK_INCONSISTENT: 1. The requested block is inconsistent, it may contain corrupted data.
 *                                        2. Block is NOT found.
 * @retval      MEMIF_BLOCK_INVALID: The requested block has been marked as invalid, the requested operation can not be
 *                                   performed.
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61229
 */
#define MemIf_GetJobResult(DeviceIndex) MemIf_MemFPtr[DeviceIndex].GetJobResult()

/**
 * @brief       Invokes the "Cancel" function of the underlying memory abstraction module selected by the parameter
 *              DeviceIndex.
 * @param[in]   DeviceIndex: index number of device
 * @reentrant   Non Reentrant
 * @synchronous Synchronous
 * @trace       CPD-61231
 */
#define MemIf_Cancel(DeviceIndex) MemIf_MemFPtr[DeviceIndex].Cancel()
/* PRQA S 5004 -- */

#ifdef __cplusplus
}
#endif
#endif
