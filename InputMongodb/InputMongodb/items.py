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

import scrapy


class InputmongodbItem(scrapy.Item):
    tag = scrapy.Field()  # 标签字段
    cont = scrapy.Field()  # 名言内容
    pass