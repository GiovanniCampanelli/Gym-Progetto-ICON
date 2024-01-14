from __future__ import (absolute_import,division,print_function,unicode_literals,)

import telegram.ext
import unicodedata

#import flask_mysqldb
#from flask import Flask
#from flask_mysqldb import MySQL
import future
from bs4 import BeautifulSoup
from google.cloud import translate_v2 as tra
import random
import csv
import pygetwindow as gw
import keyboard
import google_trans
from google_trans import Translator as transle
import langdetect
from langdetect import detect, lang_detect_exception
import unicodedata
import scrapy
import mysql.connector
import encodings
import re
import os
import sys
from urllib.request import urlopen
import time
import sched
import functools
import operator
import pickle
import pymysql
import datetime
import rasa
import rasa_sdk
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from builtins import *
from typing import Final
from telegram import Update,Bot,_update,ChatMemberUpdated
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes,CallbackContext,Updater,_jobqueue
import multiprocessing
import urllib3
import requests

TOKEN: Final = '6106626051:AAGPCWgk2YnJleGRcgjdCqjpUbmGuMPsVyw'
BOT_USERNAME: Final = '@PlatinumGameBot'
global links
links = ["3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3",]
global appr
app = Application.builder().token(TOKEN).build()
global nome
nome=""
global cognome
cognome=""
global eta
eta=""
global username
username=""
global risposta
risposta=""
global quando
quando=""
global extra
extra=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1""1","1","1","1","1","1","1","1","1","1"]
global tutto
tutto=""
global dove
dove=""
global come
come=""
global genere
genere=""
global periodo
periodo=""
global inglese
inglese=""
global lingue
lingue=""
global lingue2
lingue2=""
global lingue3
lingue3=""
global lingue4
lingue4=""
global strumentali
strumentali=""
global strumentali2
strumentali2=""
global ballo
ballo=""
global ballo2
ballo2=""
global canto
canto=""
global canto2
canto2=""
global film
film=""
global radio
radio=""
global varr
varr=""
global frequenza
frequenza=""
global ore
ore=""
global strumento
strumento=""
global strumento2
strumento2=""
global serie
serie=""
global commerciale
commerciale=""
global hobby
hobby=""
global videogiochi
videogiochi=""
global testo
testo=""
global testo2
testo2=""
lop=""
#def send_to_rasa(user_message):
    #rasa_server_url = "http://localhost:5005"  # Sostituisci con l'URL del tuo server Rasa

    #payload = {
        #"sender": "user",
        #"message": user_message
    #}

    #response = requests.post(f"{rasa_server_url}/webhooks/rest/webhook", json=payload)
    #rasa_response = response.json()

    #if rasa_response:
        #return rasa_response[0]["text"]
    #else:
        #return "Mi dispiace, non ho capito."

def bbot():
    app = Application.builder().token(TOKEN).build()

def stop_bot(update: Update, context: CallbackContext):
    if update.message.chat.type == "private":
        update.message.reply_text("Il bot verrà arrestato.")
        context.application.stop()
    else:
        update.message.reply_text("Questo comando può essere utilizzato solo in chat privata con il bot.")

def stop_polling():
    app.stop_polling()
    print("Polling interrotto.")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Digita "inizia" per cominciare il questionario , se hai gia fatto il questionario e non lo vuoi ripetere fai comunque "inizia" , in caso di soprannome e nome uguali , ti verra chiesto di saltarlo , digitare "si" in caso')
def polling():
    #while(varr!=7):
    app.run_polling(poll_interval=3)
       #app.stop()
    #await Application.stop()
    #if (varr == "7"):
        #app = Application.builder().token(TOKEN).build()
        #Updater.stop()
        #return("cavallo")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
       message_type: str = update.message.chat.type
       text: str = update.message.text
       print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
       #send_to_rasa(text)
       if message_type=='group':
           if BOT_USERNAME in text:
                  new_text: str = text.replace(BOT_USERNAME, '').strip()
                  response: str = handle_response(new_text)
           else:
               return
       else:
           response: str = handle_response(text)

       print('Bot:', response)
       await update.message.reply_text(response)

       #if(varr=="7"):
           #print("gio")
           #global app
           #Bot.close()
           #app.shutdown()
        #await app.shutdown()
        #updater = Updater.shutdown()
        #ChatMemberUpdated.
        #telegram.ext.Updater.shutdown(self=Application.builder().token(TOKEN).build())
        #app.shutdown()
        #await context.bot.Updater.stop()
        #loger=TOKEN._LOGGER
        #chat_idd=update.message.chat_id
        #await Bot.leaveChat(chat_idd)
       #await app.shutdown()
       #telegram.Bot=TOKEN
           #return("add")
        #app.stop()

