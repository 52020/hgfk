{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"20240419161153493310\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"SXCC_Folder_To_File_Path_List\",\n        \"tag\": \"20240419161323539335\",\n        \"title\": \"SXCC_Folder_To_File_Path_List\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_Folder_To_File_Path_List",
        "ProChange": "2024/04/25 10:55:21",
        "ProCreate": "2024/04/19 16:11:53",
        "ProDesc": "获取文件夹中的文件绝对路径列表\n（SXCC_Folder_To_File_Path_List）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_Folder_To_File_Path_List",
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
            "sdc": "获取文件夹中的文件绝对路径列表\n（SXCC_Folder_To_File_Path_List）\n1.初始化",
            "seq": "SXCC_Folder_To_File_Path_List",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419161323539335",
            "spr": [
                {
                    "vardef": "r\"C:\\Users\\Administrator\\新建文件夹\"",
                    "vardesc": "文件夹绝对路径",
                    "varname": "Str_Folder_Path",
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
                    "vardef": "\"获取文件夹中的文件绝对路径列表\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240419162857871492",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "[]",
                    "vardesc": "文件绝对路径列表",
                    "varname": "List_File_Path",
                    "vartag": "2024042316431359089",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
