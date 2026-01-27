{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"Main\",\n        \"tag\": \"202302271636172632\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/MysqlInsert_Production",
        "ProChange": "2024/08/30 14:50:09",
        "ProCreate": "2023/02/27 16:36:17",
        "ProDesc": "效率统计组件（生产环境）",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "1",
        "ProName": "MysqlInsert_Production",
        "ProStudio": "2023.1.0.79",
        "ProTag": "202302271636172591",
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
            "sdc": "MysqlInsert_Production-组件-v3.0：\n参数statusFlg  类型int（0：流程开始，1：流程结束）\n\n",
            "seq": "Main",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202302271636172632",
            "spr": [
                {
                    "vardef": "",
                    "vardesc": "状态描述0：开始，1：结束",
                    "varname": "statusFlg",
                    "vartag": "20230627170104928467",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "流程名称",
                    "varname": "processName",
                    "vartag": "20230627170812497480",
                    "vartype": ""
                },
                {
                    "vardef": "{}",
                    "vardesc": "可选参数字典",
                    "varname": "shoudDict",
                    "vartag": "20230627171642399487",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "省分部门名称/部门名称",
                    "varname": "departmentName",
                    "vartag": "20230630163426589260",
                    "vartype": ""
                },
                {
                    "vardef": "1",
                    "vardesc": "运行次数",
                    "varname": "runCount",
                    "vartag": "202308150901179944",
                    "vartype": ""
                }
            ],
            "spv": [
            ]
        },
        {
            "sdc": "MysqlInsert_Production-组件-v3.0：\n参数statusFlg  类型int（0：流程开始，1：流程结束）\n\n",
            "seq": "MysqlInsert_Production",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202407301102120225",
            "spr": [
                {
                    "vardef": "",
                    "vardesc": "状态描述0：开始，1：结束",
                    "varname": "statusFlg",
                    "vartag": "202407301102120566",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "流程名称",
                    "varname": "processName",
                    "vartag": "202407301102120637",
                    "vartype": ""
                },
                {
                    "vardef": "{}",
                    "vardesc": "可选参数字典",
                    "varname": "shoudDict",
                    "vartag": "202407301102120708",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "省分部门名称/部门名称",
                    "varname": "departmentName",
                    "vartag": "202407301102120789",
                    "vartype": ""
                },
                {
                    "vardef": "1",
                    "vardesc": "运行次数",
                    "varname": "runCount",
                    "vartag": "2024073011021208610",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "{}",
                    "vardesc": "",
                    "varname": "dataDcit",
                    "vartag": "2024073011021209211",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "",
                    "varname": "mysqlObj",
                    "vartag": "2024073011021210112",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
