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

# INDEX
# GET '/transactions'
# NEW (NEW and CREATE are combined, because we need to create but we alos need to post it back to the DB
# this is the first step. See CREATE for the second step)
# @retailers_blueprint.route("/retailers")
# def retailers():
#     retailers = retailer_repository.select_all_alphabetically() #the way to access the DB is via the retailer_respository
#     return render_template("retailers/index.html", all_retailers = retailers)