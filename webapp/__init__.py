from flask import Flask
from webapp import datastorage
from webapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)
conn = datastorage.init()

# SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config.from_object(Config)
from webapp import routes


# Для отладки в Шарме, потом удалить
# if __name__ == '__main__':
#     app.run()
