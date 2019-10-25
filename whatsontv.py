import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
from kivy.storage.dictstore import DictStore
from kivy.clock import Clock
import threading
import datetime
import os

from ImageDownload import downloadimages

class Program:
  def __init__(self, isim, time, kanal):
    self.isim = isim
    self.time = time
    self.kanal = kanal

store = DictStore('data.py')
Programlar=[]
Kanallar_settings=[False]*47

if(store.exists('1')):
    print('loading data')
    for i in range(0, len(Kanallar_settings)):
        Kanallar_settings[i]=store.get(str(i))['state']





class WindowManager(ScreenManager):
    pass

class ChooseWindow(Screen):
    renklist = ListProperty(None)


    def storedata(self):
        for i in range(0,len(Kanallar_settings)):
            store.put(str(i), state=Kanallar_settings[i])

    def press_kanal(self,i,obje):
        Kanallar_settings[i] = not Kanallar_settings[i]
        if (obje.background_color == [0, 1, 0, 1]):
            obje.background_color = 1, 1, 1, 1
        else:
            obje.background_color = 0, 1, 0, 1


class ChooseWindow2(Screen):
    def storedata(self):
        for i in range(0,len(Kanallar_settings)):
            store.put(str(i), state=Kanallar_settings[i])


    def press_kanal(self,i,obje):
        Kanallar_settings[i] = not Kanallar_settings[i]
        if (obje.background_color == [0, 1, 0, 1]):
            obje.background_color = 1, 1, 1, 1
        else:
            obje.background_color = 0, 1, 0, 1



