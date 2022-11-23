from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def webhome():
    """De homepagina van de website

    :return: HTML pagina met een overzicht van de website
    """
    # Returnen van HTML pagina
    return render_template("home.html")



@app.route('/art', methods=["GET"])
def webart():
    """De homepagina van de website

    :return: HTML pagina met een overzicht van de website
    """
    # Returnen van HTML pagina
    return render_template("articles.html")



@app.route('/res', methods=["GET"])
def webresult():
    """De homepagina van de website

    :return: HTML pagina met een overzicht van de website
    """
    # Returnen van HTML pagina
    return render_template("results.html")


if __name__ == '__main__':
    app.run()