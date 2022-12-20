import sqlite3

class AppData():
    """def __init__(self):
        self.connection = sqlite3.connect('data_base.db')
    
    def insertarSuscripcion(self, cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo):
        cursor = self.connection.cursor()
        sql = '''INSERT INTO suscripcion (cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo)
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()"""


class AppData():
    def __init__(self):
        self.connection = sqlite3.connect('data_base.db')
    
    def insertarSuscripcion(self, cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo):
        cursor = self.connection.cursor()
        sql = '''INSERT INTO suscripcion (cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(sql, (cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo))
        self.connection.commit()
        cursor.close()