class MainWindow(Screen):
    scroll_grid= ObjectProperty(None)

    cols=1
    rows = 1



    Urller = [
        'https://www.tvyayinakisi.com/kanal-d-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/show-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/star-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/fox-yayin-akisi',
        'https://www.tvyayinakisi.com/atv-yayin-akisi',
        'https://www.tvyayinakisi.com/tv-8-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-1-yayin-akisi',
        'https://www.tvyayinakisi.com/teve2-yayin-akisi',
        'https://www.tvyayinakisi.com/beyaz-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/a2-yayin-akisi',
        'https://www.tvyayinakisi.com/tv-85-yayin-akisi',
        'https://www.tvyayinakisi.com/cartoon-network-yayin-akisi',
        'https://www.tvyayinakisi.com/tlc-yayin-akisi',
        'https://www.tvyayinakisi.com/kanal-7-yayin-akisi',
        'https://www.tvyayinakisi.com/cnn-turk-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-3-yayin-akisi',
        'https://www.tvyayinakisi.com/fb-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/a-haber-yayin-akisi',
        'https://www.tvyayinakisi.com/disney-channel-yayin-akisi',
        'https://www.tvyayinakisi.com/halk-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/ntv-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-cocuk-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-movies-turk-yayin-akisi',
        'https://www.tvyayinakisi.com/360-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-movies-premiere-yayin-akisi',
        'https://www.tvyayinakisi.com/disney-junior-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-series-sci-fi-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-2-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-movies-stars-yayin-akisi',
        'https://www.tvyayinakisi.com/national-geographic-yayin-akisi',
        'https://www.tvyayinakisi.com/haberturk-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-movies-action-yayin-akisi',
        'https://www.tvyayinakisi.com/bloomberg-ht-yayin-akisi',
        'https://www.tvyayinakisi.com/ulke-tv-yayin-akisi',
        'https://www.tvyayinakisi.com/disney-xd-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-okul-yayin-akisi',
        'https://www.tvyayinakisi.com/discovery-channel-yayin-akisi',
        'https://www.tvyayinakisi.com/kanal-24-yayin-akisi',
        'https://www.tvyayinakisi.com/trt-muzik-yayin-akisi',
        'https://www.tvyayinakisi.com/eurosport-yayin-akisi',
        'https://www.tvyayinakisi.com/nickelodeon-yayin-akisi',
        'https://www.tvyayinakisi.com/ntvspor-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-movies-action-2-yayin-akisi',
        'https://www.tvyayinakisi.com/bein-box-office-1-yayin-akisi',
        'https://www.tvyayinakisi.com/nick-jr-yayin-akisi',
        'https://www.tvyayinakisi.com/s-sport-yayin-akisi'
    ]
    Kanallar = [
        'kanald',
        'show',
        'star',
        'fox',
        'atv',
        'tv8',
        'trt1',
        'teve2',
        'beyaztv',
        'a2',
        'tv85',
        'cn',
        'tlc',
        'kanal7',
        'cnnturk',
        'trtspor',
        'fbtv',
        'ahaber',
        'disney',
        'halktv',
        'ntv',
        'trtcocuk',
        'beinmoviesturk',
        '360',
        'beinmoviesp',
        'disneyj',
        'beinss',
        'trthaber',
        'beinms',
        'natigeo',
        'haberturk',
        'beinma',
        'bloomberg',
        'ulketv',
        'disneyxd',
        'trtokul',
        'discovery',
        '24',
        'trtmuzik',
        'eurosport',
        'nick',
        'ntvspor',
        'beinma2',
        'beinboxo',
        'nickjr',
        'ssport'
    ]

    def getprogram(self,i):
        if (Kanallar_settings[i] == True):
            req = Request(self.Urller[i], headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req)
            webpage_raw = webpage.read()
            webpage.close()
            page_soup = soup(webpage_raw, "html.parser")
            box = page_soup.find("div", {"class": "active"})
            Time = datetime.datetime.now().time()
            for program in box.ul.findAll("li"):
                if (Time.hour * 60 + Time.minute >= int(program["data-start"][-8:-6]) * 60 + int(
                        program["data-start"][-5:-3]) and Time.hour * 60 + Time.minute <= int(
                        program["data-end"][-8:-6]) * 60 + int(program["data-end"][-5:-3])):
                    Programlar.append(Program(program.find("p", {"class": "name"}).get_text(),
                                              Time.hour * 60 + Time.minute - (
                                                          int(program["data-start"][-8:-6]) * 60 + int(
                                                      program["data-start"][-5:-3])), self.Kanallar[i]))

                    return Programlar[-1]
            last_program=box.ul.findAll("li")[-1]
            if(Time.hour==0):
                return (Program(last_program.find("p", {"class": "name"}).get_text(),
                                24 * 60 + Time.minute - (
                                        int(last_program["data-start"][-8:-6]) * 60 + int(
                                    last_program["data-start"][-5:-3])), self.Kanallar[i]))
            else:
                return (Program(last_program.find("p", {"class": "name"}).get_text(),
                                              Time.hour * 60 + Time.minute - (
                                                          int(last_program["data-start"][-8:-6]) * 60 + int(
                                                      last_program["data-start"][-5:-3])), self.Kanallar[i]))

    def refresh(self):
        Programlar.clear()
        for child in [child for child in self.scroll_grid.children]:
            self.scroll_grid.remove_widget(child)

        for i in range(0, len(self.Urller)):
            program = self.getprogram(i)
            if(program!=None):
                img = Image(source=(os.path.join(os.getcwd(), 'images', program.kanal + "." + 'png')),size_hint=(0.5,0.5),pos_hint=(0.5,0.5))
                label =Label(text=program.isim.replace(' ', '\n'), font_size='15sp',bold=True)
                self.scroll_grid.add_widget(img)
                self.scroll_grid.add_widget(label)
                self.scroll_grid.add_widget(Label(text=(str(program.time) + ' dk geçti'), font_size='15sp'))


renkler=[]
print('setting colors up')
for i in range(0,len(Kanallar_settings)):
    if(Kanallar_settings[i]==True):
            renkler.append((0,1,0,1))
    else:
            renkler.append((1,1,1,1))
renklist = renkler.copy()





kv = Builder.load_file("my.kv")





class MyMainApp(App):


    def build(self):
        return kv




if __name__ == "__main__":
    MyMainApp().run()
