#coding:utf-8
# -*- coding: utf-8 -*-
from util.oss import const_var
import oss2
import pprint
auth = oss2.Auth(const_var.ID, const_var.KEY)
# APScheduler


def get_bucket(auth, end_point, bucket_name, timeout=60, enable_crc=True):
    bucket = oss2.Bucket(auth, end_point, bucket_name,
                         connect_timeout=timeout, enable_crc=enable_crc)
    return bucket


def upload(oss_url, file):
    bucket = get_bucket(auth, const_var.ENDPOINT,
                        const_var.BUCKET_NAME, timeout=60, enable_crc=True)
    # pprint.pprint(bucket.put_object(oss_url, file).status)
    result = bucket.put_object(oss_url, file)
    return oss_result_handle(result)


def oss_result_handle(result):
    if result.status == 200:
        return True
    else:
        return False


if __name__ == '__main__':
    # upload('testupload.txt', './local.txt')
    print('1')

#oss api result
# class RequestResult(object):
#     def __init__(self, resp):
#         #: HTTP响应
#         self.resp = resp

#         #: HTTP状态码
#         self.status = resp.status

#         #: HTTP头
#         self.headers = resp.headers

#         #: 请求ID，用于跟踪一个OSS请求。提交工单时，最后能够提供请求ID
#         self.request_id = resp.headers.get('x-oss-request-id', '')
