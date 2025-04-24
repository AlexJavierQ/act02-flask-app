# Importa Flask(framework web) y request (para poder hacer peticones HTTP) 
from flask import Flask
import requests

# Crea una aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    # URL del archivo de texto que contiene los datos
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    
    # Hace una petición HTTP a esa URL y guarda el contenido línea por línea separado por saltos de línea
    # El método text.text devuelve el contenido de la respuesta como una cadena de texto
    datos = requests.get(url).text.strip().split("\n")

    # Encabezado y encabezado en el HTML de la tabla
    html = "<h2>Personas con ID iniciando en 3, 4, 5, 7</h2><table border='1'>"
    html += "<tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Pais</th><th>Direccion</th></tr>"

    # Recorre cada línea del archivo
    for linea in datos:
        # Separa los campos usando el carácter "|"
        partes = linea.split("|")
        
        # Verifica (con el metodo "startswith" que devuelve true si el texto inicia con el prefijo dado)
        # si el ID empieza con 3, 4, 5 o 7
        if partes[0].startswith(("3", "4", "5", "7")):
        # Crea una fila HTML con cada dato envuelto en <td> (celda de tabla)
        # "".join(...) une todas esas celdas en una sola cadena
        # El método f-string permite insertar variables dentro de cadenas de texto
            fila = "".join(f"<td>{campo}</td>" for campo in partes)
            # Agrega la fila a la tabla HTML usando nuevamente el método f-string
            html += f"<tr>{fila}</tr>"

    # Cierra la tabla
    html += "</table>"
    # Devuelve el HTML generado al navegador
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
