from flask import Flask
from threading import Thread

app = Flask('Yashot3001')

@app.route('/')
def home():
    return "I'm Ready!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
