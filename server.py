from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

#things i learned today: 
# The render_template and the "templates" folder
# move the static files to the "static" folder. the src attrs will start with "static/"
#Flask likes to cache the static files.
#Even chrome will not refresh. To hardreload: "Shift + (click on refresh)"