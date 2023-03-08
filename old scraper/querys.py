#scraper

select_init = "select   p.id, " \
               "        p.url, " \
               "        c.name, " \
               "        c.priceclass, " \
               "        c.pricetag, " \
               "        c.nameclass, " \
               "        c.nametag," \
              "         c.id " \
               "from    product p, " \
               "        commerce c " \
               "where   p.id_commerce = c.id "

def get_insert_historical(rowPid,valor):
    return "INSERT INTO `scraper`.`historical` " \
           "(" \
           "`id_product`," \
           "`price`" \
           ") " \
           "VALUES " \
           "(" \
           " "+ str(rowPid) +" , " \
           " "+ valor +" " \
           ");"

def get_update_product_name(productName,rowPid):
    return "UPDATE `scraper`.`product` " \
           "SET `name` = \""+ productName +"\" " \
           "WHERE `id` = "+str(rowPid)+";"


#Comparador
select_get_product = "select	p.id," \
                     "          p.name," \
                     "          p.url," \
                     "          c.discount " \
                     "from  	product p, " \
                     "          commerce c " \
                     "where     p.id_commerce = c.id"

def get_select_get_priceAverage(rowPid):
    return  "select 	avg(h.price) " \
            "from 	historical h " \
            "where 	id_product = " + str(rowPid)

def get_select_get_bestprice(rowPid):
    return "select 	h.price " \
            "from    historical h " \
            "where 	id_product = " + str(rowPid) + " " \
            "order by h.price " \
            "asc limit 1; "

def get_select_get_worstprice(rowPid):
    return "select h.price " \
           "from   historical h " \
           "where 	id_product = " + str(rowPid) + " " \
           "order by h.price " \
           "desc limit 1; "

def get_select_get_newestprice(rowPid):
    return "select 	h.price " \
           "from 	    historical h " \
           "where 	id_product = " + str(rowPid) + " " \
           "order by h.reg_date " \
           "desc limit 1; "