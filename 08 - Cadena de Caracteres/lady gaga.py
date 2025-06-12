from datetime import datetime
tema = "Bradley Cooper | Lukas Nelson - Shallow"
vistas = "1900 millones"
duracion = "3:37"
link = "https://www.youtube.com/watch?v=bo_efYhYU2A"
fecha_de_lanzamiento = "2018-09-27"

def obtener_colaboradores(titulo: str) -> list:
    tema = titulo.split("-")
    colaboradores = tema[0].split("|")
    for i in range (len(colaboradores)):
        colaboradores[i] = colaboradores[i].strip()
    return colaboradores

def obtener_nombre_tema(titulo: str) -> str:
    tema = titulo.split("|")
    titulo = tema[0].strip()
    return titulo

def convertir_vistas_numerico(vistas: str) -> int:
    vistas = vistas.split(" ")
    vista_num = int(vistas[0]) * 1000000
    return vista_num

def convertir_duracion_numerico(duracion: str) -> int:
    duracion = duracion.split(":")
    for i in range(len(duracion)):
        duracion[i] = int(duracion[i])
    total_segundos = (duracion[0]) *60 + duracion[1]
    return total_segundos

def obtener_codigo(url: str) -> str:
    url = url.split("?v=")
    codigo = url[1]
    return codigo

fecha_de_lanzamiento = "2018-09-27"
def formatear_fecha(fecha: str) -> datetime.date:
    formato_fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
    return formato_fecha


x = formatear_fecha(fecha_de_lanzamiento)
print(type(x))

