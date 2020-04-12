# -*- coding: utf-8 -*-
from ...client import get_api_client

def get_league_list(page_size,page):
	"""批量获取赛事列表
	参数page_size,page
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/list"#赛事列表
	data={}
	if page_size>0: data["page_size"]=page_size;
	if page >0: data["page"]=page;

	return client.api(uri, data)

def get_league_detail(v_league_id):
	"""单个获取赛事详情
	参数v_league_id=[string], FunData 内部维护的联赛 ID
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/detail"#赛事详情
	data={}
	if len(v_league_id)>0: data["v_league_id"]=v_league_id;

	return client.api(uri, data)

def get_league_team_list(v_league_id):
	"""单个联赛队伍列表
	参数v_league_id=[string], FunData 内部维护的联赛 ID
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/join/team/list"#联赛队伍列表
	data={}
	if len(v_league_id)>0: data["v_league_id"]=v_league_id;

	return client.api(uri, data)