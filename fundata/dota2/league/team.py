# -*- coding: utf-8 -*-

from ...client import get_api_client
#基础信息

def get_batch_team(page=0,limit=16):
	"""批量获取战队列表
	page=[int]，默认为 0
	limit=[int]，默认为 16
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/team"#战队列表
	data={}
	if page>0: data["page"]=page;
	if limit >0: data["limit"]=limit;

	return client.api(uri, data)

def get_single_team(team_id):
	"""单个获取战队
	team_id=[int] 战队编号
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/team/info"#战队信息
	data={}
	if team_id>0: data["team_id"]=team_id;

	return client.api(uri, data)

def get_team_player(team_id):
	"""战队下队员的列表
	team_id=[int] 战队编号
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/team-with-players"
	data={}
	if team_id>0: data["team_id"]=page;

	return client.api(uri, data)