from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

poll_data = {
    "question": "",
    "options": [],
    "votes": []
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        poll_data["question"] = request.form["question"]
        option_count = int(request.form["option_count"])
        poll_data["votes"] = [0] * option_count
        return redirect(url_for("options", count=option_count))
    return render_template("home.html")

@app.route("/options/<int:count>", methods=["GET", "POST"])
def options(count):
    if request.method == "POST":
        poll_data["options"] = [request.form[f"option{i}"] for i in range(count)]
        return redirect(url_for("poll"))
    return render_template("options.html", count=count)

@app.route("/poll", methods=["GET", "POST"])
def poll():
    if request.method == "POST":
        vote = int(request.form["vote"])
        poll_data["votes"][vote] += 1
        return redirect(url_for("result"))
    return render_template("poll.html", poll_data=poll_data)

@app.route("/result")
def result():
    return render_template("result.html", poll_data=poll_data)

if __name__ == "__main__":
    app.run(debug=True)
