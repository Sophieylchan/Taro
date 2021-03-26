from flask import Flask, Response,url_for

app = Flask(__name__)


@app.route('/get/text')
def get_text():
    return Response("Boo!", mimetype='text/plain')


@app.route("/")
def aboutme():
    url =url_for("get_text")
    return """
   <html>
   <head>
    <title> About Page </title>
   </head>


   <body>
    <h1> About me </h1>
    <p> Hello!</p>
    <p> My name is Sophie!</p>
    <hr>
    <a href="https://imgur.com/R9KauAo.png">Click here for a pretty picture</a>
    <hr>
    <a href="{}">Click for something else</a>
   </body>

   </html>
   """.format(url)


if __name__ == '__main__':
    app.run(debug=True)