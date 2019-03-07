from lxml import html
import requests

list_prod = ['as', 'sa']


def scraping(retailer, link, qty):
    if (retailer == """Colorpop: [$50]💄"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@class="prod-name"]/text()')
        prod_price = tree.xpath('//*[@id="mainprice"]/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[8:12]
        return list_prod

    elif (retailer == """Sephora: [$40]💄"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@class="product-brand"]/a/text()')
        prod_price = tree.xpath(
            '//*[@class="product-price"]/a/text()')
        list_prod[0] = prod_name
        list_prod[1] = prod_price
        return list_prod

    elif (retailer == """Zara: [$79]👚"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@id="product"]/div[1]/div/div[2]/header/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="product"]/div[1]/div/div[2]/div[1]/node()')
        list_prod[0] = prod_name[0]
        list_prod[1] = prod_price
        return list_prod

    elif (retailer == """The Editor's Market: [$60]👚"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="node-product-right-inner"]/h1/text()')
        prod_price = tree.xpath(
            '//*[@id="node-product-price"]/div[' + qty + ']/div[1]/span/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[1:]
        return list_prod

    elif (retailer == """Uniqlo: [$60]👚"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath('//*[@id="goodsNmArea"]/span/text()')
        prod_price = tree.xpath(
            '//*[@id="product-price-7"]/text()')
        list_prod[0] = (prod_name[0])[21:]
        list_prod[1] = (prod_price[0])[2:]
        return list_prod
    elif (retailer == """Colorpop: [$50]💄"""):
        page = requests.get(link)
        tree = html.fromstring(page.content)
        # This will create a list of buyers:
        prod_name = tree.xpath(
            '//*[@class="prod-name"]/text()')
        prod_price = tree.xpath('//*[@id="mainprice"]/text()')
        list_prod[0] = prod_name[0]
        list_prod[1] = (prod_price[0])[8:12]
        return list_prod


# print(scraping("""Sephora: [$40]💄""",
#                """https://www.sephora.sg/products/burts-bees-soap-bark-and-chamomile-deep-cleansing-cream/v/default""", "NA"))
print(scraping(
    """Zara: [$79]👚""", """https://www.zara.com/sg/en/check-shirt-p04284415.html?v1=9561638&v2=1181080""", "NA"))
