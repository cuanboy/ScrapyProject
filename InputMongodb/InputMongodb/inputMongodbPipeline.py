"""
功能：本项目主要演示Scrapy数据存储mongodb具体操作；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入InputMongodb目录（scrapy.cfg目录)输入：

scrapy crawl IntoMongodbSpider

项目详情：http://www.scrapyd.cn/jiaocheng/171.html；
注意事项：运行前请确保mongodb已安装并已启动
创建时间：2018年1月31日12:08:02
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import pymongo


class InputmongodbPipeline(object):
    def __init__(self):
        # 建立MongoDB数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017)
        # 连接所需数据库,ScrapyChina为数据库名
        db = client['ScrapyChina']
        # 连接所用集合，也就是我们通常所说的表，mingyan为表名
        self.post = db['mingyan']

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.post.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写
