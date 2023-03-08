import csv
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def printcsv(header, data):

    print("")
    print("")
    print("data created in file .\\comparisons\\"+timestr + '.csv')

    with open("comparisons\\"+timestr + '.csv', 'wb') as newFile:

        cvs_writer = csv.writer(newFile, delimiter=';')
        cvs_writer.writerow(header)

        for line in data:

            cvs_writer.writerow(line)


def readcsv():

    print("")
    print("")
    print("reading file .\\conf\\products"  + '.csv')

    with open("conf\\products" + '.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:

            if line_count == 0:

                print("header" + row[0])
                line_count += 1

            else:

                print(row[0]+row[1]+row[2]+row[3]+row[4])
                line_count += 1


readcsv()