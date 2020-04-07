# -*- coding: utf-8 -*-

from ...client import get_api_client


def get_player_detail_stats(player_id):
	"""玩家常规统计数据
	参数player_id，玩家ID， int
	返回dict格式
	"""
	if get_player_data_status(player_id)==2:
		client=get_api_client()
		uri="/fundata-dota2-free/v2/player/"+str(player_id)+"/detail_stats"
		return client.api(uri,{})
	else:
		print("player_id=%i has no data"%player_id)
		return 0


def get_player_data_status(player_id):
	"""玩家数据状态
	参数player_id，玩家ID， int
	返回dict格式: status统计数据的状态, 2有数据，1没有数据
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/player/"+str(player_id)+"/data_status"
	res=client.api(uri,{})
	if res["retcode"]==200 and res["data"]["status"]==2:
		return 2
	else:
		return 1