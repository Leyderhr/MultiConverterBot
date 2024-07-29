import requests
import telebot as tlb
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import assistant


# You can set parse_mode by default. HTML or MARKDOWN
token =  "7289229933:AAGb2BqwtPj98ktIkbl6b3nKc3TyUeUSzaI"
bot = tlb.TeleBot(token, parse_mode=None) 

# Declaracion de las variables para almacenar los valores

tipos_magnitud = {"kilometros/h" : 'kph', "metros/s" : 'mps', "millas/h" : 'mph', "mililitros" : 'ml',
                  "centilitro" : 'cl', "decilitro" : 'dl', "litro" : 'l', "decalitro" : 'dal',
                  "hectolitro" : 'hl', "kilolitro" : 'kl', "kilometros" : 'km', "metros" : 'm',
                  "decimetros" : 'dm', "centimetros" : 'cm', "milimetros" : 'mm', "millas" : 'miles',
                  "toneladas" : 't', "kilogramos" : 'kg', "gramos" : 'g', "miligramos" : 'mg',
                  "libras" : 'lb', "grados Celsius" : '°C', "grados Fharenheit" : '°F', "grados Kelvin" : 'kelvin',
                  "km²" : 'km', "m²" : 'm', "cm²" : 'cm'}
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
def send_photo(message):
    url_web = "https://eltoque.com/tasas-de-cambio-de-moneda-en-cuba-hoy#informal-diaria"
    url_foto = "https://wa.cambiocuba.money/trmi.png"
    url_foto_descargada = "https://github.com/Leyderhr/MultiConverterBot/blob/main/Imagen1.jpg"
    mensaje = f'<a href="{url_foto_descargada}"> Presiona aqui para ver el valor real</a>\nPapa el dolar esta carísimo'
    
    
    # Haciendo peticion al sitio web
    resp = requests.get(url_foto)
    resp.raise_for_status()

    with open('Imagen1.jpg', 'wb') as imagen:
        imagen.write(resp.content)
    
    # Enviando foto
    img = open("Imagen1.jpg", "rb") 
    bot.send_photo(message.chat.id, img)   
 
    
# Metodo que configura el telado y mestra los tipos de uniades que se pueden convertir
# =============================================================
def convertir_Keyboard(message):
    
    # Se configura el teclado para que muetre las opciones a convertir
    board = ReplyKeyboardMarkup(row_width= 2, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("Velocidad"), KeyboardButton("Volumen"),
        KeyboardButton("Longitud"), KeyboardButton("Peso y Masa"),
        KeyboardButton("Temperatura"), KeyboardButton("Área"))   
    
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
    
# Manejadores de VELOCIDAD
# =============================================================================
def convert_speed_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("metros/s"),
        KeyboardButton("kilometros/h"),
        KeyboardButton("millas/h")) 
    
    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_speed)
    

# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_speed(message):
    
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 1}
        
    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_speed_value)


# Esta funcion guarda el valor de la magnitud
def save_speed_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)

    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("metros/s"),
        KeyboardButton("kilometros/h"),
        KeyboardButton("millas/h")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler(message, show_result)
   
    
# Fin de las funciones manejadoras de VELOCIDAD 
# ============================================================================= 
    

# Manejadores de VOLUMEN
# ============================================================================= 
def convert_volume_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("mililitros"),
        KeyboardButton("centilitro"),
        KeyboardButton("decilitro"),
        KeyboardButton("litro"),
        KeyboardButton("decalitro"),
        KeyboardButton("hectolitro"),
        KeyboardButton("kilolitro")) 
      
    message = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_volumen)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_volumen(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 1}

    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_volumen_value)


# Esta funcion guarda el valor de la magnitud
def save_volumen_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("mililitros"),
        KeyboardButton("centilitro"),
        KeyboardButton("decilitro"),
        KeyboardButton("litro"),
        KeyboardButton("decalitro"),
        KeyboardButton("hectolitro"),
        KeyboardButton("kilolitro")) 
     
    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler(message, show_result)    
 

