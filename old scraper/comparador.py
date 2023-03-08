import mysql.connector
import querys
from printData import printRow, printHighLightRow

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="scraper"
)

mycursor2 = db.cursor()
datacsv = []

#prueba
idProductBestPrice = "1"

mycursor2.execute(querys.select_get_product)
myresultPid = mycursor2.fetchall()

resumen = False
resumenCount = 0

for row in myresultPid:
    rowPid = row[0]
    rowPname = row[1]
    rowPurl = row[2]
    rowCdiscount = row[3]
    priceAverage = 1.0
    priceBest = 0.0
    priceWorst = 0.0
    priceNewest = 0.0
    #umbral es el valor del producto al cual estoy dispusto observar
    porcentajeDescuento = rowCdiscount

    mycursor2.execute(querys.get_select_get_newestprice(rowPid))
    cnewestPrice = mycursor2.fetchall()

    for rowPnewest in cnewestPrice:
        if rowPnewest[0] is not None:
            priceNewest = float(rowPnewest[0])

    if priceNewest != -1:

        mycursor2.execute(querys.get_select_get_priceAverage(rowPid))
        cPriceAverage = mycursor2.fetchall()

        mycursor2.execute(querys.get_select_get_bestprice(rowPid))
        cBestPrice = mycursor2.fetchall()

        mycursor2.execute(querys.get_select_get_worstprice(rowPid))
        cWorstPrice = mycursor2.fetchall()

        for rowPrice in cPriceAverage:
            if rowPrice[0] is not None:
                priceAverage = float(rowPrice[0])

        for rowPbest in cBestPrice:
            if rowPbest[0] is not None:
                priceBest = float(rowPbest[0])

        for rowPworst in cWorstPrice:
            if rowPworst[0] is not None:
                priceWorst = float(rowPworst[0])

        percentPrice = (priceNewest * 100 )/ priceAverage

        umbral = 100.0 - porcentajeDescuento
        priceDiscountPercent = 100.0 - percentPrice

        tempData = [str(rowPid),rowPname.encode('utf-8'),str(priceNewest),str(priceAverage),str(priceBest),str(priceWorst),str(percentPrice),str(int(priceDiscountPercent)),str(umbral),rowPurl]

        datacsv.append(tempData)
        printRow(tempData)
        resumen = printHighLightRow(tempData)

        if resumen:
            resumenCount += 1

if resumenCount != 0:
    print("")
    print("")
    print("Existen " + str(resumenCount) + " precios destacados")
    print("")
    print("")

#solo pruebas, no es necesario guardarlo en un csv
#header = ['id','name','newPrice','avgPrice','bestPrice','worstPrice', 'percentPrice','percentDiscountPrice','umbral']
#printcsv(header,datacsv)