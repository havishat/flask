from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
         # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
@app.route('/')                                          # the following "hello_world" function.
def myname():
  return render_template('index.html')    # Render the template and return it!
@app.route('/users', methods=['POST'])  
 
def create_user():
    name = request.form['Your name']
    print name
    #return redirect('/')
    return render_template('process.html',Name=name)
#def process():
  #return render_template('process.html')  
app.run(debug=True) # Run the app in debug mode.
                      