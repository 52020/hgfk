{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"20240419161153493310\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"seq\": \"One_List_Deduplication\",\n        \"tag\": \"20240419161323539335\",\n        \"title\": \"One_List_Deduplication\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"Two_List_Deduplication\",\n        \"tag\": \"20240531092500401120\",\n        \"title\": \"Two_List_Deduplication\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_List_Related_Operations",
        "ProChange": "2024/06/14 09:27:38",
        "ProCreate": "2024/04/19 16:11:53",
        "ProDesc": "列表相关操作\n（SXCC_List_Related_Operations）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_List_Related_Operations",
        "ProStudio": "2023.1.0.79",
        "ProTag": "20240419161153467308",
        "ProUserID": "F20390F061706B0DFE7B406FF8BC260C",
        "ProUserName": "Administrator",
        "ProVersion": "1.0.0.1",
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
            "seqtag": "20240419161153493310",
            "spr": [
            ],
            "spv": [
            ]
        },
        {
            "sdc": "一维列表去重\n（One_List_Deduplication）\n1.初始化",
            "seq": "One_List_Deduplication",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419161323539335",
            "spr": [
                {
                    "vardef": "[\"Q\",\"W\",\"Q\"]",
                    "vardesc": "一维列表（输入）",
                    "varname": "List_Input_One_Data",
                    "vartag": "20240419161323610336",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240419161323652338",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"一维列表去重\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240419162857871492",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "[]",
                    "vardesc": "一维列表（输出）",
                    "varname": "List_Output_One_Data",
                    "vartag": "2024042316431359089",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "二维列表去重\n（One_List_Deduplication）\n1.修改去重方式",
            "seq": "Two_List_Deduplication",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240531092500401120",
            "spr": [
                {
                    "vardef": "[[1, 2], [3, 4], [1, 2], [5, 6]]",
                    "vardesc": "二维列表（输入）",
                    "varname": "List_Input_Two_Data",
                    "vartag": "20240531092500463121",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240531092500478122",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"二维列表去重\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240531092500491123",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "[]",
                    "vardesc": "二维列表（输出）",
                    "varname": "List_Output_Two_Data",
                    "vartag": "20240531092500503124",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
