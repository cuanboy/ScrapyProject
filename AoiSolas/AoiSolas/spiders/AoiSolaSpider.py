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
from AoiSolas.items import AoisolasItem


class AoisolaspiderSpider(scrapy.Spider):
    name = "AoiSola"
    allowed_domains = ["www.mm131.com"]
    start_urls = ['http://www.mm131.com/xinggan/',
                  'http://www.mm131.com/qingchun/',
                  'http://www.mm131.com/xiaohua/',
                  'http://www.mm131.com/chemo/',
                  'http://www.mm131.com/qipao/',
                  'http://www.mm131.com/mingxing/'
                  ]

    def parse(self, response):
        list = response.css(".list-left dd:not(.page)")
        for img in list:
            imgname = img.css("a::text").extract_first()
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl2 = str(imgurl)
            print(imgurl2)
            next_url = response.css(".page-en:nth-last-child(2)::attr(href)").extract_first()
            if next_url is not None:
                # 下一页
                yield response.follow(next_url, callback=self.parse)

            yield scrapy.Request(imgurl2, callback=self.content)

    def content(self, response):
        item = AoisolasItem()
        item['name'] = response.css(".content h5::text").extract_first()
        item['ImgUrl'] = response.css(".content-pic img::attr(src)").extract()
        yield item
        # 提取图片,存入文件夹
        # print(item['ImgUrl'])
        next_url = response.css(".page-ch:last-child::attr(href)").extract_first()

        if next_url is not None:
            # 下一页
            yield response.follow(next_url, callback=self.content)

