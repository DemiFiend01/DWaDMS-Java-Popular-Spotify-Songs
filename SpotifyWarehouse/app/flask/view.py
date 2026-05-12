from flask import Flask, render_template
from os import listdir
from os.path import isfile, join

class View:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule("/", view_func=self.start)
        self.pictures=[]

    def start(self):
        return render_template('index.html', pictures=self.pictures)
  
    def load_pictures(self, path: str):
        fs_path = "app/flask" + path
        self.pictures = [
            {"src" : path + "/" + p }
            for p in listdir(fs_path) if isfile(join(fs_path,p)) and p.endswith(".png")
        ]

test = View()

if __name__ == "__main__":
    test.load_pictures(path="/static/output")
    test.app.run(debug="true")
    
