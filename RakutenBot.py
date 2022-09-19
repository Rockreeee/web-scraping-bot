#注意点----------本番環境----------
#urlは正しいか
#購入確定ボタンはコメントアウトされていないか
#カゴはからか
#注意点----------本番環境----------
import time
import os

import chromedriver_binary
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class auto_order:
    def __init__(self, userdata_dir, password):
        print("----------------------RakutenBotStart--------------------------")
        print("   \|/          \|/       \|/         \|/      \|/       \|/   ")
        print("    |            |        \|/         \|/      \|/       \|/   ")
        print("    |    \/      |    //   |           |   \/   |/        |    ")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("■■■■■□□□□□□□□□□□□□■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□■□□□■□□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□■□□□□■□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□■□□□□■□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□■□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□■□□□□■□□□□■■■■□□□□■□□□□■□□■■□□□■■□□■■■■■■□□□□□■■■□□□□■■□■■■□□□")
        print("□■□□□■□□□□■□□□□■□□□■□□□■□□□□■□□□□■□□□□■□□□□□□□■□□□■□□□□■■□□□■□□")
        print("□■■■■□□□□□□□□□□■□□□■□□■□□□□□■□□□□■□□□□■□□□□□□■□□□□□■□□□■□□□□■□□")
        print("□■□□■□□□□□□■■■■■□□□■□■■□□□□□■□□□□■□□□□■□□□□□□■■■■■■■□□□■□□□□■□□")
        print("□■□□□■□□□□■□□□□■□□□■■□□■□□□□■□□□□■□□□□■□□□□□□■□□□□□□□□□■□□□□■□□")
        print("□■□□□■□□□■□□□□□■□□□■□□□■□□□□■□□□□■□□□□■□□□□□□■□□□□□□□□□■□□□□■□□")
        print("□■□□□■□□□■□□□□□■□□□■□□□□■□□□■□□□□■□□□□■□□□■□□■□□□□□■□□□■□□□□■□□")
        print("□■□□□□■□□■□□□□■■□□□■□□□□■□□□■□□□■■□□□□■□□□■□□□■□□□□■□□□■□□□□■□□")
        print("■■■□□□■■□□■■■■□■■□■■■□□□■■□□□■■■□□■□□□□■■■□□□□□■■■■□□□■■■□□■■■□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("   \|/          \|/       \|/         \|/      \|/       \|/   ")
        print("    |            |        \|/         \|/      \|/       \|/   ")
        print("    |    \/      |    //   |           |   \/   |/        |    ")
        print("----------------------RakutenBotStart--------------------------")
        self.userdata_dir = userdata_dir #ユーザープロファイル PATH
        self.password = password
        options = Options()
        options.add_argument('--user-data-dir=' + self.userdata_dir)
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def watch_start(self,url, interval = 300, lim = 1000, is_order = False):
        count = 0        
        while True:
            self.driver.get(url)
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            #カートに加えるボタン
            resOfAddToCartButton = self.driver.find_elements_by_class_name("new_addToCart")
            if len(resOfAddToCartButton) == 0:#ボタンが存在しない時
                print("not found 404")
            else:#ボタンが存在する時
                print("has been found")
                if is_order:
                    resOfAddToCartButton[0].click()
                    #購入手続きボタン
                    self.resOfProcedureForPurchasingButton()
                    #次へボタン
                    self.resOfNextButton()
                    #注文確定ボタン
                    # self.resOfConfirmTheOrderButton()
                    break
                    
            if count > lim:
                break

            time.sleep(interval)
            count += 1
            print("\nループ回数{0}".format(count))

    def resOfProcedureForPurchasingButton(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'js-cartBtn')))
            resOfProcedureForPurchasingButton = self.driver.find_elements_by_id('js-cartBtn')
            resOfProcedureForPurchasingButton[0].click()
        except:
            print("ご購入手続きボタンが表示されません。")
            self.driver.back()
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located)
            try:
                resOfAddToCartButton = self.driver.find_elements_by_class_name("new_addToCart")
                resOfAddToCartButton[0].click()
                return self.resOfProcedureForPurchasingButton()
            except:
                print("ご購入手続きボタンが消えた")
        
    def resOfNextButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located)
            resOfPasswordTextField = self.driver.find_elements_by_name("p")
            resOfPasswordTextField[0].send_keys(self.password)
            resOfNextButton = self.driver.find_elements_by_class_name('btn-red')
            resOfNextButton[0].click()
        except:
            print("次へボタンが表示されません。")
            self.driver.back()
            return self.resOfProcedureForPurchasingButton()
        
    def resOfConfirmTheOrderButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS＿NAME, 'btn-red')))
            resOfConfirmTheOrderButton = self.driver.find_elements_by_class_name("btn-red")
            resOfConfirmTheOrderButton[0].click()
        except:
            print("注文確定ボタンが表示されません。")
            self.driver.back()
            return self.resOfNextButton()

    def quit(self):
        self.driver.quit()
        

# In[実際に起動する]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ :
model = auto_order(userdata_dir = "/Users/*********/Desktop/Anaconda/ChromeForBot1",
                   password = "***********")
model.watch_start("https://books.rakuten.co.jp/rb/16462859/?bkts=1", 
                    interval = 10,
                    lim = 5000,
                    is_order = True)
model.quit()