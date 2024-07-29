# MultiConverterBot
Este Bot fue creado por 3 alumnos de Ingeniería Informática 🐳de la Cujae (Cuba)  como proyecto de la optativa Python.

Te puede ayudar a convertir todo tipo de unidades, ya sean de volumen, distancia, presión e incluso monetarias, y sí, también te dice a cuánto ElToque tiene dólar hoy😉

Para programar el bot se utilizó la librería [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot.git) como base principal para crear todos los 
manejadores de mensajes y los teclados que aparecen en el bot. Lamentablemene aún no esta subido a un servicio de cloud por lo que sólo funciona si te descargas el código
y lo corres manualmente desde tu pc, **ten pasciencia con la conexión de Etecsa**.

Técnicas como el web scraping se utilizaron mediante la librería **requests** de python para lograr descargar la foto del la Tasa de Cambio en el Mercado Informal en Cuba
y poderla enviar al chat mediante el comando /dolar.
Se hizo uso de la librería **pint**, que contiene funciones especializadas en el trabajo con magnitudes fisicas, estas se emplearon para realizar las conversiones solicitadas
por el usuario mediante el UnitRegistry. Tambien se empleó la librería **googletrans**, especializada en traducciones, para cambiar el idioma de los resultados al lenguaje
nativo de los usuarios.


Creadores: [**Leyder**](https://github.com/Leyderhr), [**Dennis**](https://github.com/DnsSera) y **Orlando** (La Mafia)
