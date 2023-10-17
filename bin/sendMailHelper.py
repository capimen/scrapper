from SqlHelper import SqlHelper


def get_highlight():

    sqlHelper = SqlHelper()
    cHighlight = sqlHelper.select_highlight_by_user('gustavo')

    for row in cHighlight:

        print("producto destacado para el usuario: " + str(row[2]))



def get_HTMLHighLight(user):

    sqlHelper = SqlHelper()
    cHighlight = sqlHelper.select_highlight_by_user(user)

    HTMLHeader = "    <!DOCTYPE html> " \
                "    <html> " \
                "    <head> " \
                "       <title>Correo HTML</title> " \
                " " \
                "    </head> " \
                "    <body> " \
                "        <div style=\"text-align: center; font-size: 18px;\"> " \
                "            <p>¡Hola!</p> " \
                "            <p>Estos son los libros que estan con descuentos para tí</p> " \
                "        </div> " \
                "                                                      " \
                "       <table border=\"1\" cellspacing=\"0\" cellpadding=\"10\" align=\"center\" style=\"margin: 0 auto;\"> " \
                "            <thead> " \
                "                <tr> " \
                "                    <th>Nombre</th> " \
                "                    <th>nuevo precio</th> " \
                "                    <th>Menor precio historico</th> " \
                "                    <th>Precio Promedio</th> " \
                "                    <th>Precio de referencia</th> " \
                "                    <th>tipo de umbral</th> " \
                "                </tr> " \
                "            </thead> " \
                "            <tbody> " \


    HTMLTableData = ""

    for row in cHighlight:

        HTMLTableData = HTMLTableData + "                <tr> "
        HTMLTableData = HTMLTableData + "                    <td> <a href=\""+ str(row[12])+"\"> " + row[2] +" </a></td> "  #nombre
        HTMLTableData = HTMLTableData + "                    <td> " + str(row[3]) + " </td> " #precio nuevo
        HTMLTableData = HTMLTableData + "                    <td> " + str(row[5]) + " </td> " #mejor precio historico
        HTMLTableData = HTMLTableData + "                    <td> " + str(row[4]) + " </td> " #precio Promedio
        if row[5] == 1 :
            HTMLTableData = HTMLTableData + "                    <td> " + "sin dato" " </td> " #Precio de referencia
        else:
            HTMLTableData = HTMLTableData + "                    <td> " + str(row[19]) + " </td> " #Precio de referencia

        HTMLTableData =  HTMLTableData + "                    <td> "

        if row[15] == 1:
            HTMLTableData = HTMLTableData + " - umbral de porcentaje "

        if row[17] == 1:
            HTMLTableData = HTMLTableData + " - umbral de precio "

        if row[13] is True:
            HTMLTableData = HTMLTableData + " - mejor precio historico "

        HTMLTableData =  HTMLTableData + "                    <td> "
        HTMLTableData =  HTMLTableData + "                </tr> "

    if HTMLTableData == "":
        return None

    HTMLFooter =                "            </tbody> " \
                 "        </table> " \
                 " " \
                 "          <div style=\"text-align: center; font-size: 18px;\"> " \
                 "            <p>Gracias por revisar este ejemplo.</p> " \
                 "        </div> " \
                 "    </body> " \
                 "    </html> "

    HTML = HTMLHeader + HTMLTableData + HTMLFooter

    return HTML


