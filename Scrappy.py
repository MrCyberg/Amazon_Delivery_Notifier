import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/InfiZoneTM-HDMI-Switch-4K-Splitter/dp/B0815SR29H/ref=pd_rhf_gw_p_img_2?_encoding=UTF8&psc=1&refRID=VGTSS4RCWF4NYTBRXK9Y'

# URL = 'https://www.amazon.in/dp/B086GYPJW7/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=ZFTSS5A0EDFR4JWBQAHP&pf_rd_t=101&pf_rd_p=a4c75c43-317d-49bf-9597-594d50bd3413&pf_rd_i=21433333031'

headers =  {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

deliveryData = soup.find(disabled="disabled")

print(title.strip())

#print(deliveryData)

try:
    if(deliveryData.find('disabled="disabled"') != -1):
        confirmMessage = print("Product is Not Deliverable")
except:
    confirmMessage = print("Product is Deliverable")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Sender_Mail_ID', 'Your_App_Code')

    subject = 'Your Product Can be Delivered'
    body = 'Check out your product for delivery ' + URL

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail('Sender_Mail_ID', 'Receiver_Mail_ID', message)

    print("E-Mail Has Been Sent!!")

    server.quit()
