# from models.transaction import Transaction
# from models.retailer import Retailer
# from models.label import Label

# import repositories.transaction_repository as transaction_repository
# import repositories.retailer_repository as retailer_repository
# import repositories.label_repository as label_repository


# transaction_repository.delete_all() # the order of deletion is important here - since task repo uses data from the user repo, we need to delete the tasks first
# retailer_repository.delete_all()
# label_repository.delete_all()

# #SAVE
# retailer1 = Retailer("Tesco", True)
# retailer_repository.save(retailer1)
# print(f"{retailer1.name} is the name of retailer 1")

# #SAVE
# label1 = Label("Groceries", True)
# label_repository.save(label1)
# print(f"{label1.name} is the name of label 1")


# # # SAVE
# transaction1 = Transaction(retailer1, label1, 40)
# transaction_repository.save(transaction1) #this is taking the 'save ' function from user_repo and NOT task_repo
# print(f"I spent £{transaction1.value} on {transaction1.label.name} at {transaction1.retailer.name}")

# #SELECT ALL
# retailers = retailer_repository.select_all()
# labels = label_repository.select_all()
# transactions = transaction_repository.select_all()

# breakpoint()

