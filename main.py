from tkinter import TRUE
from click import command, help_option
from pyparsing import Token
import telebot as tlb
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from zmq import Message


# You can set parse_mode by default. HTML or MARKDOWN
token =  "7289229933:AAGb2BqwtPj98ktIkbl6b3nKc3TyUeUSzaI"
bot = tlb.TeleBot(token, parse_mode=None) 


@bot.message_handler(commands=['start', 'help', 'description'])
def send_welcome(message):
    if message.text == '/start':
        bot.reply_to(message, "Que bola'\nAquí abajo tienes las opciones para convertir lo que quieras")
        convertir_Keyboard(message)
        
    elif message.text == '/help':
        bot.reply_to(message, "Aqui solo convertimos unidades.\nTambién tienes el comando /dolar para ver el precio del dolar actual")



# Metodo que configura el telado y mestra los tipos de uniades que se pueden convertir
# =============================================================
@bot.message_handler(content_types="text")
def convertir_Keyboard(message):
    # Se configura el teclado para que muetre las opciones a convertir
    board = ReplyKeyboardMarkup(row_width= 2, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Km/h a Millas/h"), KeyboardButton("mlls/h a km/h"),
        KeyboardButton("Velocidad"), KeyboardButton("Volumen"),
        KeyboardButton("Longitud"), KeyboardButton("Peso y Masa"),
        KeyboardButton("Temperatura"), KeyboardButton("Energía"),
        KeyboardButton("Área"), KeyboardButton("Moneda"))   
    
    bot.send_message(message.chat.id, "Elige qué quieres contar:", reply_markup=board)
    bot.register_next_step_handler(message, handle_converter)    
# ============================================================== 
 
    
def handle_converter(message):
    
     # Comprobar la elección del usuario y proceder con la función correspondiente
    if message.text == "Velocidad":
        bot.send_message(message.chat.id, "Escribe los kilometros a convertir")
        bot.register_next_step_handler(message, convert_kms)
        
    elif message.text == "Volumen":
        bot.send_message(message.chat.id, "Elige lo que quieres convertir")
        bot.registrer_next_Step_handler (message, convert_volume)
           
    elif message.text == "mlls/h a km/h":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar caracteres"
        )
        # bot.register_next_step_handler(message, count_characters) 
    

def convert_kms(message):
    kms = float(message.text)
    millas = kms / 1.609
    bot.send_message(message.chat.id, f"Son {round(millas, 4)} Millas/h") 

bot.infinity_polling()
