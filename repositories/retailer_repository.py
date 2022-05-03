from db.run_sql import run_sql

from models.retailer import Retailer #importing the class of Retailer to be used in CRUD




#SAVE
def save(retailer):
    sql = """
        INSERT INTO retailers (name, active) 
        VALUES (%s, %s) 
        RETURNING *
    """
    #i dont insert a value ie '%s' for the id value here, because it hasnt been generated yet - because its a new item, and thereore doesnt have an id yet. Thats why its listed as None in the def init on reatiler.py file
    
    values = [
        retailer.name, 
        retailer.active 
        ]
    results = run_sql(sql, values)
    id = results[0]['id'] #this is telling it where to find the 'id' number once its been generated in the 'dictionary'  - see run_sql file for defintion of the the dctionary
    retailer.id = id
    return retailer




#SELECT_ALL
def select_all():  
    retailers = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL users to it.

    sql = "SELECT * FROM retailers"
    results = run_sql(sql)

    for row in results:
        retailer = Retailer(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id']
            )
        retailers.append(retailer)
    return retailers 



 
 
 
#SELECT_ALL_ALPHABETICALLY
def select_all_alphabetically():  
    retailers = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL users to it.

    sql = "SELECT * FROM retailers ORDER BY name"
    results = run_sql(sql)

    for row in results:
        retailer = Retailer(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id']
            )
        retailers.append(retailer)
    return retailers 



#SELECT_ALL_ALPHABETICALLY_AND_ACTIVE
def select_all_alphabetically_and_active():  
    retailers = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL reatilers to it.

    sql = "SELECT * FROM retailers WHERE active=True ORDER BY name" #i only want ACTIVE=TRUE retailers
    results = run_sql(sql)

    for row in results:
        retailer = Retailer(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id']
            )
        retailers.append(retailer)
    return retailers 



#SELECT_ALL_ALPHABETICALLY_AND_INACTIVE
def select_all_alphabetically_and_inactive():  
    retailers = [] #the user cant see or acces the DB directly, so we first need to generate a new list to add ALL reatilers to it.

    sql = "SELECT * FROM retailers WHERE active=False ORDER BY name" #i only want ACTIVE=FALSE retailers
    results = run_sql(sql)

    for row in results:
        retailer = Retailer(
            row['name'], #these are taken from the sql table headers, as opposed to the class constructor names
            row['active'], 
            row['id']
            )
        retailers.append(retailer)
    return retailers 
    

#SELECT_BY_ID
def select(id):
    retailer = None
    sql = """
        SELECT * FROM retailers 
        WHERE id = %s
    """ 
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
# alterntaive line of code:
    # if row is not None:
        retailer = Retailer(
            result['name'], 
            result['active'], 
            result['id'] 
            )
    return retailer



#DELETE_ALL
def delete_all():
    sql = "DELETE FROM retailers" 
    run_sql(sql)
    
    
    
#DELETE_BY_ID
def delete(id):
    sql = """
        DELETE FROM retailers 
        WHERE id = %s
    """ 
    values = [id]
    run_sql(sql, values)
    
    
    
#UPDATE 
def update(retailer):
    sql = """
        UPDATE retailers 
        SET (name, active) = (%s, %s) 
        WHERE id = %s
    """
    values = [
        retailer.name, 
        retailer.active, 
        retailer.id
        ]
    run_sql(sql, values) 