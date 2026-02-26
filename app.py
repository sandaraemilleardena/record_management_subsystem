from flask import Flask, render_template, request, redirect, url_for, flash
from app.record_manager import RecordManager

app = Flask(__name__)
app.secret_key = "secret"
manager = RecordManager()

@app.route("/")
def dashboard():
    records = manager.get_all_records()
    return render_template("dashboard.html", records=records)

@app.route("/add", methods=["POST"])
def add_record():
    try:
        record_id = int(request.form["record_id"])
        name = request.form["name"]
        age = int(request.form["age"])
    except:
        flash("Invalid input format")
        return redirect(url_for("dashboard"))

    success, message = manager.add_record(record_id, name, age)
    flash(message)
    return redirect(url_for("dashboard"))

@app.route("/update", methods=["POST"])
def update_record():
    try:
        record_id = int(request.form["record_id"])
        name = request.form["name"]
        age = int(request.form["age"])
    except:
        flash("Invalid input format")
        return redirect(url_for("dashboard"))

    success, message = manager.update_record(record_id, name, age)
    flash(message)
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:record_id>")
def delete_record(record_id):
    manager.delete_record(record_id)
    flash("Record Deleted")
    return redirect(url_for("dashboard"))

@app.route("/search", methods=["POST"])
def search_record():
    try:
        record_id = int(request.form["search_id"])
    except:
        flash("Invalid search input")
        return redirect(url_for("dashboard"))

    record = manager.search_record(record_id)
    if record:
        return render_template("dashboard.html", records=[record])
    else:
        flash("Record Not Found")
        return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)