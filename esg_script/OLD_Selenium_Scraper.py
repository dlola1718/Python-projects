from selenium import webdriver
import time
import os.path
from os import path
import pandas as pd 
 

# web driver directory 
drvPath = "/Users/damiijiwola/Documents/REPLY CHALLENGES/softwares/chromedriver"


# set incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(drvPath, options=chrome_options)
# my url
browser.get("https://uk.finance.yahoo.com/")





##################################################################################################
#open file excel [a - append, o - opens new file, ]  first check if file exists
fname="ESG_Ratings_YahooFinance.csv"

FileExist = 1
if not path.exists(fname):
    FileExist = 0
    
f = open(fname, "a", encoding="utf-8")

# PAUSED
# if FileExist == 0:
#     f.write("    Total ESG risk score, Risk Level, Controversy Level Score, Controversy Level, Date   " )



##################################################################################################









##################################################################################################
# yahoo consent page & click
consent_buttton = browser.find_element_by_name('agree')
consent_buttton.click()


# find seearch bar
search_bar = browser.find_element_by_id('yfin-usr-qry')
search_bar.send_keys("NVDA")
time.sleep(3)
browser.find_element_by_id('search-button').click()
 


# click on sustainability
time.sleep(2)
sustainability_button = browser.find_element_by_xpath("//span[contains(text(),'Sustainability')]")
sustainability_button.click()


# extract sustainability rating [risk score, risk range, controversy level ]
time.sleep(5)
esg_risk_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
esg_risk = esg_risk_score.text
# print(esg_risk)


esg_range_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]")
esg_range = esg_range_score.text
# print(esg_range)


esg_controversy_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
esg_controversy = esg_controversy_score.text
# print(esg_controversy)


esg_controversy_score_translation = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
controversy_translation = esg_controversy_score_translation.text
# print(controversy_translation)


last_updated_date = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[3]/span[2]/span[1]")
last_updated = last_updated_date.text
# print(last_updated)

# Sustainalytics’ controversies research identifies companies involved in incidents and events that may negatively affect stakeholders, the environment or the company’s operations. Controversies are rated on a scale from one to five, with five denoting the most serious controversies with the largest potential impact
# controversy_level = browser.find_element_by_id('')

##################################################################################################
##################################################################################################




##################################################################################################



# write to file [ \n - newline]
f.write("\n" + esg_risk + "," + esg_range  + "," + esg_controversy + "," + controversy_translation+ "," +  last_updated )




##################################################################################################





time.sleep(5)
browser.close()