#!/usr/bin/python3
#-*-coding:utf-8-*-


import threading
from Sqlcore import Sqlcore


'''
入口功能
'''

'''vmode打印显示模式full/standard/simple'''


#生产环境的photo相册
conn = {"hostname":"xxxxxx.mysql.rds.aliyuncs.com","username":"forpython","password":"Ffu398fh_GFUPY","database":"dbuser","hostport":3708}
cfgs = {"table":"bota_photo", "column":"corver,gallery", "offset":0, "vmode":"full", "limit":5, "sleep": 1}

#本机的photo相册
conn = {"hostname":"localhost","username":"website","password":"website123","database":"dbuser","hostport":3306}
cfgs = {"table":"bota_photo", "column":"corver,gallery", "offset":0, "vmode":"full", "limit":5, "sleep": 0}

#去哪儿酒店的配置
#conn = {"hostname":"192.168.1.11","username":"website","password":"website123","database":"dbuser","hostport":3306}
#cfgs = {"table":"bota_hotel", "column":"cover,photos", "offset":0, "vmode":"full", "limit":50, "sleep": 5}




if __name__ == "__main__":
    
    sc = Sqlcore("x1", conn, cfgs)
    sc.run()

    print("welcome")
