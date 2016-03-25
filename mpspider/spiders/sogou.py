# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.link import Link

class PageItem(scrapy.Item):
    title = scrapy.Field()

class SogouSpider(CrawlSpider):
    handle_httpstatus_list = [302]
    name = "sogou"
    cookie = ''
    allowed_domains = ["weixin.sogou.com",'mp.weixin.qq.com']
    start_urls = [
        'http://weixin.sogou.com/weixin?type=1&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=12304&sst0=1458730727228&lkt=4%2C1458730721514%2C1458730727088&query=',
        # 'http://weixin.sogou.com/weixin?type=1&query=%E4%BF%A1%E7%94%A8%E5%8D%A1&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=12304&sst0=1458730727228&lkt=4%2C1458730721514%2C1458730727088',
        # 'http://weixin.sogou.com/gzh?openid=oIWsFt1T5FOB05yWoDGJV13adT5A&ext=I1fZar2WXBFToUc_pemqn-edrj94dXbnN-5w9SYFA7wCOBPf25LL_DkpzJQ9-9Zr',
        # 'http://weixin.sogou.com/gzhjs?ext=pbbx73yLDYYU_yXUl79qkkzt75yDOMkJBgZNu06g98A8acUlOBe9D4HUZVJBYoec&openid=oIWsFt-vTc-mkQpwBkA3j_G4JlEM&cb=sogou.weixin_gzhcb&page=1'
    ]

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        # Rule(LinkExtractor(allow=('/gzh\?openid='), tags='div'), callback='parse_index'),
        # Rule(LinkExtractor(allow=('/gzh\?openid=oIWsFt1T5FOB05yWoDGJV13adT5A'), tags='div'), callback='parse_index'),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        # Rule(LinkExtractor(allow=('/websearch/art\.jsp', '/s\?__biz')), callback='parse_item'),
        # Rule(JsonLinkExtractor()),
    )
    # def make_requests_from_url(self, url):
    #     req=super(SogouSpider, self).make_requests_from_url(url)
    #     if self.cookie:
    #         req.headers['Cookie'] = self.cookie
    #     return req
    #     
    #     
    def __init__(self, query='', pagelimit=1):
        super(SogouSpider, self).__init__()
        self.start_urls[0] += query
        self.pagelimit = pagelimit

    def parse_gzhjs(self, response):
        data=response.body
        import json
        import xml.etree.cElementTree as ET
        data=  json.loads(data)
        data=data['items']
        xmlp = ET.XMLParser(encoding="utf-8")
        if not data:
            print 'error!!!!!!!!!!!!!!!!!!!!!!!!!'
        for i in data:
            # s = i.decode('gbk')
            s=i.encode('utf-8').replace('encoding="gbk"','encoding="utf-8"')
            s=ET.fromstring(s)
            root=ET.ElementTree(s).getroot()
            title= root[1][3][2].text
            url= root[1][3][3].text
            imglink= root[1][3][5].text
            yield scrapy.Request('http://weixin.sogou.com'+url, self.parse_item)

    def parse_start_url(self, response):
        url=response.css('div.wx-rb.bg-blue.wx-rb_v1._item::attr(href)').extract_first()
        print url
        yield scrapy.Request('http://weixin.sogou.com'+url, callback=self.parse_index)

    def parse(self, response):
        # if response.status == 302:
        #     # reload
        #     print 'Reload!!!!!!!!!!!!' + response.url
        #     print 'Location' + response.headers['Location']
        #     print response.request.headers
        #     print response.headers
        #     return scrapy.Request(response.url, cookies=None, meta={'dont_merge_cookies':True})
        return super(SogouSpider, self).parse(response) 

    def parse_index(self, response):
        title = response.css('h3#weixinname::text').extract()[0].encode('utf-8')
        # parse ajax
        for i in range(self.pagelimit):
            gzhjs_url = response.url.replace('/gzh', '/gzhjs') + '&page=' + str(i+1)
            yield scrapy.Request(url=gzhjs_url, callback=self.parse_gzhjs)

    def parse_item(self, response):
        title = response.css('h2#activity-name::text').extract()[0].encode('utf-8')
        print title
        yield {'title':title, 'url':response.url}
