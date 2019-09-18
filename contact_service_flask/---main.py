from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')
    
# @app.route('/')
# def hello_world():
#    return 'Hello World!'

# run the application
if __name__ == "__main__":
    app.run(debug=True)