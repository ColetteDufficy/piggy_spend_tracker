from db.run_sql import run_sql

from models.label import Label #importing the class of Label to be used in CRUD


#SAVE
def save(label):
    sql = """
        INSERT INTO labels (name, active) 
        VALUES (%s, %s) 
        RETURNING *
    """
    #i dont insert a value ie '%s' for the id value here, because it hasnt been generated yet - because its a new item, and thereore doesnt have an id yet. Thats why its listed as None in the def init on label.py file
    values = [
        label.name, 
        label.active 
        ]
    results = run_sql(sql, values)
    id = results[0]['id'] #this is telling it where to find the 'id' number once its been generated in the 'dictionary'  - see run_sql file for defintion of the the dctionary
    label.id = id
    return label


#SELECT_ALL
def select_all():  
    labels = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL labels to it.

    sql = "SELECT * FROM labels"
    results = run_sql(sql)

    for row in results:
        label = Label(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id'])
        labels.append(label)
    return labels 



#SELECT_ALL_ALPHABETICALLY
def select_all_alphabetically():  
    labels = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL labels to it.

    sql = "SELECT * FROM labels ORDER BY name"
    results = run_sql(sql)

    for row in results:
        label = Label(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id'])
        labels.append(label)
    return labels 



#SELECT_ALL_ALPHABETICALLY_AND_ACTIVE
def select_all_alphabetically_and_active():  
    labels = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL labels to it.

    sql = "SELECT * FROM labels WHERE active=True ORDER BY name" #i only want ACTIVE=TRUE labels
    results = run_sql(sql)

    for row in results:
        label = Label(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id'])
        labels.append(label)
    return labels 



#SELECT_ALL_ALPHABETICALLY_AND_ACTIVE
def select_all_alphabetically_and_inactive():  
    labels = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL labels to it.

    sql = "SELECT * FROM labels WHERE active=False ORDER BY name" #i only want ACTIVE=FALSE labels
    results = run_sql(sql)

    for row in results:
        label = Label(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id'])
        labels.append(label)
    return labels 


#SELECT_BY_ID
def select(id):
    label = None
    sql = """
        SELECT * FROM labels 
        WHERE id = %s
    """ 
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        label = Label(
            result['name'], 
            result['active'], 
            result['id'] )
    return label



#DELETE_ALL
def delete_all():
    sql = "DELETE FROM labels" 
    run_sql(sql)
    
    
    
#DELETE_BY_ID
def delete(id):
    sql = """
        DELETE FROM labels 
        WHERE id = %s
    """ 
    values = [id]
    run_sql(sql, values)
    

#UPDATE 
def update(label):
    sql = """
        UPDATE labels 
        SET (name, active) = (%s, %s) 
        WHERE id = %s
    """
    values = [
        label.name, 
        label.active, 
        label.id
        ]
    run_sql(sql, values) 