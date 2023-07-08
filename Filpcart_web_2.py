import requests
from bs4 import BeautifulSoup
import pandas as pd
page_number=int(input("Enter number of pages:"))
phn_name=[]
phn_price=[]
phn_decs=[]
'''
for iphone product
https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy%2C4io&page=1
'''
for i in range(1,page_number+1):
    url="https://www.flipkart.com/laptops/~laptops-under-rs50000/pr?sid=6bo%2Cb5g&page="+str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.text,'html.parser')
    name=content.find_all('div',{'class':'_4rR01T'})
    price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
    desc=content.find_all('ul',{'class':'_1xgFaf'})
    print(len(name))
    print(len(price))
    print(len(desc))
    for i in name:
        phn_name.append(i.text)
    for i in price:
        phn_price.append(i.text)
    for i in desc:
        phn_decs.append(i.text)
data={'laptop name':phn_name,'laptop price':phn_price,'laptop ratings':phn_decs}
df=pd.DataFrame(data)
df.to_csv("laptop_products_under50000.csv")