def handle_response(text: str) ->str:
    #processed: str = text.lower()
    #return 'ffsafa'
    global lop
    processed: str = text.lower()
    if 'ciao' in processed:
        return 'salve!'

    if 'come stai' in processed:
        return 'bene , grazie'

    if 'door' in processed:
        return 'jiji'
    if lop=="23":
       os.system('python Music.py')
    if processed and lop == "22":
        lop = "23"
        i = 0
        while (i < 80):
            holder = links[i]
            if (links[i] == "3" or links[i] == "https://www.youtube.com/results?search_query="):
                links[i] = ""
            else:
                links[i] = "link = " + holder
            i = i + 1
        i = 0
        return (links)
    if 'inizia' in processed:
        name = 'books'
        dominio = ['https://musicbrainz.org/', 'https://www.radio-italiane.it/']
        CAT_FACTS_URL = 'https://musicbrainz.org/'
        url = 'https://musicbrainz.org/'
        radioo = 'https://www.radio-italiane.it/'
        annoo = 'https://www.musicoutfitters.com/topsongs/'
        youtube = 'https://music.apple.com/us/search?term='
        classifica = 'https://www.passioninside.net/classifiche-canzoni/classifica-italiana-2023/'
        instrumental = 'https://musicbrainz.org/tag/instrumental/'
        urlartist = url
        urlradio = radioo
        urlnazione = url
        urlanno = annoo
        urlstrumento = url
        urlinstrumental = url
        urlcanto = url
        urlballo = url
        global urlserie
        global cossso
        global soccco
        global fossso
        cossso = 'yg'
        soccco = 'gy'
        fossso = 'gj'
        #global lop
        urlserie = youtube
        global urlfilm
        urlfilm = youtube
        global contenitore
        global cont
        global car
        global nome

        global cognome
        global eta
        global username
        global risposta
        global quando
        global dove
        global come
        global genere
        global periodo
        global inglese
        global lingue
        global lingue2
        global lingue3
        global lingue4
        global strumentali
        global strumentali2
        global ballo
        global ballo2
        global canto
        global canto2
        global film
        global radio
        global var
        global frequenza
        global ore
        global strumento
        global strumento2
        global serie
        global commerciale
        global hobby
        global videogiochi
        global testo
        global testo2
        global caratteristiche
        contenitore = ['1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                       '1111', '1111', '1111', '1111']
        caratteristiche = ['1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111']
        cont = 0
        car = 0
        n = random.randint(1, 242)
        faaf = 0
        #global lop
        lop="."
        return(
            "Questa app ti permette di ascoltare musica a tuo piacimento, ma prima di tutto dammi alcuni dati che ti riguardano ,seguiti da un questionario :D (Premi un tasto per continuare)")
    if processed and lop==".":
        lop = ".."
        return("Dimmi il tuo nome")
        #nome = input(" : ")
    if processed and lop=="..":
        lop = "..."
        global nome
        processed=processed.replace(" ","")
        nome=processed
        return("Dimmi il tuo cognome")
    if processed and lop == "...":
        lop = "...."
        global cognome
        cognome = processed
        return("Dimmi il tuo soprannome")
    if processed and lop == "....":
        lop = "....."
        global username
        processed = processed.replace(" ", "")
        username = processed
        global tutto
        tutto=nome + username
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            charset="utf8",
            # password="vanni1998",
            # database="Music",
            port="3306",
            # auth_plugin="caching_sha2_password",
        )
        ppp=0
        mycursor = mydb.cursor()
        mycursor.execute("USE music", )
        database_name = "Music"
        mycursor.execute("SHOW TABLES")
        tabelle = mycursor.fetchall()



        for table in tabelle:
            tabel = str(tabelle[ppp])
            tabel = tabel.replace("',)", "")
            tabel = tabel.replace("('", "")
            if (tabel==tutto):
                lop = "mo"

                return("Dati con le tue credenziali sono già presenti, vuoi utilizzarli?")
            ppp=ppp+1
        return ("Dimmi la tua età")
    if processed=="si" and lop == "mo":
        lop = "57"
        cons=""
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            charset="utf8",
            # password="vanni1998",
            # database="Music",
            port="3306",
            # auth_plugin="caching_sha2_password",
        )
        ppp = 0
        mycursor = mydb.cursor()
        mycursor.execute("USE music", )
        mycursor.execute(f"""SELECT dati_extra FROM {tutto}""")
        global extra
        extra= mycursor.fetchall()
        extra=extra+extra+extra
        return("Ok , premo un tasto per far partire la ricerca")
    if processed and lop == "57":
        i=0
        end=0
        follo=0
        cons=""
        while(i<10):
            ginger=str(extra[i])
            ginger = ginger.replace("',)", "")
            ginger = ginger.replace("('", "")
            extra[i]=ginger
            if(extra[i]==" " or "1"):
                i=i+1
            i=i+1
        i=0
        extra = extra + extra + extra
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            charset="utf8",
            # password="vanni1998",
            # database="Music",
            port="3306",
            # auth_plugin="caching_sha2_password",
        )
        ppp = 0
        mycursor = mydb.cursor()
        mycursor.execute("USE music", )
        database_name = "Music"
        mycursor.execute("SHOW TABLES")
        tabelle = mycursor.fetchall()
        for table in tabelle:
            tabel = str(tabelle[ppp])
            tabel = tabel.replace("',)", "")
            tabel = tabel.replace("('", "")
            print(tabel)
            if (tabel == tutto.lower()):
                i = 31;
            while (i < 30):
                tabel = str(tabelle[ppp])
                tabel = tabel.replace("',)", "")
                tabel = tabel.replace("('", "")
                trovare = f"""SELECT dati FROM {tabel} WHERE dati_extra like %s ORDER BY RAND() LIMIT 1"""
                ginger=str(extra[i])
                value = '%' + ginger + '%'
                mycursor.execute(trovare, (value,))
                consiglio = mycursor.fetchall()
                if (consiglio and extra[i] != " "):
                    trov = f"""SELECT dati FROM {tabel} ORDER BY RAND() LIMIT 1"""
                    mycursor.execute(trov)
                    consiglio = mycursor.fetchall()
                    while (follo != 9):
                        cons = str(consiglio)
                        print(cons)
                        cons = cons.replace("[('", "")
                        cons = cons.replace("',)]", "")
                        print(cons)
                        try:
                            fl = float(cons)
                            fuo = True
                        except ValueError:
                            fuo = False
                        print(fuo)
                        if (fuo == False and cons != " "):
                            follo = 9
                            print("falsee")
                        if (fuo == True or cons == " "):
                            trov = f"""SELECT dati FROM {tabel} ORDER BY RAND() LIMIT 1"""
                            # valu = '%' + domandine[i] + '%'
                            # tabel = str(tabelle[ppp])
                            # tabel = tabel.replace("',)", "")
                            # tabel = tabel.replace("('", "")
                            # trovare = f"""SELECT dati FROM {tabel} WHERE dati_extra like %s ORDER BY RAND() LIMIT 1"""
                            # value = '%' + domandine[i] + '%'
                            mycursor.execute(trov)
                            consiglio = mycursor.fetchall()
                            print("truee")
                    cons = cons.replace("[('", "")
                    cons = cons.replace("',)]", "")
                    print(cons)
                    end = 1
                    # endd=1
                    # ppp = ppp + 1
                    break

                i = i + 1
                if (extra[i] == " "):
                    i = 31
                # ppp=ppp+1
                # end=1
            i = 0
            ppp = ppp + 1
            if (end == 1):
                break

        i = 0;
        yout = "https://www.youtube.com/results?search_query="
        ner = yout
        yout = "link=" + ner + cons + "+music"
        yout = yout.replace(" ","+")
        lop = "77"
        return(yout,"vuoi altri consigli?")
    if processed=="si" and lop == "77":
        lop = "57"
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            charset="utf8",
            # password="vanni1998",
            # database="Music",
            port="3306",
            # auth_plugin="caching_sha2_password",
        )
        ppp = 0
        mycursor = mydb.cursor()
        mycursor.execute("USE music", )
        mycursor.execute(f"""SELECT dati_extra FROM {tutto}""")
        #global extra
        extra = mycursor.fetchall()
        return("Ok , premi un tasto per far partire la ricerca")
    if processed!="si" and lop == "77":
        lop = "23"
        return ("Ok")
    if processed!="si" and lop == "mo":
        lop = "....."
        return ("Ok, allora continuiamo ,dimmi la tua età")
    if processed and lop == ".....":
        lop = ","
        global eta
        eta = processed
        return("Ti piace la musica?")
    if processed and lop == ",":
        lop = ",,"
        global risposta
        risposta = processed
        return("Quando la ascolti?")
    if processed and lop == ",,":
            lop=",,,"
            global quando
            quando = processed
            return("Dove la ascolti?")
    if processed and lop == ",,,":
        lop = ",,,,"
        global dove
        dove = processed
        return("In Sottofondo , normale o ad alto volume?")
    if processed and lop == ",,,,":
            lop=",,,,,"
            global come
            come = processed
            return("Che genere di musica ascolti?")
    if processed and lop == ",,,,,":
        lop = "-"
        global genere
        genere = processed
        return("Quale periodo musicale preferisci?")
    if processed and lop == "-":
        lop = "--"
        global periodo
        periodo = processed
        return("Ascolti musica in lingua inglese?")
    if processed and lop == "--":
        lop = "---"
        global inglese
        inglese = processed
    if lop == "---" and inglese!="si":
        lop = "---2"
        global lingue
        lingue = processed
        return("E quale lingua preferisci?")
    if processed and lop == "---" and inglese == "si":
        lop = "---3"
        global lingue2
        lingue2 = processed
        return("Ascolti anche musica in altre lingue?")
    if processed and lop == "---3" and lingue2 == "si":
        lop = "---4"
        global lingue3
        lingue3 = processed
        return("Quale nazione in particolare?")
    if processed and lop == "---2":
        lop = "---4"
        global lingue4
        lingue4 = processed
        return("Quale nazione in particolare?")
    if processed and lop == "---4":
        lop = "---5"
        #global lingue4
        lingue4 = processed
        return("Preferisci brani strumentali?")
    if processed and lop == "---2":
        lop = "---5"
        #global lingue4
        lingue4 = processed
        return("Preferisci brani strumentali?")
    if processed=="si" and lop == "---5":
        lop = "3"
        global strumentali
        strumentali = processed
        return("Che genere?")
    if processed!="si" and lop == "---5":
        lop = "4"
        #global strumentali
        strumentali = processed
        return("Ti piace ballare?")
    if processed and lop == "3":
        lop = "4"
        #global strumentali2
        strumentali2 = processed
        return ("Ti piace ballare?")
    if processed and lop == "---5" and strumentali!="si":
        lop = "4"
        #global strumentali
        strumentali = processed
        return ("Ti piace ballare?")
    if processed=="si" and lop =="4":
        lop = "5"
        global ballo
        ballo = processed
        return ("Che Genere?")
    if processed!="si" and lop =="4":
        lop = "6"
        #global ballo
        ballo = processed
        return ("Ti piace cantare?")
    if processed and lop == "5":
        lop = "7"
        global ballo2
        ballo2 = processed
        return ("Ti piace cantare?")
    if (processed=="si" and lop == "7") or (processed=="si" and lop=="6"):
        lop = "8"
        global canto
        canto = processed
        return ("Che genere?")
    if (processed!="si" and lop == "7") or (processed!="si" and lop=="6"):
        lop = "9"
        #global canto
        canto = processed
        return ("Qual'è il tuo film preferito?")
    if processed and lop=="8":
        lop="9"
        global canto2
        canto2 = processed
        return ("Qual'è il tuo film preferito?")
    if processed and lop=="9":
        lop="10"
        global film
        film = processed
        return ("Ascolti la radio?")
    if processed and lop=="10":
        lop="11"
        global radio
        radio = processed
    if radio=="si" and lop=="11":
        lop="12"
        return ("Quale radio?")
    if radio!="si" and lop=="11":
        lop="13"
        return ("Quanto tempo al giorno ascolti la musica?")
    if processed and lop=="12":
        lop="13"
        global radio2
        radio2 = processed
        fer="radio"
        gfff=radio2
        if(fer not in radio2):
            radio2="radio " + gfff
        return ("Quanto tempo al giorno ascolti la musica?")
    if processed and lop=="13":
        lop="14"
        global ore
        ore = processed
        return ("Suoni uno strumento?")
    if processed=="si" and lop=="14":
        lop="15"
        global strumento
        strumento = processed
        return ("Quale strumento?")
    if processed!="si" and lop=="14":
        lop="16"
        #global strumento
        strumento = processed
        return ("Qual'è la tua serie (TV , streaming .ecc) preferita?")
    if processed and lop=="15":
        lop="16"
        global strumento2
        strumento2 = processed
        return ("Qual'è la tua serie (TV , streaming .ecc) preferita")
    if processed and lop=="16":
        lop="17"
        global serie
        serie = processed
        return ("Ti piace ascoltare musica commerciale , underground o entrambe?")
    if processed and lop=="17":
        lop="18"
        global commerciale
        commerciale = processed
        return ("Quali sono i tuoi hobby?")
    if processed and lop=="18":
        lop="19"
        global hobby
        hobby = processed
        return ("Per te è importate il testo di una canzone? (prima si o no e in seguito verra chiesta la motivazione)")
    if processed and lop=="19":
        lop="20"
        global testo
        testo = processed
        return ("Perchè?")
    if processed and lop=="20":
        lop="21"
        global testo2
        testo2 = processed
        app = Application.builder().token(TOKEN).build()
        #Updater.stop(Application.builder().token(TOKEN).build())
        #app.stop()
        return("Hai completato il questionario , premi un tasto per avviare la ricerca")
    if processed and lop=="21":
        global varr
        varr="7"


        __author__ = "Giovanni Campanelli"
        __author_email__ = "chrlunsf@cisco.com"
        __contributors__ = ["Brad Bester <brbester@cisco.com>"]
        __copyright__ = "Copyright (c) 2016-2020 Cisco and/or its affiliates."
        __license__ = "MIT"
        faaf = 0
        ff = 0
        fff = 0
        #global contenitore
        #global cont
        # contenitore = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','1','2','3','4','5','6','7','8','9','10']
        # cont=0
        cossso = 'yg'
        soccco = 'gy'
        fossso = 'gj'
        urlfilm = ''
        #global caratteristiche
        #global car

        from flask import Flask, request
        import requests

        from webexteamssdk import WebexTeamsAPI, Webhook
        class music(scrapy.Spider):

            name = 'books'
            dominio = ['https://musicbrainz.org/', 'https://www.radio-italiane.it/']
            CAT_FACTS_URL = 'https://musicbrainz.org/'
            url = 'https://musicbrainz.org/'
            radioo = 'https://www.radio-italiane.it/'
            annoo = 'https://www.musicoutfitters.com/topsongs/'
            youtube = 'https://music.apple.com/us/search?term='
            classifica = 'https://www.passioninside.net/classifiche-canzoni/classifica-italiana-2023/'
            instrumental = 'https://musicbrainz.org/tag/instrumental/'
            urlartist = url
            urlradio = radioo
            urlnazione = url
            urlanno = annoo
            urlstrumento = url
            urlinstrumental = url
            urlcanto = url
            urlballo = url
            global urlserie
            urlserie = youtube
            global urlfilm
            urlfilm = youtube
            global contenitore
            global cont
            global car
            global caratteristiche
            contenitore = ['1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                           '1111']
            caratteristiche = ['1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111', '1111',
                               '1111']
            cont = 0
            car = 0
            n = random.randint(1, 242)
            faaf = 0
            print(n)
            print(
                "Questa app ti permette di ascoltare musica a tuo piacimento, ma prima di tutto dammi alcuni dati che ti riguardano ,seguiti da un questionario :D")
            print("Dimmi il tuo nome")
            #nome = input(" : ")
            print("Dimmi il tuo cognome")
            #cognome = input(" : ")
            print("Dimmi il tuo sopprannome")
            #username = input(" : ")
            print("Dimmi la tua età")
            #eta = input(" : ")
            print("Ti piace la musica?")
            #risposta = input(" : ")
            if (risposta == risposta):
                print("Quando la ascolti?")
                #quando = input(" : ")
                print("Dove la ascolti?")
                #dove = input(" : ")
                print("In Sottofondo , normale o alto volume?")
                #come = input(" : ")
                print("Che genere di musica ascolti?")
                #genere = input(" : ")
                print("Quale periodo musicale preferisci?")
                #periodo = input(" : ")
                print("Ascolti musica in lingua inglese?")
                #inglese = input(" : ")
                if (inglese == "no"):
                    print("E quale lingua preferisci?")
                    #lingue = input(" : ")
                    urlnazione += 'search?query=' + lingue4 + '&type=area&method=indexed'
                if (inglese == "si"):
                    print("Ascolti anche musica in altre lingue?")
                    #lingue2 = input(" : ")
                    if (lingue2 == "si"):
                        print("Quale lingua in particolare?")
                        #lingue3 = input(" : ")
                        urlnazione += 'search?query=' + lingue4 + '&type=area&method=indexed'
                print("Preferisci brani strumentali?")
                #strumentali = input(" : ")
                if (strumentali == "si"):
                    print("Che genere?")
                    #strumentali2 = input(" : ")
                print("Ti piace ballare?")
                #ballo = input(" : ")
                if (ballo == "si"):
                    print("Quale genere di canzoni ti piace ballare?")
                    #ballo2 = input(" : ")
                print("Ti piace cantare?")
                #canto = input(" : ")
                if (canto == "si"):
                    print("Quale genere di canzoni di piace cantare?")
                    #canto2 = input(" : ")
                print("Qual'è il tuo film preferito?")
                #film = input(" : ")
                print("Ascolti la radio?")
                #radio = input(" : ")
                if (radio == "si"):
                    print("Quale frequenza?")
                    #frequenza = input(" : ")
                print("Quanto tempo al giorno ascolti musica?")
                #ore = input(" : ")
                print("Suoni uno strumento?")
                #strumento = input(" : ")
                if (strumento == "si"):
                    print("Quale strumento?")
                    #strumento2 = input(" : ")
                print("Qual'è la tua serie preferita?")
                #serie = input(" : ")
                print("Ti piace ascoltare musica commerciale , underground o entrambe?")
                #commerciale = input(" : ")
                print("Quali sono i tuoi hobby?")
                #hobby = input(" : ")
                if (hobby == "videogiochi"):
                    print("Quali videogiochi?")
                    #videogiochi = input(" : ")
                print("Per te è importante il testo di una canzone?")
                #testo = input(" : ")
                print("Perchè?")
                #testo2 = input(" : ")
            if (risposta == "no"):
                print("Quali suoni preferisci ascoltare allora?")
                #nomusic = input(" : ")

            urlartist += 'tag/' + genere + '/release?page=1'
            print(urlartist)
            if (ballo == 'si'):
                urlballo += 'tag/' + ballo2 + '/release?page=1'
            if (canto == 'si'):
                urlcanto += 'tag/' + canto2 + '/release?page=1'
            if (radio == 'si'):
                frequenza = frequenza.replace(' ', '-')
                urlradio += frequenza
                print(urlradio)

            if (strumento == 'si'):
                urlstrumento += 'search?query=' + strumento2 + '&type=instrument&limit=25&method=indexed'
            urlserie += serie
            urlserie = urlserie.replace(" ", "%20")

            urlfilm += film
            urlfilm = urlfilm.replace(" ", "%20")
            if (commerciale == 'commerciale'):
                classificar = classifica
            if (strumentali == 'si'):
                nn = str(n)
                urlinstrumental += 'search?query=' + strumentali2 + '&type=instrument&limit=25&method=indexed'

            def start_requests(self):
                f = 0
                d = str(f)
                print(d)
                # pif = URL.replace("1", "2")
                yield scrapy.Request(url=music.urlartist, callback=self.response_parser)
                yield scrapy.Request(url=music.urlradio, callback=self.response_parser)

            def response_parser(self, response):
                # print(faaf)
                artisti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                           '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                urlart = music.urlartist
                yield scrapy.Request(url=music.urlartist, callback=self.response_parser)
                for selector in response.css('nav'):
                    yield {
                        'descrizione': selector.css('p::attr(title)').extract_first(),
                        'price': selector.css('p::text').extract()
                    }
                    num = selector.css('ul > li > a::text').extract()[4]
                    print(num)
                    numm = int(num)
                    print(numm)
                    nnn = random.randint(1, numm)
                    randompage1 = random.randint(0, 99)
                    randompage2 = random.randint(0, 99)
                    print(nnn)
                    st = str(nnn)
                music.urlartist = music.urlartist.replace("1", st)
                pif = music.urlartist
                print('prova')
                s = 1
                i = 0
                k = 0
                # while i < 1:
                f = s - 1
                d = str(f)
                dd = str(s)
                i = i + 1
                s = s + 1
                alessandro = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                              '22', '23',
                              '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11',
                              '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28',
                              '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                              '22', '23',
                              '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11',
                              '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28',
                              '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                              '22', '23',
                              '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11',
                              '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28',
                              '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                              '22', '23',
                              '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11',
                              '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28',
                              '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                              '4', '5', '6',
                              '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                              '22', '23',
                              '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11',
                              '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28',
                              '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
                fof = 2
                if (commerciale == "commerciale"):
                    music.urlartist = urlart
                yield scrapy.Request(url=music.urlartist, callback=self.response_parser)
                for selector in response.css('ul > li > a'):
                    yield {
                        'descrizione': selector.css('a::attr(title)').extract_first(),

                        'price': selector.css('bdi::text').extract_first()
                    }
                    # print(artisti[k])
                    if (k <= 200 and selector.css('bdi::text').extract_first() != None and selector.css(
                            'a::attr(title)').extract_first() != None):
                        artisti[k] = selector.css('bdi::text').extract_first(),
                        print(artisti[k])
                        k = k + 1

                # next_page_link = response.css('li.next a::attr(href)').extract_first()
                # if next_page_link:
                # yield response.follow(next_page_link, callback=self.response_parser)
                # i = i + 1
                # s = s + 1

                print("ecco a te: ")
                print(artisti[randompage1])
                print(artisti[randompage2])
                global contenitore
                global cont
                global caratteristiche
                global car
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "genere " + ";;" + genere + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage1]
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "genere " + ";;" + genere + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage2]
                faaf = 4
                print(faaf)

            # def book_spider_result():
            # books_results = []

            # def crawler_results(item):
            # books_results.append(item)

            # dispatcher.connect(crawler_results, signal=signals.item_scraped)
            # crawler_process = CrawlerProcess()
            # crawler_process.crawl(music)
            # crawler_process.start()
            # return books_results

            # if __name__ == '__main__':
            # books_data = book_spider_result()

            # keys = books_data[0].keys()
            # with open('books_data.csv', 'w', newline='') as output_file_name:
            # writer = csv.DictWriter(output_file_name, keys)
            # writer.writeheader()
            # writer.writerows(books_data)

            def closed(self, reason):
                # Esegui azioni alla fine del spider, ad esempio, operazioni di pulizia
                self.logger.info(f"Spider chiuso per la seguente ragione: {reason}")

        class RadioRadio(scrapy.Spider):

            name = 'books'
            global cont
            global contenitore

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url=music.urlradio, callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                rad = 1
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']
                print(music.urlradio)
                yield scrapy.Request(url=music.urlradio, callback=self.response_parser)
                for selector in response.css('p'):
                    yield {
                        'descrizione': selector.css('p::text').extract_first(),
                        'price': selector.css('p::text').extract_first()
                    }
                    if (j <= 50 and selector.css('p::text').extract_first() != None and selector.css(
                            'p::text').extract_first() != ' '):
                        braniradio[j] = selector.css('p::text').extract_first(),
                        boool = False
                        dff = tuple
                        dff = 'Ultimi 7 giorni:'
                        boool = dff in braniradio[j]
                        if boool is True:
                            rad = rad + 1
                        if rad == 3 or rad == 4:
                            global contenitore
                            global cont
                            global caratteristiche
                            global car
                            print(braniradio[j])
                            cont = cont + 1
                            con = str(cont)
                            caratteristiche[car] = "radio " + ";;" + frequenza + "___" + con
                            car = car + 1
                            contenitore[cont] = braniradio[j]
                            rad = rad + 1
                        if rad == 2:
                            rad = rad + 1
                        # print(braniradio[j])
                        j = j + 1

                next_page_link = response.css('li.next a::attr(href)').extract_first()
                if next_page_link:
                    yield response.follow(next_page_link, callback=self.response_parser)
                    # i = i + 1
                    # s = s + 1
                print("radio")

        class canto(scrapy.Spider):
            name = 'book'
            global cont

            def start_requests(self):
                f = 0
                d = str(f)
                print(d)
                # pif = URL.replace("1", "2")
                yield scrapy.Request(url=music.urlcanto, callback=self.response_parser)
                # yield scrapy.Request(url=music.urlradio, callback=self.response_parser)

            def response_parser(self, response):
                artisti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                           '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
                # print(faaf)
                yield scrapy.Request(url=music.urlcanto, callback=self.response_parser)
                for selector in response.css('nav'):
                    yield {
                        'descrizione': selector.css('p::attr(title)').extract_first(),
                        'price': selector.css('p::text').extract()
                    }
                    num = selector.css('ul > li > a::text').extract()[4]
                    print(num)
                    numm = int(num)
                    print(numm)
                    nnn = random.randint(1, numm)
                    randompage1 = random.randint(0, 99)
                    randompage2 = random.randint(0, 99)
                    print(nnn)
                    st = str(nnn)

                pif = music.urlartist
                print('prova')
                s = 1
                i = 0
                k = 0
                while i < 1:
                    f = s - 1
                    d = str(f)
                    dd = str(s)
                    music.urlcanto = music.urlcanto.replace("1", st)
                    i = i + 1
                    s = s + 1
                    yield scrapy.Request(url=music.urlcanto, callback=self.response_parser)
                    for selector in response.css('ul > li > a'):
                        yield {
                            'descrizione': selector.css('a::attr(title)').extract_first(),

                            'price': selector.css('bdi::text').extract_first()
                        }
                        if (k <= 200 and selector.css('bdi::text').extract_first() != None and selector.css(
                                'a::attr(title)').extract_first() != None):
                            artisti[k] = selector.css('bdi::text').extract_first(),
                            print(artisti[k])
                            k = k + 1
                # next_page_link = response.css('li.next a::attr(href)').extract_first()
                # if next_page_link:
                # yield response.follow(next_page_link, callback=self.response_parser)
                # i = i + 1
                # s = s + 1

                print("ecco a te: ")
                print(artisti[randompage1])
                print(artisti[randompage2])
                global cont
                global contenitore
                global caratteristiche
                global car
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "canto " + ";;" + canto2 + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage1]
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "canto " + ";;" + canto2 + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage2]

        class ballo(scrapy.Spider):

            name = 'book'
            global cont

            def start_requests(self):
                f = 0
                d = str(f)
                print(d)
                # pif = URL.replace("1", "2")
                yield scrapy.Request(url=music.urlballo, callback=self.response_parser)
                # yield scrapy.Request(url=music.urlradio, callback=self.response_parser)

            def response_parser(self, response):
                artisti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                           '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                           '5', '6',
                           '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                           '23',
                           '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                           '11',
                           '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                           '27', '28',
                           '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
                # print(faaf)
                yield scrapy.Request(url=music.urlballo, callback=self.response_parser)
                for selector in response.css('nav'):
                    yield {
                        'descrizione': selector.css('p::attr(title)').extract_first(),
                        'price': selector.css('p::text').extract()
                    }
                    num = selector.css('ul > li > a::text').extract()[4]
                    print(num)
                    numm = int(num)
                    print(numm)
                    nnn = random.randint(1, numm)
                    randompage1 = random.randint(0, 99)
                    randompage2 = random.randint(0, 99)
                    print(nnn)
                    st = str(nnn)

                pif = music.urlartist
                print('prova')
                s = 1
                i = 0
                k = 0
                while i < 1:
                    f = s - 1
                    d = str(f)
                    dd = str(s)
                    music.urlballo = music.urlballo.replace("1", st)
                    i = i + 1
                    s = s + 1
                    yield scrapy.Request(url=music.urlballo, callback=self.response_parser)
                    for selector in response.css('ul > li > a'):
                        yield {
                            'descrizione': selector.css('a::attr(title)').extract_first(),

                            'price': selector.css('bdi::text').extract_first()
                        }
                        if (k <= 200 and selector.css('bdi::text').extract_first() != None and selector.css(
                                'a::attr(title)').extract_first() != None):
                            artisti[k] = selector.css('bdi::text').extract_first(),
                            print(artisti[k])
                            k = k + 1
                # next_page_link = response.css('li.next a::attr(href)').extract_first()
                # if next_page_link:
                # yield response.follow(next_page_link, callback=self.response_parser)
                # i = i + 1
                # s = s + 1

                print("ecco a te: ")
                print(artisti[randompage1])
                print(artisti[randompage2])
                global contenitore
                global cont
                global caratteristiche
                global car
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "ballo " + ";;" + ballo2 + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage1]
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "ballo " + ";;" + ballo2 + "___" + con
                car = car + 1
                contenitore[cont] = artisti[randompage2]

        class Strumento(scrapy.Spider):
            global cossso
            coso = ''
            name = 'books'
            varr = ''

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url=music.urlstrumento, callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                foffo = 0
                rad = 1
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']
                print(music.urlstrumento)

                yield scrapy.Request(url=music.urlstrumento, callback=self.response_parser)
                for selector in response.css('td'):
                    yield {
                        'descrizione': selector.css('td > a::attr(href)').extract_first(),
                        'price': selector.css('td > a::attr(href)').extract_first()
                    }
                    if (j <= 100 and selector.css('td > a::attr(href)').extract_first() != None and selector.css(
                            'td > a::attr(href)').extract_first() != ' '):
                        braniradio[j] = selector.css('td > a::attr(href)').extract_first(),
                        print(braniradio[j])
                        j = j + 1
                print(braniradio[0])
                braniradio[0] = str(braniradio[0])
                Strumento.coso = music.url + braniradio[0] + '/releases?page=1'
                Strumento.coso = Strumento.coso.replace("('/", "")
                Strumento.coso = Strumento.coso.replace("',)", "")
                print(Strumento.coso)
                # with open(self, response) as f:
                # pickle.dump(coso)
                next_page_link = response.css('li.next a::attr(href)').extract_first()
                if next_page_link:
                    yield response.follow(next_page_link, callback=self.response_parser)
                    # i = i + 1
                    # s = s + 1
                print("rao")
                cosi = str(Strumento.coso)
                print(cosi)
                print(Strumento.coso)
                global cossso
                meta = {Strumento.coso: cossso}
                cossso = Strumento.coso
                print(cossso)
                return cossso

            def __str__(self):
                global cossso
                return cossso

            def roba(self, response):
                var = Strumento()
                global cossso
                cossso = response.meta.get(Strumento.coso)
                print(cossso)
                print("sssss")
                # return cossso

        class Lingua(scrapy.Spider):
            global soccco
            coso = str

            name = 'books'
            global cont
            cont = cont + 2

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                print('frr')
                print(cossso)
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url=music.urlnazione, callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                rad = 1
                print("dsd")
                # cosso = Strumento2.coso.response_parser(response)
                # print(cosso)
                # cs=list(cosso)
                # string_list = [str(element) for element in cosso]
                delimiter = ", "
                # result_string = delimiter.join(string_list)
                # print(string_list)
                # cs = str(cosso)
                # print(''.join(cs))
                # print(cs)
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']
                print(music.urlnazione)
                yield scrapy.Request(url=music.urlnazione, callback=self.response_parser)
                for selector in response.css('td'):
                    yield {
                        'descrizione': selector.css('a::attr(href)').extract_first(),
                        'price': selector.css('a::attr(href)').extract_first()
                    }
                    if (j <= 100 and selector.css('a::attr(href)').extract_first() != None and selector.css(
                            'a::attr(href)').extract_first() != ' '):
                        braniradio[j] = selector.css('a::attr(href)').extract_first(),
                        print(braniradio[j])
                        j = j + 1
                print(braniradio[0])
                braniradio[0] = str(braniradio[0])
                coso = music.url + braniradio[0] + '/releases?page=1'
                coso = coso.replace("('/", "")
                coso = coso.replace("',)", "")
                print(coso)
                print(cossso)
                print("pop")
                cosso = Strumento2.coso.response_parser(response)
                # ",".join(str(cosso) for cosso in response_parser(response).childern)
                print(cosso)
                global soccco
                soccco = coso
                return soccco

                # next_page_link = response.css('li.next a::attr(href)').extract_first()
                # if next_page_link:
                # yield response.follow(next_page_link, callback=self.response_parser)
                # i = i + 1
                # s = s + 1
                # print("raio")

        class Strumento2(scrapy.Spider):
            # global cossso
            # coso=functools.reduce(operator.add, (Strumento.coso))
            # coso=str(Strumento.coso)
            name = 'book'
            st = ''
            # response=None
            coso = Strumento()
            cosso = ''
            print(Strumento().__str__())
            # coso=coso.roba()
            # print(Strumento())

            # coso=Str
            # coso=cosso.coso
            print('sddd')

            # coso = coso.roba()
            # print(cosso)
            # music.cont = music.cont + 2
            def start_requests(self):
                f = 0
                d = str(f)
                print(d)
                # pif = URL.replace("1", "2")
                global cossso
                coo = Strumento.cossso
                print("cosso")
                yield scrapy.Request(url=cossso, callback=self.response_parser)
                # yield scrapy.Request(url=music.urlradio, callback=self.response_parser)

            def response_parser(self, response):
                # print(faaf)
                cosso = Strumento2.coso.roba(response)
                global cossso
                yield scrapy.Request(url=cossso, callback=self.response_parser)
                for selector in response.css('nav'):
                    yield {
                        'descrizione': selector.css('p::attr(title)').extract_first(),
                        'price': selector.css('p::text').extract()
                    }
                    num = selector.css('ul > li > a::text').extract()[4]
                    print(num)
                    numm = int(num)
                    print(numm)
                    nnn = random.randint(1, numm)
                    randompage1 = random.randint(0, 99)
                    randompage2 = random.randint(0, 99)
                    print(nnn)
                    st = '=' + str(nnn)

                pif = music.urlartist
                print('prova')
                s = 1
                i = 0
                k = 0
                artisti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                           '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3',
                           '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                           '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
                           '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8',
                           '9', '10', ]
                artisti2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                            '18',
                            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4',
                            '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                            '23',
                            '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                            '11',
                            '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                            '27', '28',
                            '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
                while i < 1:
                    f = s - 1
                    d = str(f)
                    dd = str(s)
                    sooo = Strumento().__str__()
                    cossso = cossso.replace("=1", st)
                    i = i + 1
                    s = s + 1
                    yield scrapy.Request(url=cossso, callback=self.response_parser)
                    for selector in response.css('tr'):
                        yield {
                            'descrizione': selector.css('tr > td > a > bdi::text').extract_first(),

                            'price': selector.css('td > a > bdi::text').extract_first()
                        }
                        if (k <= 100 and selector.css(
                                'tr > td > a > bdi::text').extract_first() != None and selector.css(
                                'td > a > bdi::text').extract_first() != None):
                            artisti[k] = selector.css('tr > td > a > bdi::text').extract_first(),
                            artisti2[k] = selector.css('td > a > bdi::text').extract_first(),
                            print(artisti[k])
                            print(artisti2[k])
                            k = k + 1
                # next_page_link = response.css('li.next a::attr(href)').extract_first()
                # if next_page_link:
                # yield response.follow(next_page_link, callback=self.response_parser)
                # i = i + 1
                # s = s + 1

                print("ecco a te: ")
                print(artisti[randompage1])
                print(artisti2[randompage1])
                print(artisti[randompage2])
                print(artisti2[randompage2])
                artista_completo = artisti2[randompage1] + ' - ' + artisti[randompage1]
                print(artista_completo)
                artista_completo2 = artisti2[randompage2] + ' - ' + artisti[randompage2]
                print(artista_completo2)
                # music.contenitore[music.cont] = artista_completo
                # music.contenitore[music.cont + 1] = artista_completo2

        class Anni(scrapy.Spider):

            name = 'books'
            global cont
            cont = cont + 2
            a50 = "50" in periodo
            a60 = "60" in periodo
            a70 = "70" in periodo
            a80 = "80" in periodo
            a90 = "90" in periodo
            a2000 = "2000" in periodo
            a2010 = "2010" in periodo
            amoderno = "attuale" in periodo

            if (a50 == True):
                nnn50 = random.randint(1950, 1959)
                nn50 = str(nnn50)
                print(nn50)
                music.urlanno += nn50 + ".htm"
            if (a60 == True):
                nnn60 = random.randint(1960, 1969)
                nn60 = str(nnn60)
                print(nn60)
                music.urlanno += nn60 + ".htm"
            if (a70 == True):
                nnn70 = random.randint(1970, 1979)
                nn70 = str(nnn70)
                print(nn70)
                music.urlanno += nn70 + ".htm"
            if (a80 == True):
                nnn80 = random.randint(1980, 1989)
                nn80 = str(nnn80)
                print(nn80)
                music.urlanno += nn80 + ".htm"
            if (a90 == True):
                nnn90 = random.randint(1990, 1999)
                nn90 = str(nnn90)
                print(nn90)
                music.urlanno += nn90 + ".htm"
            if (a2000 == True):
                nnn2000 = random.randint(2000, 2009)
                nn2000 = str(nnn2000)
                print(nn2000)
                music.urlanno += nn2000 + ".htm"
            if (a2010 == True):
                nnn2010 = random.randint(2010, 2019)
                nn2010 = str(nnn2010)
                print(nn2010)
                music.urlanno += nn2010 + ".htm"
            if (amoderno == True):
                nnnmoderno = random.randint(2020, datetime.date.today().year)
                nnmoderno = str(nnnmoderno)
                print(nnmoderno)
                music.urlanno += nnmoderno + ".htm"

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url="https://www.musicoutfitters.com/", callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                rad = 1
                contatti = ''
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']

                print(music.urlanno)
                yield scrapy.Request(url=music.urlanno, callback=self.response_parser)
                for selector in response.css('li'):
                    yield {
                        'descrizione': selector.css('a::text').extract_first(),
                        'price': selector.css('a::text').extract_first()
                    }
                    if (j <= 130 and selector.css('a::text').extract_first() != None and selector.css(
                            'p::text').extract_first() != ' '):
                        braniradio[j] = selector.css('a::text').extract_first(),
                        # print(braniradio[j])
                        j = j + 1
                        if (braniradio[j] == "('Contact Us',)"):
                            contatti = "us"
                            rad = j
                randompage = random.randint(rad, rad + 100)
                print("pagina")
                print(braniradio[randompage])
                global cont
                global contenitore
                global caratteristiche
                global car
                cont = cont + 1
                con = str(cont)
                caratteristiche[car] = "anni " + ";;" + periodo + "___" + con
                car = car + 1
                contenitore[cont] = braniradio[randompage]

                next_page_link = response.css('li.next a::attr(href)').extract_first()
                if next_page_link:
                    yield response.follow(next_page_link, callback=self.response_parser)
                    # i = i + 1
                    # s = s + 1
                print("radio")

        class Film(scrapy.Spider):

            name = 'books'

            # music.cont=music.cont+2

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url=urlfilm, callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                rad = 1
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']
                print(music.urlfilm)
                yield scrapy.Request(url=urlfilm, callback=self.response_parser)
                for selector in response.css('a'):
                    yield {
                        'descrizione': selector.css('a::text').extract_first(),
                        'price': selector.css('a::text').extract_first()
                    }
                    if (j <= 150 and selector.css('a::text').extract_first() != None and selector.css(
                            'a::text').extract_first() != ' '):
                        braniradio[j] = selector.css('a::text').extract_first(),
                        boool = False
                        dff = tuple
                        dff = 'Ultimi 7 giorni:'
                        boool = dff in braniradio[j]
                        if boool is True:
                            rad = rad + 1
                        if rad == 3 or rad == 4:
                            print(braniradio[j])
                            music.contenitore[music.cont] = braniradio[j]
                            rad = rad + 1
                            music.cont = music.cont + 1
                        if rad == 2:
                            rad = rad + 1
                        print(braniradio[j])
                        j = j + 1

                next_page_link = response.css('li.next a::attr(href)').extract_first()
                if next_page_link:
                    yield response.follow(next_page_link, callback=self.response_parser)
                    # i = i + 1
                    # s = s + 1
                print("radio")

        class Instrumental(scrapy.Spider):
            global fossso
            coso = ''
            name = 'books'
            varr = ''
            global cont
            cont = cont + 2

            def start_requests(self):
                # pif = URL.replace("1", "2")
                process = CrawlerProcess()
                process.start(install_signal_handlers=False)
                yield scrapy.Request(url=music.urlinstrumental, callback=self.response_parser)

            def response_parser(self, response):
                j = 0
                foffo = 0
                rad = 1
                print('aaa')
                braniradio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                              '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                              '10', '11', '12', '13', '14', '15', '16', '17',
                              '18',
                              '19', '20', '21', '22', '23', '24', '25']
                print(music.urlstrumento)

                yield scrapy.Request(url=music.urlinstrumental, callback=self.response_parser)
                for selector in response.css('td'):
                    yield {
                        'descrizione': selector.css('a::attr(href)').extract_first(),
                        'price': selector.css('a::attr(href)').extract_first()
                    }
                    if (j <= 100 and selector.css('a::attr(href)').extract_first() != None and selector.css(
                            'a::attr(href)').extract_first() != ' '):
                        braniradio[j] = selector.css('a::attr(href)').extract_first(),
                        print(braniradio[j])
                        j = j + 1
                print(braniradio[0])
                braniradio[0] = str(braniradio[0])
                Strumento.coso = music.url + braniradio[0] + '/releases?page=1'
                Strumento.coso = Strumento.coso.replace("('/", "")
                Strumento.coso = Strumento.coso.replace("',)", "")
                print(Strumento.coso)
                # with open(self, response) as f:
                # pickle.dump(coso)
                next_page_link = response.css('li.next a::attr(href)').extract_first()
                if next_page_link:
                    yield response.follow(next_page_link, callback=self.response_parser)
                    # i = i + 1
                    # s = s + 1
                print("rao")
                cosi = str(Strumento.coso)
                print(cosi)
                print(Strumento.coso)
                global fossso
                meta = {Strumento.coso: fossso}
                fossso = Strumento.coso
                print(fossso)
                return fossso

            def __str__(self):
                global cossso
                return cossso

            def roba(self, response):
                var = Strumento()
                global cossso
                cossso = response.meta.get(Strumento.coso)
                print(cossso)
                print("sssss")
                # return cossso

        def book_spider_result():
            books_results = []

            def crawler_results(item):
                books_results.append(item)

            dispatcher.connect(crawler_results, signal=signals.item_scraped)
            crawler_process = CrawlerProcess()
            crawler_process.crawl(music)
            crawler_process.crawl(RadioRadio)
            crawler_process.crawl(canto)
            crawler_process.crawl(ballo)
            crawler_process.crawl(Anni)
            crawler_process.crawl(Film)
            crawler_process.crawl(Instrumental)
            crawler_process.crawl(Strumento)
            crawler_process.crawl(Strumento2)
            crawler_process.crawl(Lingua)
            crawler_process.start()
            return books_results

            # def parse_error(self, failure):
            # self.logger.error(f"Errore durante la richiesta: {failure.getErrorMessage()}")

        if __name__ == '__main__':
            books_data = book_spider_result()
            keys = books_data[0].keys()
            with open('books_data.csv', 'w', newline='') as output_file_name:
                writer = csv.DictWriter(output_file_name, keys)
                writer.writeheader()
                print(cossso)
                print("separatore")
                print(soccco)
                print("sep")
                print(fossso)
        i = 0
        numeretti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        song1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        song2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        song3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                 '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                 '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        punteggia = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                     '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                     '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                     '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                     '28',
                     '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        punteggia4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        punteggia5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        punteggia6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        punteggia7 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                      '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5',
                      '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
                      '24', '25', '26', '27', '28', '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                      '28',
                      '29', '30', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        if (cossso != 'https://musicbrainz.org/1/releases?page=1'):

            with urlopen(cossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('li'):
                    numeretti[i] = anchor.text
                    # print(anchor.text)
                    i = i + 1
            print('jojojo')
            print(numeretti[69])
            try:
                numm = int(numeretti[69])
                sessanove = ''
                num = random.randint(0, numm)
                numer = str(num)
                print(num)
                classina = ''
                sessanove += '=' + numer
                cossso = cossso.replace("=1", sessanove)
            except:
                numm = 0
                numm = numm
            i = 0
            with urlopen(cossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('tr'):
                    song1[i] = anchor.text
                    prov = anchor.find_next_sibling()
                    ghio = str(prov)
                    # print(prov)
                    corrispondenza = re.search(r'title="(.+?)"><bdi>', ghio)
                    corrispo = re.search(r'ity" title="(.+?)"><bdi>', ghio)
                    corr = re.search(r'<bdi>"(.+?)"></bdi></a>', ghio)
                    if corrispo:
                        if corr:
                            punteggia[i] = corr.group(1)
                            # print(punteggia[i])
                    else:
                        if corrispondenza:
                            punteggia[i] = corrispondenza.group(1)
                        # print(punteggia[i])
                    # print(i)
                    # print(anchor.text)
                    i = i + 1
                # print(anchor.get('bdi::text','/'))
            i = 0
            print("vanno")
            with urlopen(cossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('a'):
                    # print(anchor.title)
                    if (anchor.get('title') != None):
                        song1[i] = anchor.text
                        # print(anchor.get('title'))
                        i = i + 1
            print("td")
            with urlopen(cossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('td', role='cell'):
                    # print(anchor.title)
                    if (anchor.text != None):
                        # print(anchor.text)
                        i = i + 1
            i = 0
            j = 0
            nu = random.randint(0, 99)
            nu1 = nu + 1
            nu2 = nu + 2
            index = "Digital Media"
            ffff = song1[nu].find(index)
            song1[nu] = song1[nu][:ffff]
            if (ffff == -1):
                index = "CD"
                ffff = song1[nu].find(index)
                song1[nu] = song1[nu][:ffff]
            song_stru = song1[nu] + " - " + punteggia[nu - 1]
            print(song_stru)
            #global cont
            #global contenitore
            #global caratteristiche
            #global car
            cont = cont + 1
            con = str(cont)
            caratteristiche[car] = "strumento " + ";;" + strumento2 + "___" + con
            car = car + 1
            contenitore[cont] = song_stru
        if (soccco != 'https://musicbrainz.org/1/releases?page=1'):
            with urlopen(soccco) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('li'):
                    numeretti[i] = anchor.text
                    # print(anchor.text)
                    i = i + 1
            print('jojojo')
            print(numeretti[74])
            if (numeretti[74] == "Next"):
                numm = int(numeretti[73])
            else:
                numm = int(numeretti[74])
            sessanove = ''
            num = random.randint(0, numm)
            numer = str(num)
            print(num)
            classina = ''
            sessanove += '=' + numer
            soccco = soccco.replace("=1", sessanove)
            i = 0

            with urlopen(soccco) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('tr'):
                    song1[i] = anchor.text
                    prov = anchor.find_next_sibling()
                    ghio = str(prov)
                    # print(prov)
                    corrispondenza = re.search(r'title="(.+?)"><bdi>', ghio)
                    corrispo = re.search(r'ity" title="(.+?)"><bdi>', ghio)
                    corr = re.search(r'<bdi>"(.+?)"></bdi></a>', ghio)
                    if corrispo:
                        if corr:
                            punteggia[i] = corr.group(1)
                        # print(punteggia[i])
                    else:
                        if corrispondenza:
                            punteggia[i] = corrispondenza.group(1)
                        # print(punteggia[i])
                    # print(i)
                    # print(anchor.text)
                    i = i + 1
            nu = random.randint(0, 99)
            nu1 = nu + 1
            nu2 = nu + 2
            index = "Digital Media"
            ffff = song1[nu].find(index)
            song1[nu] = song1[nu][:ffff]
            if (ffff == -1):
                index = "CD"
                ffff = song1[nu].find(index)
                song1[nu] = song1[nu][:ffff]
            song_naz = song1[nu] + " - " + punteggia[nu - 1]
            print("nazione")
            print(song_naz)
            # global cont
            # global contenitore
            # global caratteristiche
            # global car
            cont = cont + 1
            con = str(cont)
            caratteristiche[car] = "nazione " + ";;" + lingue3 + "___" + con
            car = car + 1
            contenitore[cont] = song_naz
        print(urlfilm)
        i = 0
        with urlopen(urlfilm) as response:
            soup = BeautifulSoup(response, 'html.parser')
            for anchor in soup.find_all('a'):
                punteggia4[i] = anchor.text
                # print(i)
                # print(anchor.text)
                i = i + 1
                if (i == 100):
                    break
        # global caratteristiche
        # global car
        canz_film1 = punteggia4[27] + " - " + punteggia4[26]
        canz_film2 = punteggia4[29] + " - " + punteggia4[28]
        print(canz_film1)
        print(canz_film2)
        cont = cont + 1
        con = str(cont)
        caratteristiche[car] = "film " + ";;" + film + "___" + con
        car = car + 1
        contenitore[cont] = canz_film1
        cont = cont + 1
        con = str(cont)
        caratteristiche[car] = "film " + ";;" + film + "___" + con
        car = car + 1
        contenitore[cont] = canz_film2
        i = 0
        with urlopen(urlserie) as response:
            soup = BeautifulSoup(response, 'html.parser')
            for anchor in soup.find_all('a'):
                punteggia5[i] = anchor.text
                # print(i)
                # print(anchor.text)
                i = i + 1
                if (i == 200):
                    break
        canz_serie1 = punteggia5[27] + " - " + punteggia5[26]
        canz_serie2 = punteggia5[29] + " - " + punteggia5[28]
        print(canz_serie1)
        print(canz_serie2)
        # global cont
        # global contenitore
        # global caratteristiche
        # global car
        cont = cont + 1
        con = str(cont)
        caratteristiche[car] = "serie " + ";;" + serie + "___" + con
        car = car + 1
        contenitore[cont] = canz_serie1
        cont = cont + 1
        con = str(cont)
        caratteristiche[car] = "serie " + ";;" + serie + "___" + con
        car = car + 1
        contenitore[cont] = canz_serie2

        print("strumentix")
        if (fossso != 'https://musicbrainz.org/1/releases?page=1'):

            with urlopen(fossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('li'):
                    numeretti[i] = anchor.text
                    # print(anchor.text)
                    if (i == 150):
                        break
                    i = i + 1
            print('jojojo')
            if (numeretti[63] == "1"):
                print(numeretti[69])
                numm = int(numeretti[69])
                sessanove = ''
                num = random.randint(0, numm)
                numer = str(num)
                print(num)
                classina = ''
                sessanove += '=' + numer
                fossso = fossso.replace("=1", sessanove)
            i = 0
            with urlopen(fossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('tr'):
                    song1[i] = anchor.text
                    prov = anchor.find_next_sibling()
                    ghio = str(prov)
                    # print(prov)
                    corrispondenza = re.search(r'title="(.+?)"><bdi>', ghio)
                    corrispo = re.search(r'ity" title="(.+?)"><bdi>', ghio)
                    corr = re.search(r'<bdi>"(.+?)"></bdi></a>', ghio)
                    if corrispo:
                        if corr:
                            punteggia6[i] = corr.group(1)
                            # print(punteggia[i])
                    else:
                        if corrispondenza:
                            punteggia6[i] = corrispondenza.group(1)
                        # print(punteggia[i])
                    # print(i)
                    # print(anchor.text)
                    i = i + 1
                # print(anchor.get('bdi::text','/'))
            i = 0
            print("vanno")
            with urlopen(fossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('a'):
                    # print(anchor.title)
                    if (anchor.get('title') != None):
                        song2[i] = anchor.text
                        # print(anchor.get('title'))
                        i = i + 1
            print("td")
            with urlopen(fossso) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor in soup.find_all('td', role='cell'):
                    # print(anchor.title)
                    if (anchor.text != None):
                        # print(anchor.text)
                        i = i + 1
            i = 0
            j = 0
            nu = random.randint(0, 99)
            nu1 = nu + 1
            nu2 = nu + 2
            index = "Digital Media"
            ffff = song1[nu].find(index)
            song1[nu] = song1[nu][:ffff]
            if (ffff == -1):
                index = "CD"
                ffff = song1[nu].find(index)
                song1[nu] = song1[nu][:ffff]
            song_stru = song1[nu]
            print(song_stru)
            # global cont
            # global contenitore
            # global caratteristiche
            # global car
            cont = cont + 1
            con = str(cont)
            caratteristiche[car] = "instrumental " + ";;" + strumentali2 + "___" + con
            car = car + 1
            contenitore[cont] = song_stru
            print("end")
        i = 0
        sottostr = "('"
        sottostr2 = '("'
        sottostr3 = "(' "
        virgoletta1 = "'"
        virgoletta2 = '"'
        virgoletta3 = '’'
        trat = "‐"
        kol = ""
        while (i < 50):
            kol = str(contenitore[i])
            virgcheck1 = 0
            virgcheck2 = 0
            sot = sottostr in kol
            sot2 = sottostr2 in kol
            sot3 = sottostr3 in kol
            virgo1 = virgoletta1 in kol
            virgo2 = virgoletta2 in kol
            virgo3 = virgoletta3 in kol
            tratt = trat in kol
            if sot is True:
                kol = kol.replace("('", "")
                kol = kol.replace("',)", "")
                contenitore[i] = kol
            if sot2 is True:
                kol = kol.replace('("', "")
                kol = kol.replace('",)', "")
                contenitore[i] = kol
            if sot3 is True:
                kol = kol.replace("(' ", "")
                contenitore[i] = kol
            if virgo1 is True:
                kol = kol.replace("'", "\\'")
                contenitore[i] = kol
                virgcheck1 = 1
            if virgo2 is True:
                kol = kol.replace('"', '\\"')
                contenitore[i] = kol
                virgcheck1 = 1
            if virgo3 is True:
                kol = kol.replace('’', '\\’')
                contenitore[i] = kol
                virgcheck1 = 1
            if tratt is True:
                kol = kol.replace('‐', '-')
                contenitore[i] = kol
                virgcheck1 = 1
            lingua = "en"
            o = 0
            while (o != 6):
                kol = str(contenitore[i])
                try:
                    lingua = detect(kol)
                    # Traduttore = tra.Client()
                    # print("falla")
                    # kol = Traduttore.translate(kol, source_language=lingua, target_language='en')
                    # contenitore[i] = kol
                except lang_detect_exception.LangDetectException:
                    o = 6
                    # i=i+1
                    kol = contenitore[i]
                    sot = sottostr in kol
                    sot2 = sottostr2 in kol
                    sot3 = sottostr3 in kol

                    if sot is True:
                        kol = kol.replace("('", "")
                        kol = kol.replace("',)", "")
                        contenitore[i] = kol
                    if sot2 is True:
                        kol = kol.replace('("', "")
                        kol = kol.replace('",)', "")
                        contenitore[i] = kol
                    lingua = "en"
                if (
                        lingua == "ja" or lingua == "zh-cn" or lingua == "zh-tw" or lingua == "ko" or lingua == "ru" or lingua == "ar" or lingua == "gr" or lingua == "lv" or lingua == "bg"):
                    o = 4
                    contenitore[i] = " "
                    i = i + 1
                else:
                    # print(contenitore[i])
                    lingua = "en"
                    # i = i + 1
                    o = 6
                    kol = contenitore[i]
                    sot = sottostr in kol
                    sot2 = sottostr2 in kol
                    sot3 = sottostr3 in kol
                    if sot is True:
                        kol = kol.replace("('", "")
                        kol = kol.replace("',)", "")
                        contenitore[i] = kol
                    if sot2 is True:
                        kol = kol.replace('("', "")
                        kol = kol.replace('",)', "")
                        contenitore[i] = kol
                    if sot3 is True:
                        kol = kol.replace("(' ", "")
                        contenitore[i] = kol
                    if (virgcheck1 != 1):
                        if virgo1 is True and virgcheck1 != 1:
                            kol = kol.replace("'", "\\'")
                            contenitore[i] = kol
                    if (virgcheck2 != 1):
                        if virgo2 is True and virgcheck1 != 1:
                            kol = kol.replace('"', '\\"')
                            contenitore[i] = kol
                print(contenitore[i])
                if (o == 0 or o == 6):
                    kol = contenitore[i]
                    sot = sottostr in kol
                    sot2 = sottostr2 in kol
                    sot3 = sottostr3 in kol
                    if sot is True:
                        kol = kol.replace("('", "")
                        kol = kol.replace("',)", "")
                        contenitore[i] = kol
                    if sot2 is True:
                        kol = kol.replace('("', "")
                        kol = kol.replace('",)', "")
                        contenitore[i] = kol
                    if sot3 is True:
                        kol = kol.replace("(' ", "")
                        kol = kol.replace("',)", "")
                        contenitore[i] = kol
                kol = str(contenitore[i])
                virgcheck1 = 0
                virgcheck2 = 0
                sot = sottostr in kol
                sot2 = sottostr2 in kol
                sot3 = sottostr3 in kol
                virgo1 = virgoletta1 in kol
                virgo2 = virgoletta2 in kol
                virgo3 = virgoletta3 in kol
                if sot is True:
                    kol = kol.replace("('", "")
                    kol = kol.replace("',)", "")
                    contenitore[i] = kol
                if sot2 is True:
                    kol = kol.replace('("', "")
                    kol = kol.replace('",)', "")
                    contenitore[i] = kol
                if sot3 is True:
                    kol = kol.replace("(' ", "")
                    contenitore[i] = kol
                if virgo1 is True:
                    kol = kol.replace("'", "\\'")
                    contenitore[i] = kol
                    virgcheck1 = 1
                if virgo2 is True and virgcheck1 != 1:
                    kol = kol.replace('"', '\\"')
                    contenitore[i] = kol
                    virgcheck1 = 1
                if virgo3 is True and virgcheck1 != 1:
                    kol = kol.replace('’', '\\’')
                    contenitore[i] = kol
                    virgcheck1 = 1
            kol = str(contenitore[i])
            virgcheck1 = 0
            virgcheck2 = 0
            sot = sottostr in kol
            sot2 = sottostr2 in kol
            sot3 = sottostr3 in kol
            virgo1 = virgoletta1 in kol
            virgo2 = virgoletta2 in kol
            virgo3 = virgoletta3 in kol
            if sot is True:
                kol = kol.replace("('", "")
                kol = kol.replace("',)", "")
                contenitore[i] = kol
            if sot2 is True:
                kol = kol.replace('("', "")
                kol = kol.replace('",)', "")
                contenitore[i] = kol
            if sot3 is True:
                kol = kol.replace("(' ", "")
                contenitore[i] = kol
            if virgo1 is True:
                kol = kol.replace("'", "\\'")
                contenitore[i] = kol
                virgcheck1 = 1
            if virgo2 is True and virgcheck1 != 1:
                kol = kol.replace('"', '\\"')
                contenitore[i] = kol
                virgcheck1 = 1
            if virgo3 is True and virgcheck1 != 1:
                kol = kol.replace('’', '\\’')
                contenitore[i] = kol
                virgcheck1 = 1
            i = i + 1
        i = 0
        print(" 2 .");
        while (i < 50):
            print(contenitore[i])
            i = i + 1
        i = 0
        print(" 3 .")
        while (i < 50):
            kol = str(caratteristiche[i])
            virgo1 = virgoletta1 in kol
            virgo2 = virgoletta2 in kol
            print(caratteristiche[i])
            if virgo1 is True:
                kol = kol.replace("'", "\\'")
                caratteristiche[i] = kol
            if virgo2 is True:
                kol = kol.replace('"', '\\"')
                caratteristiche[i] = kol
            i = i + 1
        domandine = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " "]
        i = 0
        domandine[0] = nome
        domandine[1] = cognome
        domandine[2] = username
        domandine[3] = eta
        domandine[4] = quando
        domandine[5] = dove
        domandine[6] = come
        domandine[7] = ore
        domandine[8] = commerciale
        domandine[9] = testo2

        while (i <= 10):
            kol = str(domandine[i])
            virgo1 = virgoletta1 in kol
            virgo2 = virgoletta2 in kol
            print(domandine[i])
            if virgo1 is True:
                kol = kol.replace("'", "\\'")
                domandine[i] = kol
            if virgo2 is True:
                kol = kol.replace('"', '\\"')
                domandine[i] = kol
            i = i + 1

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            charset="utf8",
            # password="vanni1998",
            # database="Music",
            port="3306",
            # auth_plugin="caching_sha2_password",
        )
        mycursor = mydb.cursor()
        database_name = "Music"
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};", )

        i = 0

        mycursor = mydb.cursor()
        conteni = str(contenitore[i])
        cara = str(caratteristiche[i])
        domand = str(domandine[i])
        ffi = str(domandine[i]) + str(domandine[i + 2])
        create_table = f"""
        CREATE TABLE IF NOT EXISTS {ffi} (
        dati VARCHAR(500),
        posizioni VARCHAR(500),
        dati_extra VARCHAR(500)
        );
        """
        inserire = f"""INSERT INTO {ffi} (dati, posizioni, dati_extra) VALUES ('{contenitore[i]}', '{caratteristiche[i]}', '{domandine[i]}');
        """
        print(create_table)
        # mycursor.execute("SHOW DATABASES;",)
        mycursor.execute("USE music", )
        # mycursor.execute("""SHOW TABLES""",)
        mycursor.execute(create_table, )
        i = 0
        j = 0
        k = 0
        u = 5
        while (i < 30):
            conteni = str(contenitore[i])
            cara = str(caratteristiche[j])
            domand = str(domandine[k])
            # contenitore[i]=unicodedata.normalize('NFC',contenitore[i])
            # kol=contenitore[i]
            # ggh=0
            # while(ggh==0):
            # if (contenitore[i].startswith('\\x')):
            # ggh=0
            # i=i+1
            # else:
            # ggh=8

            inserire = f"""INSERT INTO {ffi} (dati, posizioni, dati_extra) VALUES ('{contenitore[i]}', '{caratteristiche[j]}', '{domandine[k]}');
            """
            inserire_flash = f"""INSERT INTO {ffi} (dati_extra) VALUES ('{domandine[k]}');
            """
            # mycursor.execute("""SHOW TABLES""",)
            if (contenitore[i] != '1111' and caratteristiche[j] != '1111'):
                try:
                    mycursor.execute(inserire)
                    i = i + 1
                    j = j + 1
                    k = k + 1
                    u = 5
                except:
                    i = i + 1
                    j = j + 1
                    k = k + 1
                    u = 5
            else:
                if (contenitore[i] == '1111'):
                    i = i + 1
                if (caratteristiche[j] == '1111'):
                    j = j + 1
                # if(contenitore[i]=='1111' or (caratteristiche[j]=='1111') and domandine[k]!=" " and u==5):
                # mycursor.execute(inserire_flash)
                # else:
                # break
                # i=i+1
            mydb.commit()
        i = 0
        end = 0
        endd = 1
        follo = 0
        ppp = 0
        mycursor.execute("SHOW TABLES")
        tabelle = mycursor.fetchall()

        for table in tabelle:
            tabel = str(tabelle[ppp])
            tabel = tabel.replace("',)", "")
            tabel = tabel.replace("('", "")
            print(tabel)
            if (tabel == ffi.lower()):
                i = 31;
            while (i < 30):
                tabel = str(tabelle[ppp])
                tabel = tabel.replace("',)", "")
                tabel = tabel.replace("('", "")
                trovare = f"""SELECT dati FROM {tabel} WHERE dati_extra like %s ORDER BY RAND() LIMIT 1"""
                value = '%' + domandine[i] + '%'
                mycursor.execute(trovare, (value,))
                consiglio = mycursor.fetchall()
                if (consiglio and domandine[i] != " "):
                    trov = f"""SELECT dati FROM {tabel} ORDER BY RAND() LIMIT 1"""
                    mycursor.execute(trov)
                    consiglio = mycursor.fetchall()
                    while (follo != 9):
                        cons = str(consiglio)
                        print(cons)
                        cons = cons.replace("[('", "")
                        cons = cons.replace("',)]", "")
                        print(cons)
                        try:
                            fl = float(cons)
                            fuo = True
                        except ValueError:
                            fuo = False
                        print(fuo)
                        if (fuo == False and cons != " "):
                            follo = 9
                            print("falsee")
                        if (fuo == True or cons == " "):
                            trov = f"""SELECT dati FROM {tabel} ORDER BY RAND() LIMIT 1"""
                            # valu = '%' + domandine[i] + '%'
                            # tabel = str(tabelle[ppp])
                            # tabel = tabel.replace("',)", "")
                            # tabel = tabel.replace("('", "")
                            # trovare = f"""SELECT dati FROM {tabel} WHERE dati_extra like %s ORDER BY RAND() LIMIT 1"""
                            # value = '%' + domandine[i] + '%'
                            mycursor.execute(trov)
                            consiglio = mycursor.fetchall()
                            print("truee")
                    cons = cons.replace("[('", "")
                    cons = cons.replace("',)]", "")
                    print(cons)
                    end = 1
                    # endd=1
                    # ppp = ppp + 1
                    break

                i = i + 1
                if (domandine[i] == " "):
                    i = 31
                # ppp=ppp+1
                # end=1
            i = 0
            ppp = ppp + 1
            if (end == 1):
                break

        i = 0;
        yout = "https://www.youtube.com/results?search_query="
        while (i < 30):
            yout = "https://www.youtube.com/results?search_query="
            try:
                cose = float(contenitore[i])
            except:
                contin = str(contenitore[i])
                contin = contin.replace(" ", "+")
                contin = contin.replace("(", "")
                contin = contin.replace(")", "")
                contin = contin.replace("/", "")
                contin = contin.replace("|", "")
                contin = contin.replace("\\", "")
                yout = yout + contin + "+music"
                print(yout)
            links[i]=yout
            i = i + 1
        yout = "https://www.youtube.com/results?search_query="
        contin = contin.replace(" ", "+")
        contin = contin.replace("(", "")
        contin = contin.replace(")", "")
        contin = contin.replace("/", "")
        contin = contin.replace("|", "")
        contin = contin.replace("\\", "")
        contin = contin + contin + "+music"
        links[i]=yout
        print(yout)
        lop="22"
        # mycursor.execute(f"INSERT (%s,%s)", (domandine[i], contenitore[i]))

        # for x in mycursor:
        # print(x)

        mycursor.close()
        mydb.close()
        #app.stop()
        #global app
        #app=Application.builder().token(TOKEN).build()
        return("ricerca completata , premi un tasto per vederli")
        #context.application.stop()

    #requests.get('https://www.spaziogames.it/categorie/recensione')
    #response = requests.get('https://www.spaziogames.it/categorie/recensione')
    return 'non ho capito, digita /help per veredere i comandi'

print('Starting bot...')
#app = Application.builder()
#app = Application.builder().token(TOKEN).build()
#print(bbot())
#dispatcherr=app.dispatcher
print(varr)



    # app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('custom', custom_command))

try:
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
#while True:
    #if (varr == "7"):
        #break
   # app.add_error_handler(error)
    print('Polling...')
    while True:
        print(varr)
        polling()
except:
      print("uscito")
