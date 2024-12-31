from flask import Flask, render_template

# DEFINE ROOT PATH
app = Flask(__name__, static_folder="./static", template_folder="./")


# ROTA RAIZ - CARREGA A PÁGINA INICIAL
@app.route('/')
def main():
    return render_template('index.html') # RENDER HOME PAGE


if __name__ == '__main__':
    print("Inicializando...")
    app.run(host="192.168.0.194", port='5080', debug=True) #TESTE