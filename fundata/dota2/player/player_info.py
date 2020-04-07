# -*- coding: utf-8 -*-

from ...client import get_api_client

uri="/fundata-dota2-free/v2/league/player"
def get_batch_player(page=0, limit=16):
	"""批量获取队员信息
	参数page-optional, default=0 
	参数limit-optional, defailt=16
	返回dict格式
	"""
	client=get_api_client()
	data={}
	if page>0: data["page"]=page;
	if limit >0: data["limit"]=limit;

	return client.api(uri, data)