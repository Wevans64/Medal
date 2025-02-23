from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    print("IP:", request.remote_addr)
    return redirect("https://medal.tv/games/garrys-mod/clips/jJT6mWGLcso7ZrJje?invite=cr-MSxqQzMsMzIxNDQyNjUwLA")

if __name__ == "__main__":
    app.run()
