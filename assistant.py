from pint import UnitRegistry
from googletrans import Translator

def transformacion_Magnitud(magnitud_inicial, magnitud_final, valor: float) :
    ureg = UnitRegistry()

    if (magnitud_final["elevada"] == 1) and (magnitud_inicial["elevada"] == 1) :
        magnt_i = ureg.Quantity(valor, magnitud_inicial["magnitud"])
        magnt_f = magnt_i.to(magnitud_final["magnitud"])
    else :
        magnt_i = valor * ureg(magnitud_inicial["magnitud"]) ** magnitud_inicial["elevada"]
        magnt_f = magnt_i.to(ureg(magnitud_final["magnitud"]) ** magnitud_final["elevada"])

    return magnt_i, magnt_f

def translate_string(magnI, magnF) :
    translator = Translator()
    string = f"{magnI.magnitude} {magnI.units} are equivalent to {round(magnF.magnitude, 3)} {magnF.units}"
    string = string.replace('_', ' ')

    return translator.translate(string, src = 'en', dest = 'es').text