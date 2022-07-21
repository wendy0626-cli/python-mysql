#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- author:yyy -*-

import pymysql

# from course import dict_data_richer,dict_data_course,dict_data_transfer

dict01 = {'cover': '/public-test/img/game/1611835597068SHWDDR3120.jpg', 'id': '222', 'no': 'abc', 'uk': 'ABCD'}

# 创建连接对象
db = pymysql.connect(
    host='xx.xx.xxx.xxx',
    port=3306,
    user='xxxx',
    passwd='xxxx',
    db='xxxxx',
    charset='utf8'
)

# 获取游标对象
cursor = db.cursor()
# 假设前缀分别是
for i in range(0, 10):
    prefix = '{0}'.format(i)
    uid = '{0}{1}'.format(prefix, dict01.get('id'))  # id里0会省略
    ono = '{0}{1}'.format(prefix, dict01.get('no'))
    ufield = '{0}{1}'.format(prefix, dict01.get('uk'))
    # 事务处理
    sql = "INSERT INTO `activity_prize_detail` (`user_id`,`act_id`,`type`,`link_no`,`prize_ratio`,`period_no`,`order_no`,`currency`,`amount`,`uk_field`,`pledge_amount`,`status`,`is_deleted`,`create_time`,`update_time`) VALUES ('{0}',223,1,'',0.7,4,'{1}','USDT',0.1,'{2}',1,2,0,'2021-12-22','2021-12-22')".format(
        uid, ono, ufield)
    cursor.execute(sql)
    db.commit()

# 关闭连接
cursor.close()
