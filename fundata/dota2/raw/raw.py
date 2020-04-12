# -*- coding: utf-8 -*-

from ...client import get_api_client


def get_hero():
	"""批量英雄列表
	不需要参数
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/raw/hero"#英雄信息
	data={}

	return client.api(uri, data)

def get_item():
	"""批量道具信息
	不需要参数
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/raw/item"#道具信息
	data={}

	return client.api(uri, data)
