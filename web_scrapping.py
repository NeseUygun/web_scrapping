#Import required library
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

#Find the url you want to scrap the data
#I choosed flipkart webpage url (https://www.flipkart.com/)

#Find out the data that you want to extract from that page. I picked up iphone7 product.
string = "iphone7"
flipkart_url = "https://www.flipkart.com/search?q="+string
flipkart_url

#get the html content 
uclient = uReq(flipkart_url)
#read the html content 
flipcardpage = uclient.read()
flipkard_html = bs(flipcardpage, "html.parser")

# after getting html content, now from this content I want to scrap the particular data(iphone7) via beatiful soap 
# by typing data html adres
bigboxes=flipkard_html.findAll("div", {"class":"_1AtVbE col-12-12"})
del bigboxes[0:3]
box = bigboxes[0]

#get the product link by navigating html adress(box.div.div.div.a["href"])
product_link = "https://www.flipkart.com"+box.div.div.div.a["href"]
#return the status code
prodres = requests.get(product_link)
prodres.encoding = "utf-8"
prod_html = bs(prodres.text, "html.parser")

comment_boxes = prod_html.find_all("div", {"class": "_16PBlm"})
# extract the users name from the web page
comment_boxes[0].div.div.find_all("p", {"class":"_2sc7ZR _2V5EHH"})[0].text
# extract the rating that users gave the product from the web page
comment_boxes[0].div.div.div.div.text
# extract the user review from the web page
comment_boxes[0].div.div.div.p.text

#getting all user name, users rating and user review via for loop from the web page
for i in range(len(comment_boxes)-1):
    print(comment_boxes[i].div.div.find_all("p", {"class":"_2sc7ZR _2V5EHH"})[0].text)
    print(comment_boxes[i].div.div.div.div.text)
    print(comment_boxes[i].div.div.div.p.text)
    print()

