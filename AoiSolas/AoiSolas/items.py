# -*- coding: utf-8 -*-

"""
项目描述：《Scrapy采花大盗小爬虫》：本scrapy爬虫，教大家爬取整个妹纸网站，妹纸4000多，图片10W多，合计10G多数据量……
运行环境：win7 64 + python3.6 + scrapy1.4
运行方式：进入AoiSolas目录（scrapy.cfg所在目录)输入：

scrapy crawl AoiSola

代码详解：http://www.scrapyd.cn/example/176.html;
创建时间：2018年4月20日22:23:19
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""

import scrapy


class AoisolasItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ImgUrl = scrapy.Field()
    pass
