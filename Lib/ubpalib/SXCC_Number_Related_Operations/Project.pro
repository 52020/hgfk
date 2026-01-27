{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"202404191535404382300\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"SXCC_Number_To_Letter\",\n        \"tag\": \"202404191537292582329\",\n        \"title\": \"SXCC_Number_To_Letter\",\n        \"type\": \"bp\"\n    },\n    {\n        \"seq\": \"SXCC_Number_To_Chine_Uppercase\",\n        \"tag\": \"20240419163620802186\",\n        \"title\": \"SXCC_Number_To_Chine_Uppercase\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_Number_Related_Operations",
        "ProChange": "2024/04/24 16:59:25",
        "ProCreate": "2024/04/19 15:35:40",
        "ProDesc": "数字相关操作\n（SXCC_Number_Related_Operations）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_Number_Related_Operations",
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
            "sdc": "把数字转换成对应的字母\n（SXCC_Number_To_Letter）\n1.初始化",
            "seq": "SXCC_Number_To_Letter",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202404191537292582329",
            "spr": [
                {
                    "vardef": "3",
                    "vardesc": "数字",
                    "varname": "Int_Number",
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
                    "vardef": "\"把数字转换成对应的字母\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "2024041916241819788",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "\"\"",
                    "vardesc": "字母",
                    "varname": "Str_Letter",
                    "vartag": "20240419163453452172",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "把数字转换成中文大写\n（SXCC_Number_To_Chine_Uppercase）\n1.初始化",
            "seq": "SXCC_Number_To_Chine_Uppercase",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419163620802186",
            "spr": [
                {
                    "vardef": "3",
                    "vardesc": "数字",
                    "varname": "Int_Number",
                    "vartag": "20240419163620873187",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240419163620888188",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"把数字转换成中文大写\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240419163620903189",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "\"\"",
                    "vardesc": "中文大写",
                    "varname": "Str_Chinese_Uppercase",
                    "vartag": "20240419163620920190",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
