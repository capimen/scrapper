from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

# database connection configuration


mycursor.execute(querys.select_init)

myresult = mycursor.fetchall()

counter = 0
sites = []

print("excecuting:")

for row in myresult:

    #mapping to variables
    rowPid = row[0]
    rowPurl = row[1]
    rowCname =  row[2]
    rowCpriceclass = row[3]
    rowCpricetag = row[4]
    rowCNameclass = row[5]
    rowCNametag = row[6]
    rowCId = row[7]

    #getting html
    uClient = uReq(rowPurl)
    page_html = uClient.read()
    uClient.close()

    # html parser
    page_soup = soup(page_html, "html.parser")
    containers_title = page_soup.findAll(rowCNameclass, {rowCNametag})

    #getting product name
    productName = "No name"

    # getting product name Buscalibre
    if rowCId == 1:

        contain_title = containers_title[0]
        productName = contain_title.h1.text

    # getting product name Portal Inmobiliario
    if rowCId == 2:

        contain_title = containers_title[0]
        productName = contain_title.text.strip()

    #Site counting
    counter += 1
    sites_name_flag = True

    for sites_name in sites:

        if sites_name == rowCname:

            sites_name_flag = False

    if sites_name_flag:

        sites.append(rowCname)


    #getting product prices
    containers = page_soup.findAll(rowCpriceclass, {rowCpricetag})

    #valor -1 means "no stock"
    valor = "null"

    if (len(containers)):

        contain = containers[0]

        if rowCId == 1:

            #getting price Buscalibre
            valor = contain.span.text.strip()

        if rowCId == 2:

            # getting price Portal Inmobiliario
            valor = contain.text.strip()

        valor = valor.replace("$", "").strip();
        valor = valor.replace(".", "").strip();

    #just for test
    print(str(valor) + "\t..........\t"+ productName)

    insert_historical = "INSERT INTO `scraper`.`historical` " \
                        "(" \
                        "`id_product`," \
                        "`price`" \
                        ") " \
                        "VALUES " \
                        "(" \
                        " "+ str(rowPid) +" , " \
                        " "+ valor +" " \
                        ");"

    update_product_name = "UPDATE `scraper`.`product` " \
                          "SET `name` = \""+ productName +"\" " \
                        "WHERE `id` = "+str(rowPid)+";"

    #ejecutar este insert solo cuando hay link nuevo para cargar el nombre
    #mycursor.execute(querys.get_update_product_name)

    # comentado por pruebas
    mycursor.execute(querys.get_insert_historical(rowPid,valor))

    #comentado por pruebas
    mycursor.execute("commit;")

#comparador

print("Done!")
print("")
print("")
print("-------------------------")
print("---------RESUMEN---------")
print("-------------------------")
print("Links actualizados: "+str(counter))
print("Sitios revisados: ")
countsitesrow = 0

for siterow in sites:

    countsitesrow +=1
    print(str(countsitesrow)+".- "+siterow)

print("-----------------------")

