#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
from ....client import get_api_client

BasicInfoURI = '/fundata-dota2-free/v2/match/basic-info'


def get_single_basic_info(match_id):
    """获取单个比赛基本数据

    `match_id` required, 比赛编号
   """

    client = get_api_client()
    data = {
        'match_id': match_id,
    }

    return client.api(BasicInfoURI, data)
