#!/usr/bin/env python
# coding: utf-8

# In[105]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
browser = webdriver.Chrome()

# Now you can use `browser`
browser.get('https://www.jio.com/fiber')

browser.maximize_window()

wait = WebDriverWait(browser, 10)

links= WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//a[@parent-attr="JioFiber"]')))

links_list = []

for link in links:
    links_list.append(link.get_attribute('href'))

#     # Loop for extracting links from Tag Objects
# for link in links:
#         links_list.append(link.get('href'))
        



def info_scrape(info_xpath,info_list):
    heading = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, info_xpath)))
    for i in heading:
        print(i.text)
        info_list.append(i.text)
    return len(info)


def info_scrape_element(element, info_list):
    text = element.text
    info_list.append(text)
    return len(info_list)


def scrape_faq_answer(info_list):
    num_plus_symbols = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="j-accordion-panel-icn j-button j-button-size__medium tertiary icon-primary icon-only as-span"]'))))
    actions = ActionChains(browser)
    
    for i in range(num_plus_symbols):
        plus_symbols = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="j-accordion-panel-icn j-button j-button-size__medium tertiary icon-primary icon-only as-span"]')))
        if plus_symbols[i].is_displayed() and plus_symbols[i].is_enabled():
            actions.move_to_element(plus_symbols[i]).perform()
            plus_symbols[i].click()
            time.sleep(2)
            answer = info_scrape('//div[@class="j-accordion-panel-content j-text-body-xs"]', info_list)
            minus_symbol = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="j-accordion-panel-icn active j-button j-button-size__medium tertiary icon-primary icon-only as-span"]')))
            minus_symbol.click()
            time.sleep(2)    


#Discover page
browser.get(links_list[0])

info=[]
heading= info_scrape('//h3[@class="j-contentBlock__title j-heading j-text-heading-l"]', info)
heading2= info_scrape('//h2[@class="j-contentBlock__title j-heading j-text-heading-l"]', info)
smallheading= info_scrape('//div[@class="j-color-primary-grey-80 j-contentBlock__description j-text-body-m"]', info)
shortheading3= info_scrape('//h3[@class="j-contentBlock__title j-heading j-text-body-m-bold"]', info)
under_sh3= info_scrape('//h3[@class="j-contentBlock__title j-color-primary-grey-100 j-text-body-s-bold "]', info)
cardheading3= info_scrape('//div[@class="j-color-primary-grey-80 j-contentBlock__description j-text-body-m"]', info)
under_cardh3= info_scrape('//div[@class=" j-contentBlock__description  j-color-primary-grey-80 j-text-body-s"]', info)
card_info=info_scrape('//div[@class="j-card bg--primary-background size--s card-vertical  w-100"]', info)                             


# Prepaid page
browser.get(links_list[1])
content_elements= wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="j-container l-layout--full"]')))
content_element =content_elements[1]
content= info_scrape_element(content_element, info)
faq_ans=scrape_faq_answer(info)


#Postpaid Page
browser.get(links_list[2])
content_elements= wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="j-container l-layout--full"]')))
content_element =content_elements[1]
content= info_scrape_element(content_element, info)
faq_ans=scrape_faq_answer(info)


#Get Jio Fiber Page
browser.get(links_list[3])
faq_ques= info_scrape('//section[@class="faqSection_faqContainer__UiWC1 j-container"]', info)
faq_ans=scrape_faq_answer(info)


#Recharge Page
browser.get(links_list[4])
faq_ques= info_scrape('//section[@class="CustomFAQ_faqContainer__3Pf-t j-container"]', info)
faq_ans=scrape_faq_answer(info)


#Services Page
browser.get(links_list[6])
data= info_scrape('//div[@class="j-container sp--l pd--vertical"]', info)

with open('jiofiber.txt', 'w', encoding='utf-8') as f:
    for inf in info:
        f.write("%s\n" % inf)


# In[ ]:




