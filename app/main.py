from app import create_app

app = create_app()


@app.route("/")
def home():
    return {"message": "Hello World!"}


if __name__ == "main":
    app.run(debug=True)
