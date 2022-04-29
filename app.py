from flask import Flask, render_template

# from controllers.transactions_controller import transactions_blueprint
from controllers.retailers_controller import retailers_blueprint
from controllers.labels_controller import labels_blueprint

app = Flask(__name__)

# app.register_blueprint(transactions_blueprint)
app.register_blueprint(retailers_blueprint)
app.register_blueprint(labels_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)