from SqlHelper import SqlHelper

def fillerNewestPrice(productHistoricalInfo):

    sqlHelper = SqlHelper()
    cnewestPrice = sqlHelper.select_get_newestprice(productHistoricalInfo.product.id, productHistoricalInfo.idCommerce)

    for rowPnewest in cnewestPrice:

        if rowPnewest[0] is not None:

            productHistoricalInfo.priceNewest = float(rowPnewest[0])



def fillerAveragePrice(productHistoricalInfo):

    sqlHelper = SqlHelper()
    cPriceAverage = sqlHelper.select_get_priceAverage(productHistoricalInfo.product.id, productHistoricalInfo.idCommerce)

    for rowPrice in cPriceAverage:

        if rowPrice[0] is not None:

            productHistoricalInfo.priceAverage = float(rowPrice[0])



def fillerBestPrice(productHistoricalInfo):

    sqlHelper = SqlHelper()
    cPriceBest = sqlHelper.select_get_bestprice(productHistoricalInfo.product.id, productHistoricalInfo.idCommerce)

    for rowPbest in cPriceBest:

        if rowPbest[0] is not None:

            productHistoricalInfo.priceBest = float(rowPbest[0])



def fillerWorstPrice(productHistoricalInfo):

    sqlHelper = SqlHelper()
    cWorstPrice = sqlHelper.select_get_worstprice(productHistoricalInfo.product.id, productHistoricalInfo.idCommerce)

    for rowPworst in cWorstPrice:

        if rowPworst[0] is not None:

            productHistoricalInfo.priceWorst = float(rowPworst[0])



def isHistoricalBest(productHistoricalInfo):

    if (int(productHistoricalInfo.priceNewest) < int(productHistoricalInfo.priceBest)):

        productHistoricalInfo.historicalBestFlag = True

    return productHistoricalInfo.historicalBestFlag




def isUmbral(productHistoricalInfo):

    if productHistoricalInfo.percentPrice < productHistoricalInfo.umbral:

        productHistoricalInfo.umbralFlag = True

    return productHistoricalInfo.umbralFlag


def isLessReferencePrice(productHistoricalInfo):

    if productHistoricalInfo.priceNewest < productHistoricalInfo.product.referencePrice:

        productHistoricalInfo.umbralFlag = True

    return productHistoricalInfo.umbralFlag



def insertComparator(productHistoricalInfo):

    sqlHelper = SqlHelper()
    sqlHelper.insert_comparator(productHistoricalInfo)



def truncateComparator():

    sqlHelper = SqlHelper()
    sqlHelper.truncate_comparator()