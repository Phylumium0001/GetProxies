# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GetproxiesPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Remove first two items
        proxies = adapter.get('proxies')
        i = 0
        for proxy in proxies:
            if i == 2:
                break
            else:
                proxies.remove(proxy)
                i += 1

        adapter['proxies'] = proxies


        return item








