from ProductHistoricalInfo import ProductHistoricalInfo
from SqlHelper import SqlHelper
from Product import Product

sqlHelper = SqlHelper()
myresultPid = sqlHelper.select_get_product()

# limpia la tabla de comparacion
ProductHistoricalInfo.truncateComparator()

resumenCount = 0


for row in myresultPid:

    resumen = False

    product = Product(row[0], row[1], row[2], row[3], row[4])
    product.printInfo()

    sqlHelperh = SqlHelper()
    myResultHistoricals = sqlHelperh.select_get_productHistorical(product.id)

    for rowh in myResultHistoricals:

        productHistoricalInfo = ProductHistoricalInfo(product, rowh[1], rowh[3], rowh[4], 1.0, 0.0, 0.0, 0.0)
        # insercion de comparacion en la base de datos
        productHistoricalInfo.insertComparator()
        # escritura de comparacion al archivo de logs
        productHistoricalInfo.printInfo()

        if productHistoricalInfo.percentPrice < productHistoricalInfo.umbral:            

            resumen = productHistoricalInfo.printHighLightInfo("Umbral")

        if productHistoricalInfo.product.referencePrice is not None:

            if productHistoricalInfo.priceNewest < productHistoricalInfo.product.referencePrice:                

                resumen = productHistoricalInfo.printHighLightInfo("Precio Referencia")

        if resumen:

            resumenCount += 1

if resumenCount != 0:

    print("")
    print("")
    print("Existen " + str(resumenCount) + " precios destacados")
    print("")
    print("")
