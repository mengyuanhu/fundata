#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
from ...client import get_api_client

#单场赛前
def get_batch_basic_info(start_time, start_from=0, limit=100):
    """批量获取比赛基本数据, 可以批量获取从一天开始(UTC时间)获取到一天结束的比赛基本数据

    `start_time` required, 比赛开始时间, 表示取从何时开始的比赛数据
    `start_from` optional, 比赛ID, 表示取从哪场比赛之后的比赛数据;
                 不为空时，start_from 与 start_time 必须具体为某一场比赛对应的数据
                 比如第一次以 start_time 获取了一个比赛列表后，列表最后的比赛对应的ID为 3813773851, 对应的比赛开始时间是1522724457，
                 则获取之后的比赛列表的方式是传 start_time=1522724457,start_from=3813773851，即可获取开始在1522724457之后并且比赛ID大于3813773851的比赛列表;
                 如此往复，知道返回的数据条目数小于 limit，然后再从新的一天的 start_time 开始
    `limit` optional, 表示返回数据的最大条目数，传零或者不传默认返回100条数据，不可超过 200，如果返回的条目数小于limit，则意味着当前的查询条件已经没有更多数据了
    """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/basic-info/batch' #单场赛前-批量比赛信息
    data = {
        "start_time":start_time,
        }

    if start_from > 0:
        data['start_from'] = start_from

    if limit > 0 and limit <= 200:
        data['limit'] = limit

    return client.api(uri, data)

def get_batch_ban_pick(start_time, start_from=0, limit=100,):
    """获取批量比赛ban-picks信息
    参数：start_time=[long] 表示取哪个时间之后的数据； 当需要通过某一次的返回结果取之后的比赛信息时需要设置为当前获取的结果的数组的最后一个 match_start_time
    Optional：start_from=[long] 当需要通过某一次的返回结果取之后的比赛信息时需要用到，设置为当前获取的结果的数组的最后一个match_id
    Optional：limit=[int] 取值范围为 [0,200]，表示返回最多多少结果，limit 不传或者为0时，返回100条数据
    返回dict格式：如果不是队长模式的比赛，返回的数据里可能只有 ban 的信息，没有 pick 的信息
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/ban-picks/batch' #单场赛前-批量比赛bp信息

    data = {
        "start_time":start_time,
        }

    if start_from > 0:
        data['start_from'] = start_from

    if limit > 0 and limit <= 200:
        data['limit'] = limit

    return client.api(uri, data)

def get_batch_match_player(start_time, start_from=0, limit=100,):
    """获取批量比赛选手数据
    参数：start_time=[long] 表示取哪个时间之后的数据； 当需要通过某一次的返回结果取之后的比赛信息时需要设置为当前获取的结果的数组的最后一个 match_start_time
    Optional：start_from=[long] 当需要通过某一次的返回结果取之后的比赛信息时需要用到，设置为当前获取的结果的数组的最后一个match_id
    Optional：limit=[int] 取值范围为 [0,200]，表示返回最多多少结果，limit 不传或者为0时，返回100条数据
    返回dict格式：如果不是队长模式的比赛，返回的数据里可能只有 ban 的信息，没有 pick 的信息
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/players/batch' #单场赛前-批量比赛选手数据

    data = {
        "start_time":start_time,
        }

    if start_from > 0:
        data['start_from'] = start_from

    if limit > 0 and limit <= 200:
        data['limit'] = limit

    return client.api(uri, data)

def get_batch_ability_upgrades(start_time, start_from=0, limit=100,):
    """获取批量比赛选手技能加点
    参数：start_time=[long] 表示取哪个时间之后的数据； 当需要通过某一次的返回结果取之后的比赛信息时需要设置为当前获取的结果的数组的最后一个 match_start_time
    Optional：start_from=[long] 当需要通过某一次的返回结果取之后的比赛信息时需要用到，设置为当前获取的结果的数组的最后一个match_id
    Optional：limit=[int] 取值范围为 [0,200]，表示返回最多多少结果，limit 不传或者为0时，返回100条数据
    返回dict格式：如果不是队长模式的比赛，返回的数据里可能只有 ban 的信息，没有 pick 的信息
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/players-ability-upgrades/batch' #单场赛前-批量比赛选手技能加点

    data = {
        "start_time":start_time,
        }

    if start_from > 0:
        data['start_from'] = start_from

    if limit > 0 and limit <= 200:
        data['limit'] = limit

    return client.api(uri, data)

#单场赛后
def get_single_basic_info(match_id):
    """获取比赛的基本信息
    参数match_id=[int]比赛编号
    返回dict格式
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/basic-info' #单场赛后-比赛信息
    data = {}
    if match_id > 0:
        data['match_id'] = match_id

    return client.api(uri, data)

def get_single_general_info(match_id):
    """获取比赛的基本信息+队员信息+ban/pick信息+队员技能升级信息+队伍信息
    参数match_id=[int]比赛编号
    返回dict格式
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/general-info' #单场赛后-比赛详情
    data = {}
    if match_id > 0:
        data['match_id'] = match_id

    return client.api(uri, data)

def get_single_ban_picks(match_id):
    """比赛bp信息
    参数match_id=[int]比赛编号
    返回dict格式
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/ban-picks' #单场赛后-比赛bp信息
    data = {}
    if match_id > 0:
        data['match_id'] = match_id

    return client.api(uri, data)

def get_single_ability_upgrades(match_id):
    """比赛选手技能加点
    参数match_id=[int]比赛编号
    返回dict格式
   """

    client = get_api_client()
    uri = '/fundata-dota2-free/v2/match/players-ability-upgrades' #单场赛后-比赛选手技能加点
    data = {}
    if match_id > 0:
        data['match_id'] = match_id

    return client.api(uri, data)