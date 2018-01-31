# -*- coding: utf-8 -*-
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
from InputMongodb.items import InputmongodbItem

class IntomongodbspiderSpider(scrapy.Spider):

    name = "IntoMongodbSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css('div.quote')

        item = InputmongodbItem()  # 实例化item类

        for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签
            item['cont'] = v.css('.text::text').extract_first()
            # 提取名言
            tags = v.css('.tags .tag::text').extract()
            # 数组转换为字符串
            item['tag'] = ','.join(tags)
            # 把取到的数据提交给pipline处理
            yield item
        # css选择器提取下一页链接
        next_page = response.css('li.next a::attr(href)').extract_first()
        # 判断是否存在下一页
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # 提交给parse继续抓取下一页
            yield scrapy.Request(next_page, callback=self.parse)
