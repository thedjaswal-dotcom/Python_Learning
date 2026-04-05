from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["lives"] = 10
        session["message"] = "Start guessing!"

    if request.method == "POST":
        guess = int(request.form["guess"])
        number = session["number"]

        if guess > number:
            session["message"] = "Too High!"
        elif guess < number:
            session["message"] = "Too Low!"
        else:
            session["message"] = "🎉 You Won!"
            return render_template("index.html", game_over=True, **session)

        session["lives"] -= 1

        if session["lives"] <= 0:
            session["message"] = f"💀 You lost! Number was {number}"
            return render_template("index.html", game_over=True, **session)

    return render_template("index.html", game_over=False, **session)


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)