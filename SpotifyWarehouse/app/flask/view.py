from flask import Flask
#from pathlib import Path #never do this path, it does not work
#put the graphs in static directory

class View:
    def __init__(self):
        self.app = Flask(__name__, static_folder="../static", static_url_path="/static")
        self.app.add_url_rule("/", view_func=self.start)
        self.site_code = "<h1>Spotify Datawarehouse Project</h1>"
        self.image_id = 1

    def start(self):
        return self.site_code
    
    def add_picture(self, path, desc: str):
        self.site_code += "<img id=\"picture" + str(self.image_id) +"\" src=" + str(path) + " height=500 ></br>"
        self.site_code += "<label for=\"picture" + str(self.image_id) +"\" >" + desc + "</label></br>"
        self.image_id += 1


test = View()

if __name__ == "__main__":
    test.add_picture(path="/static/output/earlybird.png", desc="Early bird")
    test.add_picture(path="/static/output/night_owl.png", desc="Night Owl")
    test.app.run(debug="true")
    
