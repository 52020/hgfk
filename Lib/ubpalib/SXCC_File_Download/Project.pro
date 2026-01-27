{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\",\n        \"tag\": \"20240419095823361156\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    },\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"SXCC_File_Download\",\n        \"tag\": \"20240419144437992797\",\n        \"title\": \"SXCC_File_Download\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components-自定义组件/SXCC_File_Download",
        "ProChange": "2025/06/06 16:02:55",
        "ProCreate": "2024/04/19 09:58:23",
        "ProDesc": "文件下载设置保存到指定绝对路径\n（SXCC_File_Download）\n1.添加动态加载另存为窗口功能",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_File_Download",
        "ProStudio": "2023.1.0.79",
        "ProTag": "20240419095823335154",
        "ProUserID": "F20390F061706B0DFE7B406FF8BC260C",
        "ProUserName": "Administrator",
        "ProVersion": "1.0.0.2",
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
            "seqtag": "20240419095823361156",
            "spr": [
            ],
            "spv": [
            ]
        },
        {
            "sdc": "文件下载设置保存到指定绝对路径\n（SXCC_File_Download）\n1.添加动态加载另存为窗口功能",
            "seq": "SXCC_File_Download",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419144437992797",
            "spr": [
                {
                    "vardef": "r\"C:\\Users\\Administrator\\新建文件夹\\文件下载测试.xlsx\"",
                    "vardesc": "文件绝对路径",
                    "varname": "Str_File_Path",
                    "vartag": "20240419144438017798",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240419144438033799",
                    "vartype": ""
                }
            ],
            "spv": [
            ]
        }
    ]
}
