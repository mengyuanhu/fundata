#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from .request import FundataApiException, ApiClient

api_client = None
#从fundata申请到的key
public_key="1cae5ca0cbf4009f5298160292992f6d"
secret_key="b6412b7cdd25eabc83e2cdb927f56506"

def get_api_client():
    """获取 api client 对象
    """
    #print('get', api_client)
    if api_client is None:
        raise FundataApiException('API client is not initialized')

    return api_client


def init_api_client(public_key="1cae5ca0cbf4009f5298160292992f6d", secret_key="b6412b7cdd25eabc83e2cdb927f56506", api_server=None):
    """初始化 api client，创建全局api_client
    参数public_key和secret_key默认填写, api_server默认None,
    无返回值
    """
    if api_server is not None:
        ApiClient.configure(api_server)

    global api_client
    api_client = ApiClient(public_key, secret_key)
    #print('init', api_client)
