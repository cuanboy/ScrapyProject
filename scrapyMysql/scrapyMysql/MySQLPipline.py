"""
功能：本项目主要演示Scrapy数据存储MySQL具体操作；
运行环境：win7 64 + python3.6 + scrapy1.4 + mysql；
运行方式：进入scrapyMysql目录（scrapy.cfg目录)输入：

scrapy crawl inputMysql

项目详情：http://www.scrapyd.cn/jiaocheng/170.html；
注意事项：运行前请按项目详情创建好mysql数据库、表、字段；
创建时间：2018年1月30日14:40:50；
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import pymysql.cursors


class MySQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapyMysql',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into mingyan(tag, cont)
            value (%s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['tag'],  # item里面定义的字段和表字段对应
             item['cont'],))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回
