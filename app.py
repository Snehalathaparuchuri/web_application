from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Capture form data
        fullname = request.form["fullname"]
        username = request.form["username"]
        email = request.form["email"]
        phone_number = request.form["phone-number"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        gender = request.form["gender"]

        # Basic validation
        if password != confirm_password:
            return "Passwords do not match!", 400
        
        # Here you can add code to save the data in a database (e.g., SQLite, MySQL, etc.)
        # For now, we will just display a success message.
        
        return f"Registration Successful for {fullname} ({username})"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
