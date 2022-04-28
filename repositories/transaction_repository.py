from db.run_sql import run_sql

from models.transaction import Transaction #importing the class of Retailer to be used in CRUD
import repositories.retailer_repository as retailer_repository #import everthing under the name 'retailer_repository'
import repositories.label_repository as label_repository #import everthing under the name 'retailer_repository'


#SAVE
def save(transaction):
    sql = """
        INSERT INTO transactions (retailer_id, label_id, value) 
        VALUES (%s, %s, %s) 
        RETURNING *
    """
    #i dont insert a value ie '%s' for the id value here, because it hasnt been generated yet - because its a new item, and thereore doesnt have an id yet. Thats why its listed as None in the def init on reatiler.py file
    
    values = [
        transaction.retailer.id, 
        transaction.label.id, 
        transaction.value
        ]
    results = run_sql(sql, values)
    id = results[0]['id'] #this is telling it where to find the 'id' number once its been generated in the 'dictionary'  - see run_sql file for defintion of the the dctionary
    transaction.id = id
    return transaction


#SELECT_ALL
def select_all():  
    transactions = [] 

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        retailer = retailer_repository.select(row['retailer_id'])#this extra line is needed because were trying to extract the 'id' key, from the Retailer table, via the transactions table.
        label = label_repository.select(row['label_id'])#this extra line is needed because were trying to extract the 'id' key, from the Label table, via the transactions table0
        transaction = Transaction(
            retailer,
            label,
             row['value'],
             row['id']
            )
        transactions.append(transaction)
    return transactions 




#DELETE_ALL
def delete_all():
    sql = "DELETE FROM transactions" 
    run_sql(sql)
    
    
    
#DELETE_BY_ID
def delete(id):
    sql = """
        DELETE FROM transactions 
        WHERE id = %s
    """ 
    values = [id]
    run_sql(sql, values)
    

#UPDATE 
def update(transaction):
    sql = """
        UPDATE transactions 
        SET (retailer_id, label_id, value) = (%s, %s, %s) 
        WHERE id = %s
    """
    values = [
        transaction.retailer.id, 
        transaction.label.id, 
        transaction.value, 
        transaction.id
        ]
    run_sql(sql, values) 
    