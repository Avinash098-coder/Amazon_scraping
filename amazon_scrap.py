import pandas as pd
from bs4 import BeautifulSoup
import requests
    
product_url=[]
product_name = []
cost = []
rating = []
discription = []
for i in range(2,22):
    url ="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"+str(i)
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text,"lxml")
    box = soup.find("div",class_="sg-col-inner")


    

    names = box.find_all("span",class_="a-size-medium a-color-base a-text-normal")
    #print(names)
    #print(len(names))

    for i in names:
        name = i.text
        product_name.append(name)
    print(product_name)
    print(len(product_name))
    
    money = box.find_all("span",class_= "a-price-whole")
    
    for i in money:
        name = i.text
        cost.append(name)
    print(cost)
    
    reviwes = box.find_all("span",class_="a-size-base puis-normal-weight-text")
    for i in reviwes:
        name = i.text
        rating.append(name)
    print(rating)
    print(len(rating))
    
    specification = box.find_all("div", class_="a-section a-spacing-medium a-spacing-top-small")
    for i in specification:
        name = i.text
        discription.append(name)
    print(discription)
    print(len(discription))
    
df = pd.DataFrame({"Product Name":product_name,"Rating":rating,"Discription":discription})
#print(df)

df.to_csv("Amazon Bags")














    


