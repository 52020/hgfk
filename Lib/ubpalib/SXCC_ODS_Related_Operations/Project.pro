{
    "GlobalVar": [
    ],
    "OpenFlow": "[\n    {\n        \"current-tab\": \"true\",\n        \"seq\": \"Main\",\n        \"tag\": \"20240419095823361156\",\n        \"title\": \"Main\",\n        \"type\": \"bp\"\n    }\n]\n",
    "ProInfo": {
        "ProAbsolutePath": "C:/ISRPA/PICC_Custom_Components/SXCC_ODS_Related_Operations",
        "ProChange": "2024/12/30 16:21:39",
        "ProCreate": "2024/04/19 09:58:23",
        "ProDesc": "ODS系统相关操作（谷歌浏览器）\n（SXCC_ODS_Related_Operations）\n1.初始化",
        "ProDocVersion": "1.0.0.4",
        "ProImports": "",
        "ProInstallDate": "2025.12.11",
        "ProIsAdminRun": "0",
        "ProName": "SXCC_ODS_Related_Operations",
        "ProStudio": "2023.1.0.79",
        "ProTag": "20240419095823335154",
        "ProUserID": "F20390F061706B0DFE7B406FF8BC260C",
        "ProUserName": "Administrator",
        "ProVersion": "1.0.0.3",
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
            "sdc": "ODS系统自动登录（谷歌浏览器）\n（SXCC_ODS_Automatic_Login）\n1.修改ODS系统网址\n2.修改组件网址通配",
            "seq": "SXCC_ODS_Automatic_Login",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "2024041914214610093",
            "spr": [
                {
                    "vardef": "r\"D:\\Chrome_86_odsportal\\GoogleChromePortable.exe\"",
                    "vardesc": "ODS系统专用谷歌浏览器绝对路径",
                    "varname": "Str_ODS_Google_Chrome_Path",
                    "vartag": "2024041914214612794",
                    "vartype": ""
                },
                {
                    "vardef": "\"\"",
                    "vardesc": "ODS系统账号",
                    "varname": "Str_ODS_User",
                    "vartag": "2024041914214614395",
                    "vartype": ""
                },
                {
                    "vardef": "\"\"",
                    "vardesc": "ODS系统密码",
                    "varname": "Str_ODS_Password",
                    "vartag": "2024041914214615796",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "2024041914214617397",
                    "vartype": ""
                }
            ],
            "spv": [
                {
                    "vardef": "",
                    "vardesc": "集团OCR通用识别api_url",
                    "varname": "Str_OCR_APP_URL",
                    "vartag": "2024041914214619198",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "集团OCR通用识别app_key",
                    "varname": "Str_OCR_APP_KEY",
                    "vartag": "2024041914214621099",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "集团OCR通用识别app_secret",
                    "varname": "Str_OCR_APP_SECRET",
                    "vartag": "20240419142146223100",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "循环次数",
                    "varname": "Int_Loop_Index_Number",
                    "vartag": "20240419142146237101",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "验证码元素截图的图片绝对路径",
                    "varname": "Str_Image_Path",
                    "vartag": "20240419142146252102",
                    "vartype": "EIT_ProVar_Var"
                },
                {
                    "vardef": "",
                    "vardesc": "验证码文本",
                    "varname": "Str_Identifying_Code_Text",
                    "vartag": "20240419142146268103",
                    "vartype": "EIT_ProVar_Var"
                }
            ]
        },
        {
            "sdc": "ODS系统报表搜索进入相关页面（谷歌浏览器，报表平台）\n（SXCC_ODS_Report_Search）\n1.修改查询后等待时间",
            "seq": "SXCC_ODS_Report_Search",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419142243551256",
            "spr": [
                {
                    "vardef": "\"分年期首年期交保费收入表(new)\"",
                    "vardesc": "报表名称",
                    "varname": "Str_Report_Name",
                    "vartag": "20240419142736551573",
                    "vartype": ""
                },
                {
                    "vardef": "\"是\"",
                    "vardesc": "是否需要弹窗提示",
                    "varname": "Str_Pop_Up_Prompt",
                    "vartag": "20240419142243686260",
                    "vartype": ""
                }
            ],
            "spv": [
            ]
        },
        {
            "sdc": "ODS系统文件下载设置保存到指定路径（谷歌浏览器，报表平台）\n（SXCC_ODS_File_Download）\n1.初始化",
            "seq": "SXCC_ODS_File_Download",
            "seqptag": "",
            "seqret": "1",
            "seqtag": "20240419144437992797",
            "spr": [
                {
                    "vardef": "r\"C:\\Users\\Administrator\\新建文件夹\\C.xlsx\"",
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
