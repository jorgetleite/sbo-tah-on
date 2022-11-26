''' ESTE SCRIPT FOI RODADO NO PHPMYADMIN PARA CRIAR O BANCO DE DADOS
AQUI ELE NÃO TEM FUNCIONALIDADE'''


CREATE TABLE IF NOT EXISTS produtos(
    fornecedor CHAR(50) NOT NULL,
    produto CHAR(50) NOT NULL,
    endereco CHAR(100) NULL,
    whatsapp CHAR (50) NOT NULL,
    email CHAR(50) NULL
);

'''

CREATE TABLE IF NOT EXISTS categories(
    id tinyint NOT NULL,
    name CHAR(40) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY('id')
);

ALTER TABLE produtos ADD FOREIGN KEY ('id_category')REFERENCES categories('id');

'''