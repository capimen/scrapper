import ProductHistoricalInfoHelper



class ProductHistoricalInfo:

    def __init__(self, product, url, commerce, idCommerce, priceAverage, priceBest, priceWorst, priceNewest):

        self.product = product
        self.commerce = commerce
        self.idCommerce = idCommerce
        self.url = url
        self.umbral = 100 - product.discount
        self.priceAverage = priceAverage
        self.priceBest = priceBest
        self.priceWorst = priceWorst
        self.priceNewest = priceNewest

        self.fillerInfo()

        self.percentPrice = (self.priceNewest * 100 )/ self.priceAverage
        self.priceDiscountPercent = 100.0 - self.percentPrice
        self.historicalBestFlag = False
        self.umbralFlag = False
        self.hasStock = True
        if self.priceNewest == 0.0 :
            self.hasStock = False
        self.umbral_priceReference = False


    def fillerInfo(self):

        ProductHistoricalInfoHelper.fillerNewestPrice(self)

        if self.priceNewest != -1:

            ProductHistoricalInfoHelper.fillerBestPrice(self)
            ProductHistoricalInfoHelper.fillerAveragePrice(self)
            ProductHistoricalInfoHelper.fillerWorstPrice(self)

##################
##SQL FUNCTIONS###
##################
    def insertComparator(self):

        ProductHistoricalInfoHelper.isHistoricalBest(self)
        ProductHistoricalInfoHelper.isUmbral(self)
        ProductHistoricalInfoHelper.isUmbralReferencePrice(self)
        ProductHistoricalInfoHelper.validateUmbalsByStock(self)
        ProductHistoricalInfoHelper.insertComparator(self)




    def truncateComparator():

        ProductHistoricalInfoHelper.truncateComparator()

###################
#CONSOLE SHOW INFO#
###################

    def printInfo(self):
        print("---------------" + self.commerce + "---------------")
        #print("i  = " + str(self.id))
        #print("n  = " + self.name)
        #print("c  = " + self.categoryName)
        #print("r  = " + str(self.referencePrice))
        print("w  = " + str(self.priceNewest))
        print("a  = " + str(self.priceAverage))
        print("b  = " + str(self.priceBest))
        print("u  = " + str(self.priceWorst))
        print("%  = " + str(self.percentPrice) + "%")
        print("-% = " + str(self.priceDiscountPercent) + "%")


    def printHighLightInfo(self, origen):

        if self.priceNewest == 0.0:

            print("Estado: Producto Agotado")
            return False

        else:

            if ProductHistoricalInfoHelper.isUmbral(self) or ProductHistoricalInfoHelper.isLessReferencePrice(self):

                #print("")
                #print("")
                #print("")
                print("------------------------- DESTACADO --------------------------------")
                print("--------------------- "+ origen +" ------------------------")
                print("Nombre       : " + self.product.name)
                print("Categoria    : " + self.product.categoryName)
                print("Precio ref   : " + str(self.product.referencePrice))
                print("Precio nuevo : " + str(self.priceNewest))
                print("Precio mejor : " + str(self.priceBest))
                print("Precio peor  : " + str(self.priceWorst))
                print("Precio avg   : " + str(self.priceAverage))
                print("Descuento    : " + str(self.priceDiscountPercent) + "%")
                print("Ahorro prom  : " + str(int(self.priceAverage) - int(self.priceNewest)))
                print("Ahorro worst : " + str(int(self.priceWorst) - int(self.priceNewest)))
                print("Diff mejor   : " + str(int(self.priceBest) - int(self.priceNewest)))
                print("URL          : " + self.url)

                if ProductHistoricalInfoHelper.isHistoricalBest(self) :
                    print("")
                    print("MEJOR PRECIO HISTORICO!!!!")
                    print("")
                print("-------------------------------------------------")
                print("-------------------------------------------------")
                #print("")
                #print("")
                #print("")

                return True