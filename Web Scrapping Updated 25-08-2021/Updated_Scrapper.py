from bs4 import BeautifulSoup
import requests
import math
from flask import Flask, render_template
app = Flask (__name__)

def fetch(url):
    Not_found=0
    Count = 0
    data = requests.get(url)
    plane_text = BeautifulSoup(data.text,'html.parser')
    Doctor_name = plane_text.find_all("h2",class_= "doctor-name")
    if(Doctor_name == []):
        Not_found = 1
    if Not_found == 0:
        for i in Doctor_name:
            l.append(i.text)
            # print(i.text)
   
    if(Not_found == 1):
        print("NOT!!! FOUND")

def url_generator(url,pages):
    old_url = url
    count_pages = 1
    for i in range(1,pages+1):
        new_url = old_url+"&page={}".format(i)
        count_pages = count_pages + 1
        if count_pages == pages:
            print("Fetching Process Successfully Completed")
        # print(new_url)
        fetch(new_url)

def total_page(url):
    datas = requests.get(url)
    datas = BeautifulSoup(datas.text,'html.parser')
    #datas = datas.find_all("h1",class_="u-xx-large-font u-bold u-t-grey5") <---- i was using this previously
    datas = datas.find_all("p",class_="u-xx-large-font u-bold")                                 
    for i in datas:
        #print(i.text)    
        splitting = (i.text).split() 
    print("Total number of Doctors : ",splitting[0])   
    splitted = (int(splitting[0]))/10
    return math.ceil(splitted)

city = input("Enter the City Name ")
doctor_type = input("Enter the type of Doctor ")
l = []
url = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={}".format(doctor_type,city)
print("Total no of Pages : ",total_page(url))
url_generator(url,total_page(url))


@app.route('/')
# def index():
#     return render_template("index.html")
# @app.route('/about') 
def about():
    return render_template("about.html", city = city, Doctors = doctor_type ,items = l)

if __name__=="__main__":
    app.run()
