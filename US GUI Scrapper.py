from tkinter import *
import tkinter as tk
import os
import random
import threading
from bs4 import BeautifulSoup as bs
import re
import csv
from bs4 import BeautifulSoup,SoupStrainer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32gui, win32con
import time
import pandas as pd
from phone_gen import PhoneNumber

#!------------------- To run in the background --------------------------
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
def command():
    global root
    global links
    global T
    root = tk.Tk()
    tk.Scrollbar(root)
    root.geometry("450x300")
    root.title("                      Account Login                                       .......................")
    links = StringVar()
    T = tk.Text(root, height=4, width=50)
    T.pack()
    Button(root, text="Scrap", width=10, height=1, command =  scrap).pack()
    Button(root, text="Back", width=10, height=1, command = back).pack()
    Label(root, text = "").pack()
    tk.mainloop()
def scrap():
    global link    
    link = T.get("1.0","end")
    setUp()
def setUp():
    global root
    Label(root, text = "Wait data is scrapping").pack()
    chrome_options = webdriver.ChromeOptions()  
    chrome_options.add_argument('headless')   
    driver = webdriver.Chrome(options = chrome_options, service_args=["hide_console"]) 
    # driver = webdriver.Chrome()
#!-------------------login-------------------------------------------------
    driver.get("https://www.linkedin.com/uas/login")
    time.sleep(2)
    emaile = driver.find_element_by_id("username")
    emaile.send_keys(username1)
    password = driver.find_element_by_id("password")
    password.send_keys(pasword1)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(8)
    try:    
        driver.find_element_by_name("pin")
        Label(root,text=("your linkedin blocked please verify the pin in incgnito!")).pack()
    except:
        names = []
        links = []
        phones = []
        emails = []
        adressess = []
        companies = []
        countries = []
        position=[]
        birth=[]
        websites=[]
        twitter=[]
        gradu=[]
        link_array = []
        link_array = link.split()        
        print(len(link_array))
        print(link_array)
        
        for i in range(len(link_array)):       
            url = driver.get(link_array[i])
            contact_page = bs(driver.page_source, features="html.parser")
            try:
                country = contact_page.select(
                    "div.flex-1.mr5 > ul.pv-top-card--list.pv-top-card--list-bullet.mt1 > li.t-16.t-black.t-normal.inline-block")
                print(country)
                if len(country) == 0:
                    country = "not found"
                    countries.append(country.strip())
                else:
                    for c in country:
                        cont = c.text.replace('\n', " ")
                        print("link",profile)
                        countries.append(cont.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                countries.append("Not Found")
            try:
                pos = contact_page.select(
                    "div.ph5.pb5 > div.display-flex.mt2 > div.flex-1.mr5 > h2")
                if len(pos) == 0:
                    pos = "not found"
                    position.append(pos.strip())
                else:
                    for pp in pos:
                        cont = pp.text.replace('\n', " ")
                        print("link",profile)
                        position.append(cont.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                    position.append("Not Found")
            try:
                company = contact_page.find_all('ul',attrs= {'class': 'pv-top-card--experience-list'})
                if len(company) == 0:
                    compan = "not found"
                    companies.append(compan.strip())
                else:
                    for cp in company:
                        compp = cp.text.replace('\n'," ")
                        print("link",profile)
                        companies.append(compp.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                companies.append("Not Found")
            driver.get(link_array[i] + "detail/contact-info/")
            driver.implicitly_wait(3)
            contact_page = bs(driver.page_source, features="html.parser")  
#! ------------------------------------ graduation --------------------------------
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 700)")
            time.sleep(3)
            driver.execute_script("window.scrollTo(700, 1200)")
            time.sleep(3)
            src = driver.page_source
            soup = BeautifulSoup(src, 'html.parser')
            try:
                edu_section = soup.find('section', {'id': 'education-section'}).find('ul')
                # print(edu_section)
                degree_year = \
                edu_section.find('p', {'class': 'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[
                    1].get_text().strip()

                print(degree_year)
                print("length", len(degree_year))
                if len(degree_year) == 0:
                    gd = "not found"
                    gradu.append(gd.strip())
                else:
                    print("herre")
                    grd = degree_year
                    # print("Phone", phon)
                    gradu.append(grd.strip())
                    time.sleep(2)
            except:
                print("grad not found")
                gradu.append("Not Found")
            driver.get(link_array[i]+"detail/contact-info/")
            driver.implicitly_wait(3)
            contact_page = bs(driver.page_source, features="html.parser")

#! ----------------Scrape Profile Links-------------------------
            try:
                profileLink=contact_page.select("div > section.pv-contact-info__contact-type.ci-vanity-url > div > a")
                if len(profileLink)==0:
                    profile="not found"
                    links.append(profile.strip())
                else:
                    for pl in profileLink:
                        profile = pl.text.replace('\n'," ")
                        # print("link",profile)
                        links.append(profile.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                link.append("Not Found")
#! -----------------Scrape Name--------------------------------
            try:
                name = contact_page.find_all('h1', attrs={'id': 'pv-contact-info'})
                if len(name)==0:
                    namee="not found"
                    
                    names.append(namee.strip())
                else:
                    for n in name:
                        namee = n.text.replace('\n'," ")
                        print("name",namee)
                        first = namee.split()
                        names.append(namee.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                print("name not found")

#! ---------------------------Scrape Email-----------------------------------
            try:
                email = contact_page.find_all('a', href=re.compile("mailto"))
                if len(email)==0:
                    emaill="not found"
                    emails.append(emaill.strip())
                else:
                    for e in email:
                        emaill=e.text.replace('\n'," ")
                        print("email",emaill)
                        emails.append(emaill.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                print("email not found")

#!---------------------------Bday---------
            try:
                bday = contact_page.select("div > section.pv-contact-info__contact-type.ci-birthday > div > span")
                if len(bday) == 0:
                    b = "not found"
                    birth.append(b.strip())
                else:
                    for b in bday:
                        bb = b.text.replace('\n', " ")
                        print("email",emaill)
                        birth.append(bb.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                birth.append("Not Found")

#! -----------------------------Scrape Phone-------------------------------------
            try:
                phone = contact_page.find_all('span', attrs ={'class': 't-14 t-black t-normal'})

                if len(phone) ==0:
                    phon="not found"
                    phones.append(phon.strip())
                else:
                    for ph in phone:
                        phon = ph.text.replace('\n'," ")
                        print("Phone", phon)
                        phones.append(phon)
                    time.sleep(random.uniform(0.5, 1.9))
            except:
                print("phone not found")
            # -------------------------------Scrape Address----------------------------------
            try:
                
                address=contact_page.select("div > section.pv-contact-info__contact-type.ci-address > div > a")
                if len(address)==0:                   
                    adrs="not found"
                    adressess.append(adrs.strip())

                else:
                    for ad in address:
                        adrs=ad.text.replace('\n'," ")
                        print("Address",adrs)
                        adressess.append(adrs.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:                
                print(" adress not found")
                
#!------------------ websites ----------------
            try:           
                websitee = contact_page.select("div > section.pv-contact-info__contact-type.ci-websites > ul")
            # websitee=contact_page.find_all('a', {'class': "list-style-none"})

                if len(websitee)==0:                             
                    web="not found"
                    websites.append(web.strip())

                else:
                    for wb in websitee:
                        web=wb.text.replace('\n'," ")
                        # print("Address",adrs)
                        websites.append(web.strip())
                    time.sleep(random.uniform(0.5, 1.9))
            except:           
                websites.append("Not Found")
#! ---------------------------twitter-----------
        try:
            
            twiter = contact_page.select("div > section.pv-contact-info__contact-type.ci-twitter > ul > li > a")
            # print("teeeeeeeeeeeeeeeeeeeee",twiter)
            if len(twiter) ==0:
                twi="Not Found"
                twitter.append(twi.strip())
            else:
                for tw in twiter:
                    twi = (tw.text.replace('\n'," "))
                    # print("Phone", phon)
                    twitter.append("https://twitter.com/"+twi.strip())
                time.sleep(random.uniform(0.5, 1.9))
        except:
            twitter.append("Not Found")
            
        # tdf.to_csv('data.csv' , mode = 'a' , header = False , index = False)
        driver.quit()
#!------- ----------                   --------------------
        result = "not found"                
        for i in range(len(names)):    
            if str(phones[i]) == result and countries[i] !=result:
                full_name = names [i]
                first = full_name.split()
                name = first[0]+"-"+first[-1]
                city = countries[i]
                count = []
                count = city.split(",")
                city = count[0]
                state = count[len(count)-1]
                chrome_options = webdriver.ChromeOptions()  
                chrome_options.add_argument('headless')   
                driver = webdriver.Chrome(options = chrome_options, service_args=["hide_console"]) 
                cook = True
                time.sleep(5)
                driver.get("https://www.usphonebook.com/"+name+"/"+city+"/"+state)
                i = 0
                while(cook == True):        
                    try:
                        print("enter try chrome")
                        time.sleep(5)
                        driver.find_element_by_class_name("g-recaptcha-response")
                        print("recaptca avlble")
                        driver.delete_all_cookies()
                        time.sleep(3)
                        driver.refresh()
                        cook = True
                        i = i+1
                    except :
                        print("enter except chrome")
                        cook = False              
                    if(i==3):
                        driver.quit()
                        break
                if(cook == True):
                        
                    driver = webdriver.Edge(executable_path  = 'C:\\Users\\user\\Desktop\\scrapping\\msedgedriver.exe')
                    time.sleep(5)
                    driver.delete_all_cookies()
                    driver.refresh()
                    driver.get("https://www.usphonebook.com/"+"alex-smith"+"/"+"alabama"+"/"+"albama")
                    j = 0
                    while(cook):       
                        try:  
                            print("enter try edge")
                            time.sleep(3)
                            driver.find_element_by_class_name("g-recaptcha-response")
                            cook = True
                            time.sleep(3)
                            print("Captcha availble")
                            driver.delete_all_cookies()
                            driver.refresh()
                            cook = True
                            j = j+1                    
                        except :
                            print("Enter except edge")
                            cook = False
                        if(j==3):
                            driver.quit()                   
                            break
                if cook == True:
                    print("captcha not passed")
                else:            
                    driver.maximize_window()
                    time.sleep(5)
                    try:                    
                        driver.find_element_by_xpath("//div[2]/div/div/div/a/span").click()
                        numb = driver.find_element_by_class_name( "ls_success-blue-link").get_attribute('href')
                        numb = (numb.split('/')[-1])
                        phones[i] = numb.replace("-","")
                    except :
                        pn = (PhoneNumber('US').get_number())
                        phones[i] = pn.replace("+1","")
                    try:               
                        adr = driver.find_element_by_class_name( "ls_contacts__text").text
                        adr = adr.strip()
                        adressess[i] = adr      
                        driver.quit()
                    except :
                        driver.quit()
            else:
                pass
#!-------------------------- CSV --------------------------------
        data=[links,names,emails,phones,adressess,countries,position,companies,birth,websites,twitter,gradu]
        df=pd.DataFrame(data, index=['Link','Name','Email','Phone','Address','City/ State/ Country','Position','Company','Birthday','Website','Twitter','Graduation'])
        tdf=df.T
        tdf.reset_index(drop=True)
        tdf.to_csv('webs1.csv', mode = 'a', header = False)
        driver.quit()
        Label(root, text = "Data scrapped").pack()
def back():
    root.destroy()
    main_account_screen()

    
def login_verify():
    global username1
    global pasword1

    username1 = username_verify.get()
    pasword1 = password_verify.get()
    if len(username1) < 10 or len(pasword1) < 4:
        print("if state")
        Label(main_screen, text = "please enter the password and email").pack()
    else:
        print("entered")
        Label(main_screen, text = "Wait verifying the password and mail!").pack()
        print(username1)
        print(pasword1)
        login_check()

        if pas == True and ml == True:
            driver.quit()
            main_screen.destroy()
            command()
        else:
            driver.quit()
            Label(main_screen, text = "wrong mail or password:").pack()

#! main_screen----

def main_account_screen():
    global main_screen
    global username_verify
    global password_verify
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login                        ....")   
    username_verify = StringVar()
    password_verify = StringVar()    
    Label(main_screen, text="Username * ").pack()
    username_login_entry = Entry(main_screen, textvariable = username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password *").pack()
    password_login_entry = Entry(main_screen, textvariable = password_verify)
    password_login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command = lambda: login_verify()).pack()
# threading.Thread(target = login_verify).start
    main_screen.mainloop()
def login_check():
    global pas
    global ml
    global driver    
    chrome_options = webdriver.ChromeOptions()  
    chrome_options.add_argument('headless')   
    driver = webdriver.Chrome(options = chrome_options, service_args=["hide_console"])   
#-------------------login-------------------------------------------------
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    emaile = driver.find_element_by_id("username")
    emaile.send_keys(username1)
    password = driver.find_element_by_id("password")
    password.send_keys(pasword1)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(2)
    try:
        driver.find_element_by_id("error-for-password")
        pas = False
        print("password error")
        driver.quit()
    except:
        pas = True
        print("pas ok")
    try:
        driver.find_element_by_id("error-for-username")
        ml = False
        driver.quit()
        print("user error")  
    except:
        print("user ok")
        ml = True              
main_account_screen()
