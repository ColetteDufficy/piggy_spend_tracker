class Retailer:
    
    def __init__(self, name, active = True, id = None ):
        self.name = name
        self.active = active
        self.id = id
        
    def deactivate_retailer(self):
        self.active = False #keep this method here, to flip a acvtie retailer from true to false
        #test in run_test.py
        
    def rectivate_retailer(self):
        self.active = True #method to flip a active from false to true
        # test in run_tests.py