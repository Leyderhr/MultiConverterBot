
from tkinter import TRUE
from click import command, help_option
from pyparsing import Token
import telebot as tlb
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from zmq import Message


# You can set parse_mode by default. HTML or MARKDOWN
token =  "7289229933:AAGb2BqwtPj98ktIkbl6b3nKc3TyUeUSzaI"
bot = tlb.TeleBot(token, parse_mode=None) 

# Declaracion de las variables para almacenar los valores
magnitudInicial = None
magnitudFinal = None
valor = None


@bot.message_handler(commands=['start', 'help', 'description'])
def send_welcome(message):
    
    if message.text == '/start':
        bot.reply_to(message, "Que bola'\nAquí abajo tienes las opciones para convertir lo que quieras")
        convertir_Keyboard(message)
        
    elif message.text == '/help':
        bot.reply_to(message, "Aqui solo convertimos unidades.\nTambién tienes el comando /dolar para ver el precio del dolar actual")



# Metodo que configura el telado y mestra los tipos de uniades que se pueden convertir
# =============================================================
def convertir_Keyboard(message):
    
    # Se configura el teclado para que muetre las opciones a convertir
    board = ReplyKeyboardMarkup(row_width= 2, resize_keyboard=True, one_time_keyboard=True)
    board.add(
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
        bot.register_next_step_handler(message, convert_Speed_Keyboard(message))
        
    elif message.text == "Volumen":
        #  bot.send_message(message.chat.id, "Elige lo que quieres convertir")
        bot.register_next_step_handler(message, convert_Volume_Keyboard)
           
    
    elif message.text == "mlls/h a km/h":
        bot.send_message(
            message.chat.id, "Envía el texto del que deseas contar caracteres"
        )
        # bot.register_next_step_handler(message, count_characters) 
    

# Manejadores de VELOCIDAD
# =============================================================================
def convert_Speed_Keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Metros/s"),
        KeyboardButton("Kilometros/h"),
        KeyboardButton("Millas/h")) 
    
    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_speed)
    
    
    
 
# Esta funcion guarda el tipo de agnitud que tenemos y queremos convertir   
def save_speed(message):
    
    # VARIABLE ks, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial 
    magnitudInicial = message.text
    
    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_speed_value)

 
    
def convert_Speed_Keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Metros/s"),
        KeyboardButton("Kilometros/h"),
        KeyboardButton("Millas/h")) 
    
    # msg = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board)
    global magnitudFinal
    magnitudFinal = message.text 
    

      



# Esta funcion guarda el valor de la magnitud
def save_speed_value(message):
    # VARIABLE kms, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_Speed_Keyboard2)
 
 
    

    
# ============================================================================= 
    
    
def convert_Volume_Keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Mililitros"),
        KeyboardButton("Centilitro"),
        KeyboardButton("Decilitro"),
        KeyboardButton("Litro"),
        KeyboardButton("Decalitro"),
        KeyboardButton("Hectolitro"),
        KeyboardButton("Kilolitro"),) 
      
    cont = 0
    if cont == 0:    
        msg = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
        bot.register_next_step_handler (msg, convert_Volumen)
        cont+= 1
        cont1 = cont
    
    
    elif cont1 == 1:
        msg = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres llevar el resultado:", reply_markup=board)
        bot.register_next_step_handler(msg, convert_Volumen)


    
 
def convert_Volumen(message):
    
    pos = 0
    # La variable volumen va a guardar el tipo de variable que se va a convertir
    if pos == 0:
        vol = message.text
        bot.send_message(message.chat.id, f"vol = {vol}")
        pos +=1
    else:
        vol1 = message.text
        bot.send_message(message.chat.id, f"vol1 = {vol1}")
    
           
    





bot.infinity_polling()
