from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv
import urllib

fb_url='https://www.facebook.com/groups/cookupsBD/'
filepath = 'html/cookups.html'

class FBScraper:

    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self,url,wlog):
        self.__url = url
        self.__wlog = wlog

    
    
    def write_webpage_as_html(self,filepath=filepath,data=''):                       # method for writing webpage as html
        try:
            driver = webdriver.Firefox(executable_path='D:\geckodriver-v0.22.0-win64/geckodriver.exe')
            driver.get(fb_url)
            sleep(60)
            html = driver.page_source
            driver.close()
            with open(filepath,'w+',encoding='utf-8') as fobj:
                if html:
                   fobj.write(html)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    
    def read_webpage_from_html(self,filepath=filepath):                               # method for reading webpage from html
        try:
            with open(filepath,'r',encoding='utf-8') as fobj:
                
                self.__data=fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    
    def convert_data_to_bs4(self):                                                    # method for converting data to beautiful soup
        
        self.__soup=BeautifulSoup(self.__data,'lxml')
        
         
                                   
    def parse_soup_to_csv(self):                                                      # method for parsing soup data to csv file
        
        post_list=self.__soup.find_all("div",class_='_4-u2 mbm _4mrt _5jmm _5pat _5v3q _4-u8',limit=10)

        cook_list=[]
        for item in post_list:
            cook = item.find("span",attrs={"class":"fwb"})
            cook_list.append(cook.text)
        
                   
        post_time_list=[]
        for item in post_list:
            post_time = item.find("span",attrs={"class":"timestampContent"})
            post_time_list.append(post_time.text)

        
        title_list=[]
        for item in post_list:
            title=item.find("div","div",class_='_l53')
            title_list.append(title.text)
        

        price_list=[]    
        for item in post_list:
            price = item.find("div","div",class_='_l57')
            price_list.append(price.text[1:])

        location_list=[]
        for item in post_list:
            loaction=item.find("div","div",class_='_l58')
            location_list.append(loaction.text)
         
        order_link_list=[]
        for item in post_list:
            order_link = item.find("div",class_="_5pbx userContent _3576")
            order_link_list.append(order_link.find("a",target="_blank").text)

        description_list=[]
        for item in post_list:
            element=item.find("div",class_="_5pbx userContent _3576")
            for description in element.find_all("p"):
                description_list.append(description.text)   
               
       


      
        zip_list=zip(cook_list,post_time_list,title_list,location_list,price_list,description_list,order_link_list)   # zip all list 
        with open('output_file.csv', 'w+',newline='',encoding='utf-8') as f:
            writer = csv.writer(f,delimiter=',', quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(['Cook Name','Time of Post','Title of Post','Cook Location','Price','Descriptions','Order Link','Image'])
            for row in zip_list:
                writer.writerow(row)
               

        with open('output_file.csv', 'r',newline='',encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC,)
            for row in csv_reader:
                print(type(row[4]))
        
        
        
            




