# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy下载图片重命名并放入不同目录；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入ImagesRename目录（scrapy.cfg所在目录)输入：

scrapy crawl ImgsRename

项目详情：http://www.scrapyd.cn/example/175.html；
创建时间：2018年2月28日20:50:24；
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import scrapy
from ImagesRename.items import ImagesrenameItem

class ImgsrenameSpider(scrapy.Spider):
    name = 'ImgsRename'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html',
                  'http://lab.scrapyd.cn/archives/57.html',
                  ]

    def parse(self, response):
        # 实例化item
        item = ImagesrenameItem()
        # 注意imgurls是一个集合也就是多张图片
        item['imgurl'] = response.css(".post img::attr(src)").extract()
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item
