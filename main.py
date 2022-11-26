from src.app import app



HOST = 'sql10.freemysqlhosting.net'
PORT = 3306
DEBUG = True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)
