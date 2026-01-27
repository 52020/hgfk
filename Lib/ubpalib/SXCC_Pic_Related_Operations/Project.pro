{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"Main\",\n        \"tag\": \"202404191535404382300\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_Pic_Related_Operations",
        "ProChange": "2024/07/29 17:13:13",
        "ProCreate": "2024/04/19 15:35:40",
        "ProDesc": "图片相关操作\n（SXCC_Pic_Related_Operations）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_Pic_Related_Operations",
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
            "sdc": "剪切图片\n（SXCC_Cut_Pic）\n1.初始化",
            "seq": "SXCC_Cut_Pic",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "202404191537292582329",
            "spr": [
                {
                    "vardef": "",
                    "vardesc": "输入图片（源图片）绝对路径",
                    "varname": "Str_Input_Pic_Path",
                    "vartag": "202404191537293392330",
                    "vartype": ""
                },
                {
                    "vardef": "0",
                    "vardesc": "输入左角坐标",
                    "varname": "Int_Input_Left",
                    "vartag": "202404191554527942691",
                    "vartype": ""
                },
                {
                    "vardef": "0",
                    "vardesc": "输入上角坐标",
                    "varname": "Int_Input_Upper",
                    "vartag": "20240729161722128341",
                    "vartype": ""
                },
                {
                    "vardef": "10",
                    "vardesc": "输入右角坐标",
                    "varname": "Int_Input_Right",
                    "vartag": "202404191555030952692",
                    "vartype": ""
                },
                {
                    "vardef": "10",
                    "vardesc": "输入下角坐标",
                    "varname": "Int_Input_Lower",
                    "vartag": "20240729162044692407",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输出图片（目标图片）绝对路径",
                    "varname": "Str_Output_Pic_Path",
                    "vartag": "202404191554428372690",
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
                    "vardef": "\"剪切图片\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "202404191627128842978",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "多张图片横向拼接（有间隔）\n（SXCC_Splicing_Pic_Transverse）\n1.初始化",
            "seq": "SXCC_Splicing_Pic_Transverse",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240729165919171811",
            "spr": [
                {
                    "vardef": "[]",
                    "vardesc": "输入图片（源图片）绝对路径列表",
                    "varname": "List_Input_Pic_Path",
                    "vartag": "20240729165919224813",
                    "vartype": ""
                },
                {
                    "vardef": "5",
                    "vardesc": "输入像素间隔",
                    "varname": "Int_Input_Pixel_Spacing",
                    "vartag": "20240729165919247814",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输出图片（目标图片）绝对路径",
                    "varname": "Str_Output_Pic_Path",
                    "vartag": "20240729165919301817",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240729165919316818",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"多张图片横向拼接（有间隔）\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240729165919333819",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "多张图片纵向拼接（有间隔）\n（SXCC_Splicing_Pic_Portrait）\n1.初始化",
            "seq": "SXCC_Splicing_Pic_Portrait",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240729170743829945",
            "spr": [
                {
                    "vardef": "[]",
                    "vardesc": "输入图片（源图片）绝对路径列表",
                    "varname": "List_Input_Pic_Path",
                    "vartag": "20240729170743856946",
                    "vartype": ""
                },
                {
                    "vardef": "5",
                    "vardesc": "输入像素间隔",
                    "varname": "Int_Input_Pixel_Spacing",
                    "vartag": "20240729170743875947",
                    "vartype": ""
                },
                {
                    "vardef": "",
                    "vardesc": "输出图片（目标图片）绝对路径",
                    "varname": "Str_Output_Pic_Path",
                    "vartag": "20240729170743890948",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240729170743905949",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "\"多张图片纵向拼接（有间隔）\"",
                    "vardesc": "流程名称",
                    "varname": "Str_Process_Name",
                    "vartag": "20240729170743919950",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        }
    ]
}
