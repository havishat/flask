from flask import Flask, render_template, url_for  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def dissapperininja():
    return render_template('index.html')    # Render the template and return it! 

@app.route('/ninja')
def ninja():
    color = url_for('static', filename= 'Ninjas/tmnt.png')
    return render_template('ninja.html', color= color)

@app.route("/ninja/<color>")
def findcolor(color):
    # newcolor = color
    # print newcolor
    if color == "blue":
        # filename = 'Ninjas/donatello.jpg'
        color = url_for('static', filename= 'Ninjas/leonardo.jpg')
        # return render_template('ninja.html', color= filename) 
    elif color == "orange":
        color = url_for('static', filename= 'Ninjas/michelangelo.jpg')
    elif color == "red":
        color = url_for('static', filename= 'Ninjas/raphael.jpg')
    elif color == "purple":
        color = url_for('static', filename= 'Ninjas/donatello.jpg')
    #     filename = 'Ninjas/donatello.jpg'
    #     # return render_template('ninja.html', color= filename) 
    else:
        color = url_for('static', filename= 'Ninjas/notapril.jpg')
    return render_template('ninja.html', color= color) 

app.run(debug=True)                       # Run the app in debug mode.
