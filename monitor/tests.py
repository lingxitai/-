from django.test import TestCase
import os,sqlite3
# Create your tests here.
sqlpath=os.path.join(os.path.dirname(os.path.dirname(__file__)),'db.sqlite3')
db=sqlite3.connect(sqlpath)
cursor=db.cursor()
data=cursor.execute('select id from monitor_user  left join monitor_user_qx  '
                    '(on monitor_user.username=monitor_user_qx.username) where monitor_user_qx.quanxian="新增")')
data1=data.fetchall()
print(data1)



# class BaseDB(object):
#     def __init__(self):
#         try:
#             self.db = sqlite3.connect(sqlpath)
#             self.cursor = self.db.cursor()
#         except ConnectionError as e:
#             getlog.error('连接数据报错了，报错信息为：{0}'.format(e))
#
#     def excutesql(self, sql):
#         reslut = self.cursor.execute(sql)
#         self.db.commit()
#         getlog.info('数据库执行结果为{0}'.format(reslut))
#         return reslut
#
#     def __close_db(self):
#         self.cursor.close()  # 先关cursor再关connect
#         self.db.close()
#         getlog.info('数据库已关闭')
#
#     def get_all_data(self, sql):
#         all_data = self.excutesql(sql)
#         data = all_data.fetchall()
#         getlog.info('数据库执行get_all_data方法查询结果为: \n {0}'.format(data))
#         self.__close_db()
#         return data