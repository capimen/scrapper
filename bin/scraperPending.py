import ScraperHelper
from ProductScraped import ProductScraped
from SqlHelper import SqlHelper


sqlHelper = SqlHelper()
myresult = sqlHelper.select_pending()


counter = 0
sites = []

print("excecuting pending:")

for row in myresult:

    #mapping to variables
    productScraped = ProductScraped(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    ScraperHelper.fillProductName(productScraped)
    ScraperHelper.fillerProductPrice(productScraped)

    #Site counting
    counter += 1
    sites_name_flag = True

    for sites_name in sites:

        if sites_name == productScraped.commerceName:

            sites_name_flag = False

    if sites_name_flag:

        sites.append(productScraped.commerceName)

    print(str(productScraped.productId) + "\t..........\t" + str(productScraped.valor) + "\t..........\t"+ productScraped.commerceName + "\t..........\t"+ productScraped.productName)

    sqlHelper.insert_historical(productScraped)

    # ejecutar este insert solo cuando hay link nuevo para cargar el nombre
    #sqlHelper.update_product_name(productScraped)

ScraperHelper.printDone(counter, sites)
ScraperHelper.excecuteCompareBash()