#http://170.75.167.178:30101/blogs
#blogs.py
#export FLASK_APP=blogs.py

from flask import Flask
import logging

app = Flask(__name__)

#Créez des données de test pour notre catalogue sous la forme d'une liste de dictionnaires
logging.basicConfig(filename='log/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/blogs')
def blog():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return f"Welcome to the Blog"

# Si aucun ID n'est fourni, affiche une erreur dans le navigateur
if __name__ == '__main__':

    app.run(host='localhost', debug=True)

