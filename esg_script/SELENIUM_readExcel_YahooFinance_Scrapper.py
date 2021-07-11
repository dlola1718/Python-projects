from selenium import webdriver
import time
import os.path
from os import path
import hashlib
import pandas as pd 
 

# web driver directory 
drvPath = "/Users/damiijiwola/Documents/REPLY CHALLENGES/softwares/chromedriver"


# set incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(drvPath, options=chrome_options)
# my url
browser.get("https://uk.finance.yahoo.com/")


# use ticker symbol as index column



data = pd.read_excel('check_tickers.xlsx', index_col=0, header =0)


# PAUSED
##################################################################################################
#open file excel [a - append, o - opens new file, ]  first check if file exists
# fname="ESG_Ratings_YahooFinance.csv"

# FileExist = 1
# if not path.exists(fname):
#     FileExist = 0
    
# f = open(fname, "a", encoding="utf-8")

# PAUSED
# if FileExist == 0:
#     f.write("    Total ESG risk score, Risk Level, Controversy Level Score, Controversy Level, Date   " )



##################################################################################################









##################################################################################################
# yahoo consent page & click
consent_buttton = browser.find_element_by_name('agree')
consent_buttton.click()


# find seearch bar
# search_bar = browser.find_element_by_id('yfin-usr-qry')
 

# for index, row in data.iterrows():      OR BELOW
for i in range(len(data)):
    # print(index)
    search_bar = browser.find_element_by_id('yfin-usr-qry')
    search_bar.send_keys(data.index[i])
    time.sleep(2)
    browser.find_element_by_id('search-button').click()
    

    # click on sustainability
    time.sleep(2)
    sustainability_button = browser.find_element_by_xpath("//span[contains(text(),'Sustainability')]")
    sustainability_button.click()
    # time.sleep(4)



    # extract sustainability rating [risk score, risk range, controversy level ]
    time.sleep(3)
    esg_risk_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    esg_risk = esg_risk_score.text
    # # print(esg_risk)

    data['ESG RISK SCORE'] = data.append(esg_risk)

    # data.concat([data.DataFrame([i], columns=['ESG RISK SCORE']) for i in range(4)],
    #       ignore_index=True)






    # esg_range_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]")
    # esg_range = esg_range_score.text
    # # print(esg_range)


    # esg_controversy_score = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
    # esg_controversy = esg_controversy_score.text
    # # print(esg_controversy)


    # esg_controversy_score_translation = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]")
    # controversy_translation = esg_controversy_score_translation.text
    # # print(controversy_translation)


    # last_updated_date = browser.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/section[1]/div[3]/span[2]/span[1]")
    # last_updated = last_updated_date.text
    # # print(last_updated)

    browser.back()
    # search_bar.clear()
    # browser.find_element_by_id('search-button').click()

# print(esg_risk)
 
print(data)
###################################################################################################
###################################################################################################




# import pandas as pd 




# print(data)


# # count rows.. for SYMBOLS
# print(len(data.index))
# for index, row in data.iterrows():
#     print(index)


 