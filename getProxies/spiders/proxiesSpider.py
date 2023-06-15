import scrapy
from getProxies.items import Proxyitem  


class ProxiesspiderSpider(scrapy.Spider):
    name = "proxiesSpider"
    allowed_domains = ["spys.one"]
    start_urls = ["https://spys.one/en//"]

    custom_settings = {
        'FEEDS': {
            'proxydata.json': {'format': 'json', 'overwrite': True},
        }
    }

    def parse(self, response):
        proxyItem = Proxyitem()
        proxyItem['proxies'] =  response.xpath("//tr[@class='spy1x']/td[1]/font/text()").extract()
        
        return proxyItem