from bs4 import BeautifulSoup
import requests
import math
from flask import Flask, render_template
import xlsxwriter as xl
app = Flask (__name__)



def excel_data():
    address = "C:\\Users\\Danish\\Desktop\\" + city + ".xlsx"
    Excel_file = xl.Workbook(address)
    Excel_sheet = Excel_file.add_worksheet(city)
    Excel_sheet_heading = speciality +  ' ' + 'in' + ' ' + city
    Excel_sheet.write(0,0,Excel_sheet_heading)
    for i in range(1,len(l)+1):
        Excel_sheet.write(i,0,l[i-1])
    Excel_file.close()


splitting = []
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
            excel_data()
            print(" Excel File is Created Successfully By The Name" + ' '+ city)

        # print(new_url)
        fetch(new_url)

def total_page(url):
    datas = requests.get(url)
    datas = BeautifulSoup(datas.text,'html.parser')
    #datas = datas.find_all("h1",class_="u-xx-large-font u-bold u-t-grey5") <---- i was using this previously
    datas = datas.find_all("p",class_="u-xx-large-font u-bold")  
    global l
    global splitting                               
    for i in datas:
        #print(i.text)    
        splitting = (i.text).split() 
    #print("Total number of Doctors :: ",splitting[0])   
    splitted = (int(splitting[0]))/10
    return math.ceil(splitted)

city = input("Enter the City Name : ")
doctor_type = list(map(str,input("Enter the type of Doctor : ").split()))

speciality = ''
for i in doctor_type:
    speciality = speciality + i + ' '


len_list = len(doctor_type) - 1
str1 = 'https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22'
for i in doctor_type:
    str1 = str1 + i
    if (len_list) :
        str1 = str1 + '%20'
        len_list = len_list - 1
url = str1 + '%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=' + city 
l = []
# url = "https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={}".format(doctor_type,city)
print("Total no of Pages : ",total_page(url))
print("Total number of Doctors : ",splitting[0])
url_generator(url,total_page(url))


@app.route('/')
# def index():
#     return render_template("index.html")
# @app.route('/about') 
def about():
    return render_template("about.html", city = city, Doctors = speciality ,items = l)

if __name__=="__main__":
    app.run()
