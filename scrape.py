from lxml import html
import requests

list_prod = ['as', 'sa']


def scraping(retailer, link, qty):
    if (retailer == """The Editor's Market: [$60]👚"""):
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
