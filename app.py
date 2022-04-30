from flask import Flask, render_template

from controllers.transactions_controller import transactions_blueprint
from controllers.retailers_controller import retailers_blueprint
from controllers.labels_controller import labels_blueprint

import repositories.transaction_repository as transaction_repository


app = Flask(__name__)

app.register_blueprint(transactions_blueprint)
app.register_blueprint(retailers_blueprint)
app.register_blueprint(labels_blueprint)


# i need to include the 'total' counter method here, because i cant extract it out of the transaction blueprint 'container'
@app.route('/')
def home():
    transactions = transaction_repository.select_all() 
    
    total = 0
    for transaction in transactions:
        total += transaction.value
    
    return render_template("index.html", all_transactions=transactions, total=total)



@app.route('/log_off')
def log_off():
    return render_template("log_off.html")

if __name__ == '__main__':
    app.run(debug=True)