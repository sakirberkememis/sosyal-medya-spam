import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
import os
import pyautogui
import pyperclip

def soru():
    global bas_soru
    bas_soru = input("""Lütfen hangi platformdan mesaj atacağınızı seçiniz;
1. WhatsApp
2. Instagram
3. Telegram
numarasını giriniz: """)

soru()

if(bas_soru == "1"):
    dizin = os.getcwd()

    mesaj = input("Göndermek istediğiniz mesajı yazınız: ")
    kac = int(input("Mesaj kaç kere gönderilsin!: "))


    chrome_options = Options()
    browser =webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    url = "https://web.whatsapp.com/"
    browser.get(url)

    #time.sleep()

    bildirim = ToastNotifier()
    bildirim.show_toast(title="Uyarı!!", msg="QR kodu okutunuz 30 saniyeniz var, ve göndereceğiniz kişiyi seçiniz!", duration=5)

    time.sleep(25)


    for i in range(0,kac):
        mesaj_yaz = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        mesaj_yaz.send_keys(mesaj)

        buton = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        buton.click()

    time.sleep(0.5)
    bildirim = ToastNotifier()
    bildirim.show_toast(title="bildirim", msg="İşlem Tamamlandı!!", duration=5)


elif(bas_soru == "2"):
    dizin = os.getcwd()

    mesaj2 = input("Göndermek istediğiniz mesajı yazınız: ")
    kac2 = int(input("Mesaj kaç kere gönderilsin!: "))

    chrome_options2 = Options()
    browser2 =webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options2)

    url2 = "https://www.instagram.com/"
    browser2.get(url2)

    bildirim = ToastNotifier()
    bildirim.show_toast(title="Instagram hesabınıza giriş yapınız ve mesaj göndereceğiniz kişiyi seçiniz", msg="", duration=5)

    time.sleep(60)

    for i in range(0, kac2):
        mesaj_yaz2 = browser2.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        mesaj_yaz2.send_keys(mesaj2)

        time.sleep(0.1)

        buton2 = browser2.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        buton2.click()

    time.sleep(0.5)
    bildirim = ToastNotifier()
    bildirim.show_toast(title="bildirim", msg="İşlem Tamamlandı!!", duration=5)


elif(bas_soru == "3"):
    mesaj3 = input("Göndermek istediğiniz mesajı yazınız: ")
    kac3 = int(input("Mesaj kaç kere gönderilsin!: "))
    pyperclip.copy(mesaj3)
    input("Lütfen bilgisayardaki telegram uygulamasına bağlanın ve göndereceğiniz kişiyi seçin seçince programda entere basın ve telegramı pencere olarak seçin!!!")
    time.sleep(10)
    for i in range(0, kac3):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

    time.sleep(0.5)
    bildirim = ToastNotifier()
    bildirim.show_toast(title="bildirim", msg="İşlem Tamamlandı!!", duration=5)





else:
    print("\nLütfen bulunan sayılardan birini giriniz!!!")
    time.sleep(1)
    soru()