# Fin de las funciones manejadoras de VOLUMEN
# =============================================================================


# Manejadores de LONGITUD
# =============================================================================
def convert_longitud_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("kilometros"),
        KeyboardButton("metros"),
        KeyboardButton("decimetros"),
        KeyboardButton("centimetros"),
        KeyboardButton("millas"),
        KeyboardButton("milimetros")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_longitud)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_longitud(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 1}

    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_longitud_value)


# Esta funcion guarda el valor de la magnitud
def save_longitud_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("kilometros"),
        KeyboardButton("metros"),
        KeyboardButton("decimetros"),
        KeyboardButton("centimetros"),
        KeyboardButton("millas"),
        KeyboardButton("milimetros")) 
    
    message = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board) 
    bot.register_next_step_handler(message, show_result)   


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
        KeyboardButton("miligramos"),
        KeyboardButton("libras")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_value_masa)

# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_value_masa(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 1}

    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_masa_value)


# Esta funcion guarda el valor de la magnitud
def save_masa_value(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)

    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("toneladas"),
        KeyboardButton("kilogramos"),
        KeyboardButton("gramos"),
        KeyboardButton("miligramos"),
        KeyboardButton("libras")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler(message, show_result)   


# FIN de los manejadores de PESO Y MASA
# =============================================================================


# Manejadores de TEMPERATURA
# =============================================================================
def convert_temperatura_keyboard(message):
    
    # Se configura el teclado para que muetre las opciones de Volumen a convertir
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("grados Celsius"),
        KeyboardButton("grados Fharenheit"),
        KeyboardButton("grados Kelvin")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_temperatura_value)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_temperatura_value(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 1}

    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_value_temperatura)



# Esta funcion guarda el valor de la magnitud
def save_value_temperatura(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)
    
    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("grados Celsius"),
        KeyboardButton("grados Fharenheit"),
        KeyboardButton("grados Kelvin")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud a la que quieres convertir:", reply_markup=board)    
    bot.register_next_step_handler(message, show_result)   


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

    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler (message, save_area_value)


# Esta funcion guarda el tipo de magnitud que tenemos y queremos convertir   
def save_area_value(message):
   
    # VARIABLE magnitudInicial, almacena el tipo de magnitud de VELOCIDAD
    global magnitudInicial
    magnitudInicial = {"magnitud" : tipos_magnitud[message.text], "elevada" : 2}

    message = bot.send_message(message.chat.id, "Escribe el valor a convertir")
    bot.register_next_step_handler(message, save_value_area)


# Esta funcion guarda el valor de la magnitud
def save_value_area(message):
    
    # VARIABLE valor, almacena el valor cuantitativo de la magnitud
    global valor
    valor = float(message.text)  

    board = ReplyKeyboardMarkup(row_width= 1, resize_keyboard=True, one_time_keyboard=True)
    board.add(
        KeyboardButton("km²"),
        KeyboardButton("m²"),
        KeyboardButton("cm²")) 

    message = bot.send_message(message.chat.id, "Elige la magnitud que quieres convertir:", reply_markup=board)
    bot.register_next_step_handler(message, show_result)   


# FIN de los manejadores de AREA
# =============================================================================


# Funciones auxiliares
# =============================================================================
def show_result(message) :
    global magnitudFinal, magnitudInicial, valor
    magnitudFinal = {"magnitud" : tipos_magnitud[message.text], "elevada" : magnitudInicial["elevada"]}
    result1, result2 = assistant.transformacion_Magnitud(magnitudInicial, magnitudFinal, valor)
    bot.send_message(message.chat.id, assistant.translate_string(result1, result2))
    reset_global_var()
    
def reset_global_var() :
    global magnitudInicial, magnitudFinal, valor
    magnitudInicial = magnitudFinal = valor = None
    
bot.infinity_polling()