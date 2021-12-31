import os
import pathlib
import time
import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
from pyttsx3 import speak
from selenium import webdriver
import speech_recognition as sr
from gtts import gTTS

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 389)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        Form.setFont(font)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 441, 431))
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("space.jpg"))
        self.label.setObjectName("label")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 270, 111, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.talkButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.talkButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.talkButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.talkButton.setFont(font)
        self.talkButton.setAutoFillBackground(False)
        self.talkButton.setIconSize(QtCore.QSize(64, 64))
        self.talkButton.setObjectName("talkButton")

        #When you click the button what happened.
        self.talkButton.clicked.connect(self.get_audio)

        self.horizontalLayout.addWidget(self.talkButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 431, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(120, 220, 211, 21))
        self.progressBar.setVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("color: white;")
        self.progressBar.setProperty("value",0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def get_audio(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                #Record what we are saying.
                said = r.recognize_google(audio,language="tr-TR")
                said = str(said)
                said = said.capitalize()
                print(said)

                cities = ["Adana","Adıyaman","Afyonkarahisar","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa"
                          ,"Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari"
                          ,"Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa"
                          ,"Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon"
                          ,"Tunceli","Şanlıurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova"
                          ,"Karabük","Kilis","Osmaniye","Düzce"]

                for i in cities:
                    if(said == (i+" hava durumu")):
                        self.progressBar.setVisible(True)
                        counter = 0
                        valueOfProgress = 0
                        option = webdriver.ChromeOptions()
                        option.headless=True
                        browser = webdriver.Chrome("chromedriver.exe",options=option)
                        url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il="+i
                        browser.get(url)

                        # We get datas from official weather website.
                        dataDate = browser.find_element_by_xpath("//*[@id='pages']/div/section/h2[1]/span").text
                        temperatureWeather = browser.find_element_by_xpath("//*[@id='pages']/div/section/div[5]/div[1]/div[1]").text
                        titleWeather = browser.find_element_by_xpath("//*[@id='pages']/div/section/div[5]/div[1]/div[2]/div[2]").text
                        ratioMoisture = browser.find_element_by_xpath("//*[@id='pages']/div/section/div[5]/div[2]/div[1]/div[2]/div[2]").text

                        while(counter!=101):
                            self.progressBar.setValue(valueOfProgress)
                            time.sleep(0.02)
                            valueOfProgress+=1
                            counter+=1

                        self.textBrowser.setFontPointSize(11)
                        self.textBrowser.setText("Şehir: "+i+"\n"+"Zaman: "+dataDate+"\n"+"Sıcaklık: "+temperatureWeather+"\n"+"Hava durumu: "+titleWeather+"\n"+"Nem: %"+ratioMoisture)


                    elif(said == (i+" namaz vakti")):
                        self.progressBar.setVisible(True)
                        counter = 0
                        valueOfProgress = 0

                        #We are changing some letters because English alphabet has no some letters.
                        cityName = i
                        i = i.lower()
                        i = i.replace("ö","o")
                        i = i.replace("ı","i")
                        i = i.replace("ü","u")
                        i = i.replace("ğ","g")
                        i = i.replace("ç","c")
                        i = i.replace("ş","s")

                        option = webdriver.ChromeOptions()
                        option.headless=True
                        browser = webdriver.Chrome("chromedriver.exe",options=option)

                        #We check name of city and after then go to that website.
                        if(cityName == "İstanbul"):
                            url = "https://www.sabah.com.tr/istanbul-namaz-vakitleri"

                        elif(cityName == "İzmir"):
                            url = "https://www.sabah.com.tr/izmir-namaz-vakitleri"

                        else:
                            url = "https://www.sabah.com.tr/"+i+"-namaz-vakitleri"

                        browser.get(url)

                        #We are getting datas from website.
                        imsakVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[1]").text
                        gunesVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[2]").text
                        ogleVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[3]").text
                        ikindiVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[4]").text
                        aksamVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[5]").text
                        yatsiVakti = browser.find_element_by_xpath("/html/body/section/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/ul/li[6]").text

                        imsakVakti = str(imsakVakti)
                        imsakVakti = imsakVakti.replace("\n"," ")
                        imsakVakti = imsakVakti.split(" ")

                        gunesVakti = str(gunesVakti)
                        gunesVakti = gunesVakti.replace("\n"," ")
                        gunesVakti = gunesVakti.split(" ")

                        ogleVakti = str(ogleVakti)
                        ogleVakti = ogleVakti.replace("\n"," ")
                        ogleVakti = ogleVakti.split(" ")

                        ikindiVakti = str(ikindiVakti)
                        ikindiVakti = ikindiVakti.replace("\n"," ")
                        ikindiVakti = ikindiVakti.split(" ")

                        aksamVakti = str(aksamVakti)
                        aksamVakti = aksamVakti.replace("\n"," ")
                        aksamVakti = aksamVakti.split(" ")

                        yatsiVakti = str(yatsiVakti)
                        yatsiVakti = yatsiVakti.replace("\n"," ")
                        yatsiVakti = yatsiVakti.split(" ")

                        while (counter != 101):
                            self.progressBar.setValue(valueOfProgress)
                            time.sleep(0.02)
                            valueOfProgress += 1
                            counter += 1

                        self.textBrowser.setFontPointSize(11)
                        self.textBrowser.setText("Şehir: "+cityName+"\n\n"+"İmsak  Güneş  Öğle   İkindi   Akşam  Yatsı"+"\n"+imsakVakti[1]+"  "+gunesVakti[1]+"  "+ogleVakti[1]+"  "+ikindiVakti[1]+"  "
                                                 +aksamVakti[1]+"  "+yatsiVakti[1])

                if(said == "Maç takvimi"):
                    self.progressBar.setVisible(True)
                    counter = 0
                    valueOfProgress = 0
                    option = webdriver.ChromeOptions()
                    option.headless=True
                    browser = webdriver.Chrome("chromedriver.exe",options=option)
                    url = "https://www.tff.org/default.aspx?pageID=198"
                    browser.get(url)

                    #We get datas from official league website.
                    firstMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[2]/td/table/tbody").text
                    firstMatch = str(firstMatch)
                    firstMatch = firstMatch.replace("Detaylar","")

                    secondMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[3]/td/table/tbody").text
                    secondMatch = str(secondMatch)
                    secondMatch = secondMatch.replace("Detaylar","")

                    thirdMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[4]/td/table/tbody").text
                    thirdMatch = str(thirdMatch)
                    thirdMatch = thirdMatch.replace("Detaylar","")

                    fourthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[5]/td/table/tbody").text
                    fourthMatch = str(fourthMatch)
                    fourthMatch = fourthMatch.replace("Detaylar","")

                    fifthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[6]/td/table/tbody").text
                    fifthMatch = str(fifthMatch)
                    fifthMatch = fifthMatch.replace("Detaylar","")

                    sixthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[7]/td/table/tbody").text
                    sixthMatch = str(sixthMatch)
                    sixthMatch = sixthMatch.replace("Detaylar","")

                    seventhMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[8]/td/table/tbody").text
                    seventhMatch = str(seventhMatch)
                    seventhMatch = seventhMatch.replace("Detaylar","")

                    eighthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[9]/td/table/tbody").text
                    eighthMatch = str(eighthMatch)
                    eighthMatch = eighthMatch.replace("Detaylar","")

                    ninthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[10]/td/table/tbody").text
                    ninthMatch = str(ninthMatch)
                    ninthMatch = ninthMatch.replace("Detaylar","")

                    tenthMatch = browser.find_element_by_xpath("//*[@id='ctl00_MPane_m_198_10560_ctnr_m_198_10560_dtlHaftaninMaclari']/tbody/tr[11]/td/table/tbody").text
                    tenthMatch = str(tenthMatch)
                    tenthMatch = tenthMatch.replace("Detaylar","")

                    self.textBrowser.setFontPointSize(8)

                    while (counter != 101):
                        self.progressBar.setValue(valueOfProgress)
                        time.sleep(0.02)
                        valueOfProgress += 1
                        counter += 1

                    self.textBrowser.setText(firstMatch+"\n"+secondMatch+"\n"+thirdMatch+"\n"+fourthMatch+"\n"+fifthMatch+"\n"+sixthMatch+"\n"+seventhMatch+"\n"+eighthMatch+"\n"+ninthMatch+"\n"+tenthMatch)

                elif(said == "Youtube aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.youtube.com/"
                    browser.get(url)

                elif(said == "Instagram aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.instagram.com/"
                    browser.get(url)

                elif(said == "Facebook aç"):
                    browser = webdriver.Chrome()
                    url = "https://tr-tr.facebook.com/"
                    browser.get(url)

                elif(said == "Twitter aç"):
                    browser = webdriver.Chrome()
                    url = "https://twitter.com/?lang=tr"
                    browser.get(url)

                elif(said == "Spotify aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.spotify.com/tr/"
                    browser.get(url)

                elif(said == "Google aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.google.com/"
                    browser.get(url)

                elif(said == "Java aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.tutorialspoint.com/compile_java_online.php"
                    browser.get(url)

                elif(said == "Whatsapp aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.whatsapp.com/?lang=tr"
                    browser.get(url)

                elif(said == "Skype aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.skype.com/tr/"
                    browser.get(url)

                elif(said == "E-posta aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.google.com/intl/tr/gmail/about/"
                    browser.get(url)

                elif(said == "Python aç"):
                    browser = webdriver.Chrome()
                    url = "https://www.programiz.com/python-programming/online-compiler/"
                    browser.get(url)

            except Exception:
                #If we dont say clearly, assistant will speak this text
                speak("Sorry, i can't understand you. Can you say again ?")

    def speak(self,text):
        tts = gTTS(text=text, lang="tr", slow=True)
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.talkButton.setText(_translate("Form", "T A L K"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())