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
    def __init__(self, userdata_dir):
        print("-------------------AmazonBotStart---------------------")
        print(" \|/        \|/       \|/      \|/      \|/      \|/  ")
        print("  |          |        \|/      \|/      \|/      \|/  ")
        print("  |   \/     |    //   |        |   \/   |/       |   ")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□□■■■■□□□□■■□■■□□□□□■■■■□□□□■■■■■■□□□□■■■□□□□■■□■■■□□□")
        print("□■□□□□■□□■□□■□□■□□□■□□□□■□□□■□□□■□□□□■□□□■□□□□■■□□□■□□")
        print("□□□□□□■□□■□□■□□■□□□□□□□□■□□□□□□■□□□□■□□□□□■□□□■□□□□■□□")
        print("□□■■■■■□□■□□■□□■□□□□■■■■■□□□□□□■□□□□■□□□□□■□□□■□□□□■□□")
        print("□■□□□□■□□■□□■□□■□□□■□□□□■□□□□□■□□□□□■□□□□□■□□□■□□□□■□□")
        print("■□□□□□■□□■□□■□□■□□■□□□□□■□□□□□■□□□□□■□□□□□■□□□■□□□□■□□")
        print("■□□□□□■□□■□□■□□■□□■□□□□□■□□□□■□□□■□□■□□□□□■□□□■□□□□■□□")
        print("■□□□□■■□□■□□■□□■□□■□□□□■■□□□■□□□□■□□□■□□□■□□□□■□□□□■□□")
        print("□■■■■□■■□■■□■■□■■□□■■■■□■■□■■■■■■■□□□□■■■□□□□■■■□□■■■□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
        print(" \|/        \|/       \|/      \|/      \|/      \|/  ")
        print("  |          |        \|/      \|/      \|/      \|/  ")
        print("  |   \/     |    //   |        |   \/   |/       |   ")
        print("-------------------AmazonBotStart---------------------")
        self.userdata_dir = userdata_dir #ユーザープロファイル PATH
        options = Options()
        options.add_argument('--user-data-dir=' + self.userdata_dir)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def watch_start(self,url, interval = 300, lim = 1000, is_order = False):
        count = 0        
        while True:
            self.driver.get(url)
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            resOfSeeAllButton = self.driver.find_elements_by_id("buybox-see-all-buying-choices-announce")#全ての商品を見るボタン
            resOfAddToCartButton = self.driver.find_elements_by_id("add-to-cart-button")#カートに加えるボタン
            
            if len(resOfSeeAllButton) == 0 and len(resOfAddToCartButton) == 0:#ボタンが存在しない時
                print("not found 404")
            else:#ボタンが存在する時
                print("has been found")
                if is_order:
                    if len(resOfSeeAllButton) != 0:#全ての商品を見るボタンがある時
                        resOfSeeAllButton[0].click()
                        soup = BeautifulSoup(self.makeHtml(), "lxml")
                        narrowDownSoup = soup.find_all(class_="a-size-large a-color-price olpOfferPrice a-text-bold")
                        matcher = re.findall('￥ (.{6})', str(narrowDownSoup[0]))
                        price = int(matcher[0].replace(',',''))
                        if price < 60000:
                            #カートに加える
                            self.resOfAddToCartButton1()
                            #レジに進む
                            self.setOfGoToTheCashierButton()
                            #お届け先住所の選択
                            self.resOfAddressSelectButton()
                            #発送オプションと配送オプションを選んでください
                            self.resOfOptionSelectButton()
                            #お支払い方法を選択
                            self.resOfPaySelectButton() 
                            #注文確定
                            #self.resOfPlaceYourOrderButton()
                            print("購入できた")
                            break
                        
                        else:
                            print("　　　正規価格ではない　　")
                            print("物売るってレベルじゃねーーそ")
                        
                    elif len(resOfAddToCartButton) != 0:#カートに加えるボタンがある時
                        resOfAddToCartButton[0].click()
                        #レジに進む
                        self.setOfGoToTheCashierButton()
                        #お届け先住所の選択
                        self.resOfAddressSelectButton()
                        #発送オプションと配送オプションを選んでください
                        self.resOfOptionSelectButton()
                        #お支払い方法を選択
                        self.resOfPaySelectButton() 
                        #注文確定
                        #self.resOfPlaceYourOrderButton()
                        print("購入できた")
                        break
                        
                    
            if count > lim:
                break

            time.sleep(interval)
            count += 1
            print("\nループ回数{0}".format(count))
            
    def makeHtml(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            url = self.driver.current_url
            html = urllib.request.urlopen(str(url))
            return html
        except:
            print("HTTPエラーとなりました。再読み込み")
            return self.makeHtml()
        
    def resOfAddToCartButton1(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'submit.addToCart')))
            resOfAddToCartButton1 = self.driver.find_elements_by_name('submit.addToCart')
            resOfAddToCartButton1[0].click()
        except:
            print("カートに加える画面で加えるボタンが表示されません。")
            return self.resOfAddToCartButton1()
        
    def setOfGoToTheCashierButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'hlb-ptc-btn-native')))
            setOfGoToTheCashierButton = self.driver.find_elements_by_id("hlb-ptc-btn-native")
            setOfGoToTheCashierButton[0].click()
        except:
            print("レジに進むボタンが表示されません。")
            return self.setOfGoToTheCashierButton()
        
    # def resOfMailView(self):
    #     try:
    #         WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
    #         if self.driver.current_url == 'https://www.amazon.co.jp/ap/signin?_encoding=UTF8&openid.assoc_handle=amazon_checkout_jp&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fbuy%2Fsignin%2Fhandlers%2Fcontinue.html%3Fie%3DUTF8%26brandId%3D%26cartItemIds%3D%26eGCApp%3D%26hasWorkingJavascript%3D0%26isEGCOrder%3D0%26isFresh%3D0%26oldCustomerId%3D%26oldPurchaseId%3D%26preInitiateCustomerId%3D%26purchaseInProgress%3D%26ref_%3Dcart_signin_submit%26siteDesign%3D&pageId=amazon_checkout_jp&showRmrMe=0&siteState=isRegularCheckout.1%7CIMBMsgs.%7CisRedirect.0':
    #             resOfUserMailTextField = self.driver.find_elements_by_name("")#mailフィールド
    #             resOfUserMailTextField[0].send_keys(self.passwd)
    #             resOfLoginButton = self.driver.find_elements_by_id("continue-announce")#次へボタン
    #             resOfLoginButton[0].click()
    #             print("次へボタンclick")
    #     except:
    #         print("次へボタンが表示されません。")
    #         return self.resOfMailView()
        
    # def resOfPasswordView(self):
    #     try:
    #         WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
    #         if self.driver.current_url == 'https://www.amazon.co.jp/ap/signin?_encoding=UTF8&openid.assoc_handle=amazon_checkout_jp&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fgp%2Fbuy%2Fsignin%2Fhandlers%2Fcontinue.html%3Fie%3DUTF8%26brandId%3D%26cartItemIds%3D%26eGCApp%3D%26hasWorkingJavascript%3D0%26isEGCOrder%3D0%26isFresh%3D0%26oldCustomerId%3D%26oldPurchaseId%3D%26preInitiateCustomerId%3DAUXPLEA6D1JAS%26purchaseInProgress%3D%26ref_%3Dcart_signin_submit%26siteDesign%3D&pageId=amazon_checkout_jp&showRmrMe=1&siteState=isRegularCheckout.1%7CIMBMsgs.%7CisRedirect.0':
    #             resOfUserPassTextField = self.driver.find_elements_by_name("")#passwordフィールド
    #             resOfUserPassTextField[0].send_keys(self.passwd)
    #             resOfLoginButton = self.driver.find_elements_by_id("")#ログインボタン
    #             resOfLoginButton[0].click()
    #             print("ログインボタンclick")
    #     except:
    #         print("ログインボタンが表示されません。")
    #         return self.resOfPasswordView()
        
    def resOfAddressSelectButton(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            if self.driver.current_url == 'https://www.amazon.co.jp/gp/buy/addressselect/handlers/display.html?hasWorkingJavascript=1':
                resOfAddressSelectButton = self.driver.find_elements_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/span[1]/a[1]")
                resOfAddressSelectButton[0].click()
                print("選択ボタンclick")
        except:
            print("住所選択の画面で選択ボタンが表示されません。")
            return self.resOfAddressSelectButton()
        
    def resOfOptionSelectButton(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            if self.driver.current_url == 'https://www.amazon.co.jp/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1':
                resOfOptionSelectButton = self.driver.find_elements_by_class_name("a-box-inner")
                resOfOptionSelectButton[0].click()
                print("次へボタンclick")
        except:
            print("発送オプションと配送オプションの画面で次へボタンが表示されません。")
            return self.resOfOptionSelectButton()
        
    def resOfPaySelectButton(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located)
            if self.driver.current_url == 'https://www.amazon.co.jp/gp/buy/payselect/handlers/display.html?hasWorkingJavascript=1':
                resOfPaySelectButton = self.driver.find_elements_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
                resOfPaySelectButton[0].click()
                print("続行ボタンclick")
        except:
            print("お支払い方法選択の画面で続行ボタンが表示されません。")
            return self.resOfPaySelectButton()
        
    def resOfPlaceYourOrderButton(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'placeYourOrder')))
            resOfPlaceYourOrderButton = self.driver.find_elements_by_id("placeYourOrder")
            resOfPlaceYourOrderButton[0].click()
            print("注文確定ボタンclick")
        except:
            print("注文確定の画面で注文確定ボタンが表示されません。")
            return self.resOfPlaceYourOrderButton()
        

    def quit(self):
        self.driver.quit()
        

# In[実際に起動する]↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ :
model = auto_order(userdata_dir = "/Users/********/Desktop/Anaconda/ChromeForBot")
model.watch_start("https://www.amazon.co.jp/Logicool-%E3%82%B2%E3%83%BC%E3%83%9F%E3%83%B3%E3%82%B0%E3%83%98%E3%83%83%E3%83%89%E3%82%BB%E3%83%83%E3%83%88-LIGHTSPEED%E3%83%AF%E3%82%A4%E3%83%A4%E3%83%AC%E3%82%B9-%E3%82%B5%E3%82%B9%E3%83%9A%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%B3%E3%83%89-G733-BK/dp/B08FSYJ92M/ref=sr_1_34?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=ps5&qid=1607198230&sr=8-34", 
                    interval = 10,
                    lim = 5000,
                    is_order = True)
model.quit()

























