from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.shazamcomics.cl/pluto-tomo-1'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#containers_text = page_soup.findAll("div",{"datos"})

containers_text = page_soup.find("meta", property='product:original_price:amount')
print(containers_text["content"])


containers_text = page_soup.find("meta", property='og:title')
print(containers_text["content"])

#contain_text = containers_text[0]
#print(contain_text.h1.text)

#containers = page_soup.findAll("p",{"precioAhora"})
#contain = containers[0]
#valor = contain.span.text.strip()
#print("valor= "+valor)
