#!/usr/bin/python3

import os
import cgi
import redis
import json

# 不想写代码，没有异常处理


def main():
    # 获取请求方法
    request_method = os.environ.get('REQUEST_METHOD')
    # r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    resp = "Content-type: application/json\r\n\r\n"
    # 判断请求方法
    if request_method == 'GET':  # return all the comment
        comment = r.hgetall('discuss')
        comment_map = {}
        for field, value in comment.items():
            comment_map[field.decode('utf-8')] = value.decode('utf-8')
        resp = resp + json.dumps(comment_map)
    elif request_method == 'POST':  # add this comment to redis
        form = cgi.FieldStorage()
        # 解析 POST 数据
        r.hset('discuss', form['name'].value, form['comment'].value)
    else:
        resp = resp + 'server error: unknow request method'
    r.close()  # 关闭数据库连接
    print(resp)


if __name__ == '__main__':
    main()
