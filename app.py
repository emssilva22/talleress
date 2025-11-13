from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML embebido (puedes usar un archivo .html si prefieres)
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Formulario simple</title>
    <style>
        body { font-family: Arial; margin: 50px; background-color: #f4f4f4; }
        form { background: white; padding: 20px; border-radius: 10px; width: 300px; }
        input, button { width: 100%; padding: 8px; margin-top: 10px; }
        h2 { color: #333; }
    </style>
</head>
<body>
    <h2>Formulario de Registro</h2>
    <form method="POST">
        <label>Nombre:</label>
        <input type="text" name="nombre" required>

        <label>Correo electrónico:</label>
        <input type="email" name="correo" required>

        <label>Edad:</label>
        <input type="number" name="edad" required>

        <button type="submit">Enviar</button>
    </form>

    {% if datos %}
        <h3>✅ Datos recibidos:</h3>
        <p><strong>Nombre:</strong> {{ datos.nombre }}</p>
        <p><strong>Correo:</strong> {{ datos.correo }}</p>
        <p><strong>Edad:</strong> {{ datos.edad }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def formulario():
    datos = None
    if request.method == "POST":
        datos = {
            "nombre": request.form["nombre"],
            "correo": request.form["correo"],
            "edad": request.form["edad"]
        }
    return render_template_string(HTML_FORM, datos=datos)

if __name__ == "__main__":
    # Escucha en todas las interfaces (0.0.0.0) y en el puerto 80
    app.run(host="0.0.0.0", port=80, debug=True)
