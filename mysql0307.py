#!/usr/bin/python
# -*- coding:utf-8 -*-
# -*- author:yyy -*-

import pymysql  # 导入模块
import hashlib  # MD5加密解密

str1 = list(input('input a string:'))
mydict = {'test1': 'xx.xx.xx.xx', 'test2': 'xx.xx.xx.xx', 'test3': 'xx.xx.xx.xx'}
mykeys = mydict.keys()
str2 = ''.join(str1)
if str2 in mykeys:
    # print(mydict[str2])
    HOST = mydict[str2]
else:
    print('Error occurred!')

a = input('输入加密的字符:')
b = hashlib.md5()
b.update(a.encode(encoding='utf-8'))
# print ('MD5加密前：'+ a)
# print ('MD5加密后：'+b.hexdigest())
mydict1 = {'0': 'acct_account_0', '1': 'acct_account_1', '2': 'acct_account_2', '3': 'acct_account_3',
           '4': 'acct_account_4', '5': 'acct_account_5', '6': 'acct_account_6', '7': 'acct_account_7',
           '8': 'acct_account_8', '9': 'acct_account_9', 'a': 'acct_account_10', 'b': 'acct_account_11',
           'c': 'acct_account_12', 'd': 'acct_account_13', 'e': 'acct_account_14', 'f': 'acct_account_15'}
list1 = list(b.hexdigest())
print(list1[-1])
table = list1[-1]
mykeys1 = mydict1.keys()
if table in mykeys1:
    # print('retable:'+mydict1[table])
    retable = mydict1[table]
else:
    print('Error occurred again!')

# 远程连接数据库
db = pymysql.connect(
    host='HOST',
    port=3306,
    user='uer',
    passwd='pwd',
    db='db_platform',
    charset='utf8'
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

currency1 = ['BTC', 'USDT', 'ETH', 'TRX', 'BNB', 'SOL']
for k in currency1:
    sql = "insert into {0} (`currency`,`user_id`,`product_no`,`available`,`frozen`,`expire_time`,`is_deleted`,`create_time`,`update_time`) values('{1}', '{2}', '2001', 100, 0, '2038-01-01', 0, '2022-03-03', '2022-03-03')".format(
        retable, k, a)
    # print(sql)
    insert = cursor.execute(sql)
    print('批量插入返回受影响的行数：', insert)

db.commit()  # COMMIT命令用于把事务所做的修改保存到数据库
cursor.close()  # 关闭游标
db.close()  # 关闭数据库连接
