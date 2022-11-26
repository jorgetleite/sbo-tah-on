from flask.views import MethodView 
from flask import request, render_template, redirect, flash
from src.db import mysql



class IndexController(MethodView):
    def get(self):
        return render_template('public/index.html')



class SobreController(MethodView):
    def get(self):
        return render_template('public/sobre.html')



class CadastrarController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos")
            data = cur.fetchall()

        return render_template('public/cadastrar.html', data=data)

#CATEGORIES

'''
            cur.execute("SELECT * FROM categories")
            categories = cur.fetchall()
            return render_template('public/cadastrar.html', data=data, categories=categories)
'''

class ConsultarController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos")
            data = cur.fetchall()

        return render_template('public/consultar.html', data=data)



    def post(self):
        fornecedor = request.form['fornecedor']
        produto = request.form['produto']
        endereco = request.form['endereco']
        whatsapp = request.form['whatsapp']
        email = request.form['email'] 

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO produtos VALUES (%s, %s, %s, %s, %s)", (fornecedor, produto, endereco, whatsapp, email))
                cur.connection.commit()
                flash('PRODUTO CADASTRADO COM SUCESSO', 'success')
            except:
                flash('ESTE PRODUTO NAO FOI CADASTRADO', 'error')
            
            return redirect('/cadastrar')


#CLASSES ABAIXO DESATIVADAS

'''
class DeleteProdutoController(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            try:
                cur.execute("DELETE FROM produtos WHERE code =%s", (id))
                cur.connection.commit()
                flash('PRODUTO DELETADO COM SUCESSO', 'success')
            except: 
                flash('ESTE PRODUTO NAO FOI DELETADO', 'error')
            return redirect('/')

class UpdateProdutoController(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos WHERE code =%s", (id))
            product = cur.fetchone()
            return render_template('public/update.html', product=product)
    
    def post(self, id):
        productCode = request.form['id']
        fornecedor = request.form['fornecedor']
        endereco = request.form['endereco']
        whatsapp = request.form['whatsapp']
        email = request.form['email']

        with mysql.cursor() as cur:
            try:
                cur.execute("UPDATE produtos SET fornecedor =%s, endereco =%s, whatsapp =%s, email =%s WHERE id = %s", (fornecedor, endereco, whatsapp, email))
                cur.connection.commit()
                flash('PRODUTO EDITADO COM SUCESSO', 'success')
            except:
                flash('ESTE PRODUTO NAO FOI EDITADO', 'error')
            return redirect('/')


'''


#CATEGORIAS            

'''
class CategoriesController(MethodView):
    def get(self):
        return render_template("public/categories.html")

        
    def post(self):
        id = request.form['id']
        name = request.form['name']
        description = request.form['description']
        

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO categories VALUES (%s, %s, %s)", (id,name,description))
            cur.connection.commit()
            return "sucesso!"
       
'''

        


    
