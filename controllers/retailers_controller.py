from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.retailer import Retailer
import repositories.retailer_repository as retailer_repository

retailers_blueprint = Blueprint("retailers", __name__)
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
# GET '/retailers'
@retailers_blueprint.route("/retailers")
def retailers():
    retailers = retailer_repository.select_all() #the way to access the DB is via the retailer_respository
    return render_template("retailers/new.html", all_retailers = retailers)
