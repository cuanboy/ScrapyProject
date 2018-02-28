# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy下载图片；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入ImageSpider目录（scrapy.cfg所在目录)输入：

scrapy crawl ImgSpider

项目详情：http://www.scrapyd.cn/example/174.html；
创建时间：2018年2月28日12:47:46
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            yield Request(image_url)

    # def file_path(self, request, response=None, info=None):
    #     # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    #     image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
    #     return image_guid
