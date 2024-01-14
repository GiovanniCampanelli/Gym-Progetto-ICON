# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import urllib3
import requests
from bs4 import BeautifulSoup
import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

URL = "https://musicbrainz.org"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

TOKEN: Final = '6106626051:AAGPCWgk2YnJleGRcgjdCqjpUbmGuMPsVyw'
BOT_USERNAME: Final = '@PlatinumGameBot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ciao sono BeatBot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Mostra la playlist delle canzoni che preferisci')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Questo è il custom comand')

def handle_response(text: str) ->str:
    processed: str = text.lower()
    if 'ciao' in processed:
        return 'salve!'

    if 'come stai' in processed:
        return 'bene , grazie'
    results = soup.find(id=processed)
    job_elements = results.find_all(processed, class_="recensione")
    print(job_elements)
    return results.text
    return job_elements.text
    return 'non ho capito'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

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

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__=='__main__':

    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)





