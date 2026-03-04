from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret"

DATABASE = "records.db"


# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- CREATE TABLE ----------------
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            record_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------- DASHBOARD ----------------
@app.route("/")
def dashboard():
    conn = get_db_connection()
    records = conn.execute("SELECT * FROM records").fetchall()
    conn.close()
    return render_template("dashboard.html", records=records)


# ---------------- ADD ----------------
@app.route("/add", methods=["POST"])
def add_record():
    try:
        record_id = int(request.form["record_id"])
        name = request.form["name"]
        age = int(request.form["age"])
    except:
        flash("Invalid input format")
        return redirect(url_for("dashboard"))

    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO records (record_id, name, age) VALUES (?, ?, ?)",
            (record_id, name, age),
        )
        conn.commit()
        conn.close()
        flash("Record added successfully")
    except sqlite3.IntegrityError:
        flash("Record ID already exists")

    return redirect(url_for("dashboard"))


# ---------------- UPDATE ----------------
@app.route("/update", methods=["POST"])
def update_record():
    try:
        record_id = int(request.form["record_id"])
        name = request.form["name"]
        age = int(request.form["age"])
    except:
        flash("Invalid input format")
        return redirect(url_for("dashboard"))

    conn = get_db_connection()
    cursor = conn.execute(
        "UPDATE records SET name = ?, age = ? WHERE record_id = ?",
        (name, age, record_id),
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        flash("Record not found")
    else:
        flash("Record updated successfully")

    return redirect(url_for("dashboard"))


# ---------------- DELETE ----------------
@app.route("/delete/<int:record_id>")
def delete_record(record_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM records WHERE record_id = ?", (record_id,))
    conn.commit()
    conn.close()

    flash("Record deleted successfully")
    return redirect(url_for("dashboard"))


# ---------------- SEARCH ----------------
@app.route("/search", methods=["POST"])
def search_record():
    try:
        record_id = int(request.form["search_id"])
    except:
        flash("Invalid search input")
        return redirect(url_for("dashboard"))

    conn = get_db_connection()
    records = conn.execute(
        "SELECT * FROM records WHERE record_id = ?", (record_id,)
    ).fetchall()
    conn.close()

    if records:
        return render_template("dashboard.html", records=records)
    else:
        flash("Record not found")
        return redirect(url_for("dashboard"))


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    