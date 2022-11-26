from src.controllers.controller import *
from src.controllers.errors import * 

routes = {

    "index_route":"/","index_controller":IndexController.as_view("index"),

    "cadastrar_route":"/cadastrar","cadastrarcontroller":CadastrarController.as_view("cadastrar"),
    
    "consultar_route":"/consultar","consultar_controller":ConsultarController.as_view("consultar"),  

    "sobre_route":"/sobre","sobre_controller":SobreController.as_view("sobre"),

    #"delete_route":"/delete/product/<int:code>", "delete_controller": DeleteProdutoController.as_view("delete"),
   
    #"update_route":"/update/product/<int:code>", "update_controller": UpdateProdutoController.as_view("update"),
   
    #"categories_route":"/create/categorie", "categories_controller": CategoriesController.as_view("categories"),

    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),

}

    

