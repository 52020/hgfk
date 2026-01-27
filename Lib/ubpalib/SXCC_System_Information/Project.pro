{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"20240419161153493310\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"SXCC_System_Information\",\n        \"tag\": \"20240419161323539335\",\n        \"title\": \"SXCC_System_Information\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_System_Information",
        "ProChange": "2024/04/24 17:01:28",
        "ProCreate": "2024/04/19 16:11:53",
        "ProDesc": "获取操作系统信息\n（SXCC_System_Information）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_System_Information",
        "ProStudio": "2023.1.0.79",
        "ProTag": "20240419161153467308",
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
            "seqtag": "20240419161153493310",
            "spr": [
            ],
            "spv": [
            ]
        },
        {
            "sdc": "获取操作系统信息\n（SXCC_System_Information）\n1.初始化",
            "seq": "SXCC_System_Information",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419161323539335",
            "spr": [
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
                    "vardef": "\"获取操作系统信息\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240423162306335186",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "{}",
                    "vardesc": "操作系统信息字典",
                    "varname": "Dict_System_Information",
                    "vartag": "20240419162857871492",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
