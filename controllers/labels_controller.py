from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.label import Label
import repositories.label_repository as label_repository

labels_blueprint = Blueprint("labels", __name__)
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
# GET '/labels'
# NEW (NEW and CREATE are combined, because we need to create but we alos need to post it back to the DB
# this is the first step. See CREATE for the second step)
@labels_blueprint.route("/labels")
def labels():
    labels = label_repository.select_all_alphabetically() #the way to access the DB is via the retailer_respository
    labels_active = label_repository.select_all_alphabetically_and_active() #the way to access the DB is via the retailer_respository
    labels_inactive = label_repository.select_all_alphabetically_and_inactive() #the way to access the DB is via the retailer_respository
    return render_template("labels/index.html", all_labels = labels, labels_active=labels_active, labels_inactive=labels_inactive)


# CREATE
# POST '/labels'
# post the form to fill the database
@labels_blueprint.route("/labels", methods=['POST'])
def create_label():
  name = request.form['name']
  
  new_label = Label(name)          
  label_repository.save(new_label)
  return redirect("/labels")


# EDIT (EDIT and UPDATE are combined)
# Step 1:
# GET '/labels/<id>/edit'
@labels_blueprint.route("/labels/<id>/edit", methods=["GET"])
def edit_label(id):
    label = label_repository.select(id) #singular label, becasue we only want to identify ONE label to edit, by its id number
    return render_template("labels/edit.html", label = label)


# UPDATE
# PUT '/labels/<id>'
@labels_blueprint.route("/labels/<id>", methods=['POST'])
def update_label(id):
    name = request.form['name']
    active = request.form['active']
    
    label = Label(name, active, id) 
    label_repository.update(label)
    return redirect('/labels')


# DELETE
# DELETE '/labels/<id>'
@labels_blueprint.route("/labels/<id>/delete", methods=['POST'])
def delete_label(id):
    label_repository.delete(id)
    return redirect('/labels')
