#NTT-X Store Bot For PS5
#カゴの中身はからか？
#サイトはps5か
#購入アウトコメントしたか
import time
import os

import chromedriver_binary
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class auto_order:
    def __init__(self, userdata_dir, mail, passwd):
        print("------------NTT-XStoreBotStart---------------")
        print(" \|/    \|/       \|/     \|/      \|/  \|/  ")
        print("  |      |        \|/     \|/      \|/  \|/  ")
        print("  |  \/  |    //   |       |   \/   |/   |   ")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("■□□□□■■■□■■■■■■■□□■■■■■■■□□□□□□□□□□□■■■□■■■□□")
        print("■■□□□□■□□■□□■□□■□□■□□■□□■□□□□□□□□□□□□■□□□■□□□")
        print("■□■□□□■□□■□□■□□■□□■□□■□□■□□□□□□□□□□□□■□□□■□□□")
        print("■□■□□□■□□□□□■□□□□□□□□■□□□□□□□□□□□□□□□□■□■□□□□")
        print("■□□■□□■□□□□□■□□□□□□□□■□□□□□□□□□□□□□□□□□■□□□□□")
        print("■□□■□□■□□□□□■□□□□□□□□■□□□□□■■■■■■■□□□□■□■□□□□")
        print("■□□□■□■□□□□□■□□□□□□□□■□□□□□□□□□□□□□□□□■□■□□□□")
        print("■□□□■□■□□□□□■□□□□□□□□■□□□□□□□□□□□□□□□■□□□■□□□")
        print("■□□□□■■□□□□□■□□□□□□□□■□□□□□□□□□□□□□□■□□□□□■□□")
        print("■■□□□□■□□□■■■■■□□□□■■■■■□□□□□□□□□□□□■■□□□■■□□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□□■■□■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□■□□■■□□□□□■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("■□□□□■□□□□□■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("■□□□□□□□□■■■■■■□□□□□■■■□□□□■■■□■■□□□□□■■■□□□□")
        print("□■■□□□□□□□□■□□□□□□□■□□□■□□□□□■■□□■□□□■□□□■□□□")
        print("□□□■■□□□□□□■□□□□□□■□□□□□■□□□□■□□□■□□■□□□□□■□□")
        print("□□□□□■□□□□□■□□□□□□■□□□□□■□□□□■□□□□□□■■■■■■■□□")
        print("■□□□□□■□□□□■□□□■□□■□□□□□■□□□□■□□□□□□■□□□□□■□□")
        print("■■□□□■□□□□□■□□□■□□□■□□□■□□□□□■□□□□□□□■□□□□■□□")
        print("■□■■■□□□□□□□■■■□□□□□■■■□□□□■■■■■■□□□□□■■■■□□□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print(" \|/    \|/      \|/     \|/      \|/   \|/  ")
        print("  |      |       \|/     \|/      \|/   \|/  ")
        print("  |   \/ |   //   |       |   \/   |/    |   ")
        print("------------NTT-XStoreBotStart---------------")
        self.userdata_dir = userdata_dir #ユーザープロファイル PATH
        self.mail = mail
        self.passwd = passwd
        options = Options()
        options.add_argument('--user-data-dir=' + self.userdata_dir)
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def watch_start(self,url, interval = 300, lim = 1000, is_order = False):
        count = 0
        while True:
            self.driver.get(url)
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            try:
                resOfAddToCartButton = self.driver.find_element_by_css_selector('#incontents > div.itemdetail > div.detail > div.cartarea > div > a')
                print("has been found")
                if is_order:
                    resOfAddToCartButton.click()
                    self.resOfToPurchaseProcedureButton()#購入手続きへボタン
                    self.resOfLoginView()
                    self.resOfPaymentMethodButton()#お支払い方法選択ボタン
                    self.resOfAgreeButton()#同意ボタン
                    self.resOfNextCartButton()#次のステップへ進む
                    #self.resOfCartBuyButton()#上記商品を購入するボタン
                    print("購入できた")
                    break
                
            except:
                print("not found 404")
                    
            if count > lim:
                break

            time.sleep(interval)
            count += 1
            print("\nループ回数{0}".format(count))
        
    def resOfToPurchaseProcedureButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btnConversion")))
            resOfToPurchaseProcedureButton = self.driver.find_elements_by_class_name("btnConversion")#購入手続きへボタン
            resOfToPurchaseProcedureButton[0].click()
        except:
            print("購入手続きへボタンが表示されません。")
            return self.resOfToPurchaseProcedureButton()
        
    def resOfLoginView(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            if bool(re.match(r'https://nttxstore.jp/cart/cart_Login.asp\?noise=', self.driver.current_url)):
                resOfUserMailTextField = self.driver.find_elements_by_name("USER_EMAIL1")#mailフィールド
                resOfUserMailTextField[0].send_keys(self.mail)
                resOfUserPassTextField = self.driver.find_elements_by_name("PASSWD")#passwordフィールド
                resOfUserPassTextField[0].send_keys(self.passwd)
                resOfLoginButton = self.driver.find_elements_by_id("login_login")#ログインボタン
                resOfLoginButton[0].click()
        except:
            print("ログインボタンが表示されません。")
            return self.resOfLoginView()
        
    def resOfPaymentMethodButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ID_PAYMEN_DAIBIKI")))
            resOfPaymentMethodButton = self.driver.find_elements_by_id("ID_PAYMEN_DAIBIKI")#お支払い方法選択ボタン
            resOfPaymentMethodButton[0].click()
        except:
            print("お支払い方法選択ボタンが表示されません。")
            return self.resOfPaymentMethodButton()
        
    def resOfAgreeButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ID_POLICY")))
            resOfAgreeButton = self.driver.find_elements_by_id("ID_POLICY")#同意ボタン
            resOfAgreeButton[0].click()
        except:
            print("同意ボタンが表示されません。")
            return self.resOfPaymentMethodButton()
        
    def resOfNextCartButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ID_NEXT_CART")))
            resOfNextCartButton = self.driver.find_elements_by_id("ID_NEXT_CART")#次のステップへ進む
            resOfNextCartButton[0].click()
        except:
            print("次のステップへ進むが表示されません。")
            return self.resOfPaymentMethodButton()
        
    def resOfCartBuyButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cart_buy")))
            resOfCartBuyButton = self.driver.find_elements_by_NAME("cart_buy")#上記商品を購入するボタン
            resOfCartBuyButton[0].click()
        except:
            print("上記商品を購入するボタンが表示されません。")
            return self.resOfPaymentMethodButton()

    def quit(self):
        self.driver.quit()
        

# In[実際に起動する]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ :
model = auto_order(userdata_dir = "/Users/morimotoakito/Desktop/Anaconda/ChromeForBot",
                   mail = "mmakt122@gmail.com",
                   passwd = "nttxstorengahyahi02")
model.watch_start("https://nttxstore.jp/_II_QZZ0007553",
                   interval = 3,    
                   lim = 5000,
                   is_order = True)
model.quit()

























