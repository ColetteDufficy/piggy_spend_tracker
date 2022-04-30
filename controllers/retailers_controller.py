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
# NEW (NEW and CREATE are combined, because we need to create but we alos need to post it back to the DB
# this is the first step. See CREATE for the second step)
@retailers_blueprint.route("/retailers")
def retailers():
    retailers = retailer_repository.select_all_alphabetically() #the way to access the DB is via the retailer_respository
    retailers_active = retailer_repository.select_all_alphabetically_and_active() #the way to access the DB is via the retailer_respository
    retailers_inactive = retailer_repository.select_all_alphabetically_and_inactive() #the way to access the DB is via the retailer_respository
    return render_template("retailers/index.html", all_retailers = retailers, retailers_active = retailers_active, retailers_inactive=retailers_inactive)


# CREATE
# POST '/retailers'
# post the form to fill the database
@retailers_blueprint.route("/retailers", methods=['POST'])
def create_retailer():
  name = request.form['name']
  
  new_retailer = Retailer(name)          
  retailer_repository.save(new_retailer)
  return redirect("/retailers")




# EDIT (EDIT and UPDATE are combined)
# Step 1:
# GET '/retailers/<id>/edit'
@retailers_blueprint.route("/retailers/<id>/edit", methods=["GET"])
def edit_retailer(id):
    retailer = retailer_repository.select(id) #singular retailer, becasue we only want to identify ONE retailer to edit, by its id number
    return render_template("retailers/edit.html", retailer = retailer)



# UPDATE
# PUT '/retailers/<id>'
@retailers_blueprint.route("/retailers/<id>", methods=['POST'])
def update_retailer(id):
    name = request.form['name']
    active = request.form['active']
    
    retailer = Retailer(name, active, id) 
    retailer_repository.update(retailer)
    return redirect('/retailers')


# DELETE
# DELETE '/retailers/<id>'
@retailers_blueprint.route("/retailers/<id>/delete", methods=['POST'])
def delete_retailer(id):
    retailer_repository.delete(id)
    return redirect('/retailers')
