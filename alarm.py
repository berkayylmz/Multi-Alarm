#-*- coding: utf-8 -*-
import re , urllib
from gtts import gTTS
import os
import schedule
import time
import subprocess


def job():

    os.system("mpg123 music.mp3") # Music to wake
    
    
    # Weather forecast
    
    url = 'http://www.accuweather.com/tr/tr/avcilar/318236/weather-forecast/318236'
    connection  = urllib.urlopen(url)
    kod = connection.read()
    kod = kod.decode('utf-8')
    haber = '<span class="local-temp">(.*?)</span>'
    title = re.findall(haber, kod)

    baslik = "\n".join(title)

    result = re.sub('[^0-9]','', baslik)

    rs = "istanbul'da hava " + str(result) + " derece ."
    rs = rs.decode('utf-8')
	
	# Comment about wearing

    if result <= "5":
    
        yorum = " hava soğuk . sıkı giyin ." 

    elif result <= "20":

        yorum = " hava ılık ."

    elif result <= "60":

        yorum = " hava sıcak . ince giyin ."

    yorum = yorum.decode('utf-8')
    print rs + yorum

    havadurumu = rs + yorum

    #News
    
    url = 'http://www.webtekno.com/haber'
    connection  = urllib.urlopen(url)
    kod = connection.read()
    kod = kod.decode('utf-8')
    haber = '<span class="content-timeline--underline">(.*?)</span>'
    title = re.findall(haber, kod)

    body = "\n".join(title)

    yazif = body.replace("&#039;", "'")
    yazif = yazif.replace("&quot;", "")
    yazif = yazif 

    sunu = "haberler başlıyorr ; "
    sunu = sunu.decode('utf-8')

    sonra = "'' Ders programı birazdan başlayacak : "
    sonra = sonra.decode('utf-8')

    yazif = sunu + yazif 
    hava_y = "hava durumu başlıyor ; "
    hava_y = hava_y.decode('utf-8')
    hava_y = "\n".join(hava_y)
    



    # Weekly lesson plan 

    def job2():
    
        gun = time.strftime("%A")

        list_monday = ["kimya","kimya","matematik",
                   "matematik","dil ve anlatım","dil ve anlatım",
                   "beden","beden"]
        list_tuesday = ["fizik","fizik","etkinlik",
                   "etkinlik","ingilizce","ingilizce",
                   "tarih","tarih"]
        list_wendesday = ["matematik","matematik","temel dini bilgiler",
                   "din kültürü","ingilizce","ingilizce",
                   "biyoloji","biyoloji"]
        list_thursday = ["matematik","müzik","din",
                   "ikinci yabancı dil","ikinci yabancı dil","dijital ingilizce",
                   "basit ingilizce","sosyal etkinlikler"]
        list_sunday = ["beden eğitimi","beden eğitimi","dijital ingilizce",
                   "dijital ingilizce","ikinci yabancı dil","ikinci yabancı dil",
                   "türkçe","türkçe","basit ingilizce","basit ingilizce"]

        if time.strftime("%A") == "Monday":

    
            deger = list_monday


        elif time.strftime("%A") == "Tuesday":

    
            deger = list_tuesday
    
    

        elif time.strftime("%A") == "Wendesday":

    
            deger = list_wendesday

    

        elif time.strftime("%A") == "Thursday":

            deger = list_thursday

    

        elif time.strftime("%A") == "Sunday":

    
            deger = list_sunday

        now2 = time.strftime("%H-%M-%S.mp3")
        
        ttss = gTTS(text="".join(deger), lang="tr")
        ttss.save(now2)

        os.system("mpg123 -q "+now2+" &")

        

    sonuc = sunu+yazif+hava_y+havadurumu+sonra
    

    print "\nHaberler;\n"

    print yazif

    now = time.strftime("%A-%H-%M-%S.mp3")

    
       
    tts = gTTS(text="".join(sonuc), lang="tr")
    tts.save(now)

    

    os.system("mpg123 -q "+now+" &")
    
    time.sleep( 95 )

    

    job2()

    now2 = time.strftime("%A-%H-%M-%S.mp3")

    tts = gTTS(text="".join(deger), lang="tr")
    tts.save(now2)
  
    
schedule.every().day.at("08:20").do(job) #set time


while True:
    
    schedule.run_pending()
    time.sleep(1)
