import requests
import telebot as tlb
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from urllib3 import request


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



@bot.message_handler(commands=['dolar'])
def send_welcome(message):
    url_web = "https://eltoque.com/tasas-de-cambio-de-moneda-en-cuba-hoy#informal-diaria"
    url_foto = "https://wa.cambiocuba.money/trmi.png"
    url_foto_descargada = "https://github.com/Leyderhr/MultiConverterBot/blob/main/Imagen1.jpg"
    mensaje = f'<a href="{url_foto_descargada}"> Presiona aqui para ver el valor real</a>\nPapa el dolar esta carísimo'
    
    
    # Haciendo peticion al sitio web
    resp = requests.get(url_foto)
    resp.raise_for_status()

    with open('Imagen1.jpg', 'wb') as imagen:
        imagen.write(resp.content)
        
    bot.send_message(message.chat.id, mensaje, parse_mode= "html")

    
    
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
        bot.register_next_step_handler(message, convert_speed_keyboard(message))
              
    elif message.text == "Volumen":
        bot.register_next_step_handler(message, convert_volume_keyboard(message))
           
    elif message.text == "Longitud":
        bot.register_next_step_handler(message, convert_longitud_keyboard(message))
    
    elif message.text == "Peso y Masa": 
        bot.register_next_step_handler(message, convert_masa_keyboard(message))
    
    elif message.text == "Temperatura":
        bot.register_next_step_handler(message, convert_temperatura_keyboard(message))

    elif message.text == "Área":
        bot.register_next_step_handler(message, convert_area_keyboard(message))
    
    elif message.text == "Moneda":
        bot.register_next_step_handler(message, convert_moneda_keyboard(message))


# Manejadores de VELOCIDAD
# =============================================================================
def convert_speed_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Metros/s"),
        KeyboardButton("Kilometros/h"),
        KeyboardButton("Millas/h")) 
    
    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_speed)
    
    
    
 
# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_speed(message):
    
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text
        
    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_speed_value)



# Esta funcion guarda el valor de la magnitud
def save_speed_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_speed_keyboard2)

 
    
def convert_speed_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Metros/s"),
        KeyboardButton("Kilometros/h"),
        KeyboardButton("Millas/h")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 
    
    
# Fin de las funciones manejadoras de VELOCIDAD 
# ============================================================================= 
    



# Manejadores de VOLUMEN
# ============================================================================= 
def convert_volume_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Mililitros"),
        KeyboardButton("Centilitro"),
        KeyboardButton("Decilitro"),
        KeyboardButton("Litro"),
        KeyboardButton("Decalitro"),
        KeyboardButton("Hectolitro"),
        KeyboardButton("Kilolitro")) 
      
    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_volumen)



# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_volumen(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_volumen_value)




# Esta funcion guarda el valor de la magnitud
def save_volumen_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_volumen_keyboard2)    
 


def convert_volumen_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Mililitros"),
        KeyboardButton("Centilitro"),
        KeyboardButton("Decilitro"),
        KeyboardButton("Litro"),
        KeyboardButton("Decalitro"),
        KeyboardButton("Hectolitro"),
        KeyboardButton("Kilolitro")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# Fin de las funciones manejadoras de VOLUMEN
# =============================================================================
    


# Manejadores de LONGITUD
# =============================================================================
def convert_longitud_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("km"),
        KeyboardButton("m"),
        KeyboardButton("dm"),
        KeyboardButton("cm"),
        KeyboardButton("Millas"),
        KeyboardButton("mm")) 

    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_longitud)



# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_longitud(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_longitud_value)



# Esta funcion guarda el valor de la magnitud
def save_longitud_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_longitud_keyboard2)   



def convert_longitud_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("km"),
        KeyboardButton("m"),
        KeyboardButton("dm"),
        KeyboardButton("cm"),
        KeyboardButton("Millas"),
        KeyboardButton("mm")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# Fin de los Manejadores de Longitud
# =============================================================================



# Manejadores de PESO Y MASA
# =============================================================================
def convert_masa_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("toneladas"),
        KeyboardButton("kilogramos"),
        KeyboardButton("gramos"),
        KeyboardButton("miligramos")) 

    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_masa)

# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_masa(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_masa_value)



# Esta funcion guarda el valor de la magnitud
def save_masa_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_masa_keyboard2)   



def convert_masa_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("toneladas"),
        KeyboardButton("kilogramos"),
        KeyboardButton("gramos"),
        KeyboardButton("miligramos")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# FIN de los manejadores de PESO Y MASA
# =============================================================================



# Manejadores de TEMPERATURA
# =============================================================================
def convert_temperatura_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Grados Celsius"),
        KeyboardButton("Grados Fharenheit"),
        KeyboardButton("Grados Kelvin")) 

    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_temperatura_value)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_temperatura_value(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_value_temperatura)



# Esta funcion guarda el valor de la magnitud
def save_value_temperatura(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_temperatura_keyboard2)   



def convert_temperatura_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("toneladas"),
        KeyboardButton("kilogramos"),
        KeyboardButton("gramos"),
        KeyboardButton("miligramos")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# FIN de los manejadores de TEMPERATURA
# =============================================================================


# Manejadores de AREA
# =============================================================================
def convert_area_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("km²"),
        KeyboardButton("m²"),
        KeyboardButton("cm²")) 

    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_area_value)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_area_value(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_value_area)



# Esta funcion guarda el valor de la magnitud
def save_value_area(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_area_keyboard2)   



def convert_area_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("km²"),
        KeyboardButton("m²"),
        KeyboardButton("cm²")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# FIN de los manejadores de AREA
# =============================================================================




# Manejadores de MONEDA
# =============================================================================
def convert_moneda_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("CUP"),
        KeyboardButton("USD"),
        KeyboardButton("EUR"),
        KeyboardButton("MLC")) 

    bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_moneda_value)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_moneda_value(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = message.text

    bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_value_moneda)



# Esta funcion guarda el valor de la magnitud
def save_value_moneda(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    msg = bot.send_message(message.chat.id, "Escribe la otra magnitud a convertir")
    bot.register_next_step_handler(msg, convert_area_keyboard2)   



def convert_moneda_keyboard2(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("CUP"),
        KeyboardButton("USD"),
        KeyboardButton("EUR"),
        KeyboardButton("MLC")) 
    
    
    global magnitudFinal
    magnitudFinal = message.text 

# FIN de los manejadores de MONEDA
# =============================================================================




bot.infinity_polling()