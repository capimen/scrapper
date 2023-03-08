
# 0 str(rowPid)
# 1 rowPname.encode('utf-8')
# 2 str(priceNewest)
# 3 str(priceAverage)
# 4 str(priceBest)
# 5 str(priceWorst)
# 6 str(percentPrice)
# 7 str(int(priceDiscountPercent))
# 8 str(umbral)
# 9 Purl]


Pid = ""
Pname = ""
priceNewest = ""
priceAverage = ""
priceBest = ""
priceWorst = ""
percentPrice = ""
priceDiscountPercent = ""
umbral = ""
Purl = ""

def fillVariableFromData(data):

    global Pid
    global Pname
    global priceNewest
    global priceAverage
    global priceBest
    global priceWorst
    global percentPrice
    global priceDiscountPercent
    global umbral
    global Purl

    Pid = data[0]
    Pname = data[1]
    priceNewest = data[2]
    priceAverage = data[3]
    priceBest = data[4]
    priceWorst = data[5]
    percentPrice = data[6]
    priceDiscountPercent = data[7]
    umbral = data[8]
    Purl = data[9]

def printRow(data):

    fillVariableFromData(data)

    print("--------------------------------")
    print("i  = " + Pid)
    print("n  = " + Pname)
    print("w  = " + priceNewest)
    print("a  = " + priceAverage)
    print("b  = " + priceBest)
    print("u  = " + priceWorst)
    print("%  = " + percentPrice + "%")
    print("-% = " + priceDiscountPercent + "%")

def printHighLightRow(data):

    floatPriceNewest = float(priceNewest)
    if floatPriceNewest == 0.0:

        print("Estado: Producto Agotado")
        return False

    else:

        if float(percentPrice) < float(umbral):

            print("")
            print("")
            print("")
            print("-------------------------------------------------")
            print("-------------------------------------------------")
            print("Destacado: " + Pname)
            print("precio nuevo : " + priceNewest)
            print("precio mejor : " + priceBest)
            print("precio peor  : " + priceWorst)
            print("precio avg   : " + priceAverage)
            print("descuento    : " + priceDiscountPercent + "%")
            print("ahorro prom  : " + str(int(priceAverage) - int(priceNewest)))
            print("ahorro worst : " + str(int(priceWorst) - int(priceNewest)))
            print("diff mejor   : " + str(int(priceNewest) - int(priceNewest)))
            print("url: " + Purl)
            if (int(priceNewest) - int(priceNewest)) == 0:
                print("")
                print("MEJOR PRECIO HISTORICO!!!!")
                print("")
            print("-------------------------------------------------")
            print("-------------------------------------------------")
            print("")
            print("")
            print("")

            return True