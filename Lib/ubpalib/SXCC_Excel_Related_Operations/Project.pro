{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"202404191535404382300\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"seq\": \"SXCC_Excel_2_Sheet_Copy_Paste\",\n        \"tag\": \"202404191537292582329\",\n        \"title\": \"SXCC_Excel_2_Sheet_Copy_Paste\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"SXCC_Excel_To_PDF\",\n        \"tag\": \"202404191602121012739\",\n        \"title\": \"SXCC_Excel_To_PDF\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_Excel_Related_Operations",
        "ProChange": "2024/04/24 16:52:09",
        "ProCreate": "2024/04/19 15:35:40",
        "ProDesc": "Excel相关操作\n（SXCC_Excel_Related_Operations）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_Excel_Related_Operations",
        "ProStudio": "2023.1.0.79",
        "ProTag": "202404191535403992298",
        "ProUserID": "F20390F061706B0DFE7B406FF8BC260C",
        "ProUserName": "Administrator",
        "ProVersion": "1.0.0.0",
        "ToPath": "Server",
        "operatingSystem": 0,
        "releaseUserName": "ysq_zhangzhen"
    },
    "SeqGroupList": [
    ],
    "SeqPythonModuleList": [
    ],
    "SeqTextFileList": [
    ],
    "SequenceList": [
        {
            "sdc": "",
            "seq": "Main",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202404191535404382300",
            "spr": [
            ],
            "spv": [
            ]
        },
        {
            "sdc": "Excel中两个Sheet页全部复制粘贴\n（SXCC_Excel_2_Sheet_Copy_Paste）\n1.初始化",
            "seq": "SXCC_Excel_2_Sheet_Copy_Paste",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202404191537292582329",
            "spr": [
                {
                    "vardef": "",
                    "vardesc": "输入Excel表格（源表格）绝对路径",
                    "varname": "Str_Input_Excel_Path",
                    "vartag": "202404191537293392330",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输入Sheet名称（源Sheet名称）",
                    "varname": "Str_Input_Sheet_Name",
                    "vartag": "202404191554527942691",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输出Excel表格（目标表格）绝对路径",
                    "varname": "Str_Output_Excel_Path",
                    "vartag": "202404191554428372690",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输出Sheet名称（目标Sheet名称）",
                    "varname": "Str_Output_Sheet_Name",
                    "vartag": "202404191555030952692",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "202404191537293662331",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"Excel中两个Sheet页全部复制粘贴\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "202404191627128842978",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "Excel导出为PDF\n（SXCC_Excel_To_PDF）\n1.初始化",
            "seq": "SXCC_Excel_To_PDF",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202404191602121012739",
            "spr": [
                {
                    "vardef": "",
                    "vardesc": "Excel表格绝对路径",
                    "varname": "Str_Excel_Path",
                    "vartag": "202404191602121262740",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "PDF文件绝对路径",
                    "varname": "Str_PDF_Path",
                    "vartag": "202404191602121452741",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "202404191602122052744",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"Excel导出为PDF\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "202404191625081922962",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
