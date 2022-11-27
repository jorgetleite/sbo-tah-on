from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'development'
)

if __name__ == "--main__":
    port = int(os.environ.get("PORT", 5000))   #verificar se era isso que impedia de rodar
    app.run(host='0.0.0.0', port=port)



app.add_url_rule(routes["cadastrar_route"], view_func=routes["cadastrarcontroller"])

app.add_url_rule(routes["consultar_route"], view_func=routes["consultar_controller"])

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])

app.add_url_rule(routes["sobre_route"], view_func=routes["sobre_controller"])

#app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

#app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

#app.add_url_rule(routes["categories_route"], view_func=routes["categories_controller"])

#  NO CODIGO ABAIXO FOI UTILIZADO register_error_handler PQ TRATA DE ERRO DE BD

app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])

