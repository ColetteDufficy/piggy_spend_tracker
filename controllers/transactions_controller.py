from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import Transaction

import repositories.retailer_repository as retailer_repository
import repositories.label_repository as label_repository
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)
#blueprint is a place to store lots of routes. ie @app.routes


# RESTful CRUD Routes - 7 of them:
# 1. INDEX
# 2. NEW
# 3. CREATE
# 4. SHOW
# 5. EDIT
# 6. UPDATE
# 7. DELETE

# # INDEX
# # GET '/transactions'
# # NEW (NEW and CREATE are combined, because we need to create but we alos need to post it back to the DB
# # this is the first step. See CREATE for the second step)
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all() 
    
    total = 0
    for transaction in transactions:
        total += transaction.value
    
    retailers = retailer_repository.select_all_alphabetically()
    retailers_active = retailer_repository.select_all_alphabetically_and_active()
    labels = label_repository.select_all_alphabetically()
    labels_active = label_repository.select_all_alphabetically_and_active()
    return render_template("transactions/index.html", all_transactions=transactions, all_retailers=retailers, retailers_active=retailers_active, all_labels=labels, labels_active=labels_active, total=total)


# # NEW
# # GET '/transactions/new'
# # # NEW (NEW and CREATE are combined, because we need to create but we alos need to post it back to the DB
# # # this is the first step. See CREATE for the second step)
# @transactions_blueprint.route("/transactions/new")
# def transactions():
#     transactions = transaction_repository.select_all() 
    
#     total = 0
#     for transaction in transactions:
#         total += transaction.value
    
#     retailers = retailer_repository.select_all_alphabetically()
#     labels = label_repository.select_all_alphabetically()
#     return render_template("transactions/index.html", all_transactions=transactions, all_retailers=retailers, all_labels=labels, total=total)


# # CREATE
# # POST '/transactions'
# # post the form to fill the database
@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    retailer_id = request.form['retailer_id']
    label_id = request.form['label_id']
    value = request.form['value']
        
    retailer = retailer_repository.select(retailer_id)
    label = label_repository.select(label_id)
    transaction = Transaction(retailer, label, value)
    transaction_repository.save(transaction)
    return redirect("/transactions")



# *********DONT NEED EDIT AND UPDATE AT TIS POINT******* 
# EDIT (EDIT and UPDATE are combined)
# GET '/transactions/<id>/edit'
# Step 1:
@transactions_blueprint.route("/transactions/<id>/edit", methods=["GET"])
def edit_transaction(id):
    transaction = transaction_repository.select(id) #singular transaction, becasue we only want to identify ONE transaction, by its id number
    retailers = retailer_repository.select_all() #retailers is plural cos we want ALL retailers
    labels = label_repository.select_all() 
    return render_template("transactions/edit.html", transaction = transaction, all_retailers = retailers, all_labels = labels)



# UPDATE
# PUT '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    retailer_id = request.form['retailer_id']
    label_id = request.form['label_id']
    value = request.form['value']
    
    retailer = retailer_repository.select(retailer_id) 
    label = label_repository.select(label_id) 
    transaction = Transaction(retailer, label, value, id) 
    transaction_repository.update(transaction)
    return redirect('/transactions')



# DELETE
# DELETE '/transactions/<id>/delete'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
