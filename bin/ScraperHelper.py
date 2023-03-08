from urllib import request as uReq
from bs4 import BeautifulSoup as soup
import os


def fillProductName(productScraped):

    # getting html
    uClient = uReq.urlopen(productScraped.url)
    page_html = uClient.read()
    uClient.close()

    # html parser
    page_soup = soup(page_html, "html.parser")

    #getting product name
    # getting product name Buscalibre
    if productScraped.commerceId == 1:

        containers_title = page_soup.findAll(productScraped.nameClass, {productScraped.nameTag})
        contain_title = containers_title[0]
        productScraped.productName = contain_title.h1.text

    # getting product name Portal Inmobiliario
    if productScraped.commerceId == 2:

        containers_title = page_soup.findAll(productScraped.nameClass, {productScraped.nameTag})
        contain_title = containers_title[0]
        productScraped.productName = contain_title.text.strip()

    # getting product name ShazamComics
    if productScraped.commerceId == 3:

        containers_title = page_soup.find(productScraped.nameClass, property=productScraped.nameTag)
        contain_title = containers_title["content"]
        productScraped.productName = contain_title.strip()


def fillerProductPrice(productScraped):

    # getting html
    uClient = uReq.urlopen(productScraped.url)
    page_html = uClient.read()
    uClient.close()

    # html parser
    page_soup = soup(page_html, "html.parser")

    # getting product prices
    if productScraped.commerceId == 1:

        # getting price Buscalibre
        containers = page_soup.findAll(productScraped.priceClass, {productScraped.priceTag})
        if (len(containers)):
            contain = containers[0]
            productScraped.valor = contain.span.text.strip()

    if productScraped.commerceId == 2:

        # getting price Portal Inmobiliario
        containers = page_soup.findAll(productScraped.priceClass, {productScraped.priceTag})
        if (len(containers)):
            contain = containers[0]
            productScraped.valor = contain.text.strip()

    if productScraped.commerceId == 3:

        # getting price Shazam Comics
        containers = page_soup.find(productScraped.priceClass, property=productScraped.priceTag)
        productScraped.valor = containers["content"]

    productScraped.formatValor()



def printDone(counter, sites):

    print("Done!")
    print("")
    print("")
    print("-------------------------")
    print("---------RESUMEN---------")
    print("-------------------------")
    print("Links actualizados: " + str(counter))
    print("Sitios revisados: ")
    countsitesrow = 0

    for siterow in sites:
        countsitesrow += 1
        print(str(countsitesrow) + ".- " + siterow)

    print("-----------------------")


def excecuteCompareBash():
    os.system('/home/capi/Devs/python3/scrapper3/scripts/comparator.sh')