# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Copyright 2021 ZhangT. All Rights Reserved.
# Author: yuandiaodiaodiao
# Author: zhangt2333
# spider.py 2021/5/25 0:25

import json

import requests

BUILDINGS = eval("""
[
    {
        "buildingid": "1503975980",
        "building": "凤凰居6号楼"
    },
    {
        "buildingid": "1661835273",
        "building": "B5号楼"
    },
    {
        "buildingid": "1661835256",
        "building": "B2"
    },
    {
        "buildingid": "1574231830",
        "building": "T1"
    },
    {
        "buildingid": "1503975832",
        "building": "凤凰居1号楼"
    },
    {
        "buildingid": "1503975832",
        "building": "S1一多书院"
    },
    {
        "buildingid": "1599193777",
        "building": "S11"
    },
    {
        "buildingid": "1693031698",
        "building": "B9"
    },
    {
        "buildingid": "1503976004",
        "building": "凤凰居9号楼"
    },
    {
        "buildingid": "1503975890",
        "building": "凤凰居2号楼"
    },
    {
        "buildingid": "1503975967",
        "building": "S5凤凰居5号楼"
    },
    {
        "buildingid": "1503976037",
        "building": "凤凰居10号楼"
    },
    {
        "buildingid": "1503975890",
        "building": "S2从文书院"
    },
    {
        "buildingid": "1693031710",
        "building": "阅海居B10楼"
    },
    {
        "buildingid": "1693031698",
        "building": "阅海居B9楼"
    },
    {
        "buildingid": "1574231835",
        "building": "T3"
    },
    {
        "buildingid": "1503976004",
        "building": "S9凤凰居9号楼"
    },
    {
        "buildingid": "1503975988",
        "building": "S7凤凰居7号楼"
    },
    {
        "buildingid": "1503976037",
        "building": "S10凤凰居10号楼"
    },
    {
        "buildingid": "1503975995",
        "building": "S8凤凰居8号楼"
    },
    {
        "buildingid": "1599193777",
        "building": "凤凰居11/13号楼"
    },
    {
        "buildingid": "1574231833",
        "building": "专家公寓2号楼"
    },
    {
        "buildingid": "1503975902",
        "building": "凤凰居3号楼"
    },
    {
        "buildingid": "1693031710",
        "building": "B10"
    },
    {
        "buildingid": "1661835249",
        "building": "B1"
    },
    {
        "buildingid": "1503975950",
        "building": "凤凰居4号楼"
    },
    {
        "buildingid": "1503975980",
        "building": "S6凤凰居6号楼"
    }
]
""")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G9600 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}


def building_to_id(building):
    for _building in BUILDINGS:
        if _building['building'] == building:
            return _building['buildingid']
    print('building error!')
    exit(-1)


def query(account, building, room) -> float:
    """
    :param account: 6位校园卡账号
    :param building: 宿舍楼名称, ['T1', 'T3', 'S1一多书院', 'S2从文书院', 'S5凤凰居5号楼', 'S6凤凰居6号楼', '凤凰居6号楼', 'S7凤凰居7号楼', 'S8凤凰居8号楼', 'S9凤凰居9号楼', '凤凰居9号楼', 'S10凤凰居10号楼', 'S11'] 中的一个
    :param room: 宿舍号, 一般是字母+数字
    :return: 电余量
    """
    data = {
        "jsondata": json.dumps({
            "query_elec_roominfo": {
                "aid": "0030000000002505",
                "account": str(account),
                "room": {
                    "roomid": room,
                    "room": room
                },
                "floor": {
                    "floorid": "",
                    "floor": ""
                },
                "area": {
                    "area": "青岛校区",
                    "areaname": "青岛校区"
                },
                "building": {
                    "buildingid": building_to_id(building),
                    "building": building
                }
            }
        }, ensure_ascii=False),
        "funname": "synjones.onecard.query.elec.roominfo",
        "json": "true"
    }
    try:
        response = requests.post('http://10.100.1.24:8988/web/Common/Tsm.html', headers=HEADERS, data=data)
        if response.status_code == 200:
            electricity = json.loads(response.text)['query_elec_roominfo']['errmsg']
            return float(electricity[8:])
    except Exception as e:
        print(e)
        exit(-1)
