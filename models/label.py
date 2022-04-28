class Label:
    
    def __init__(self, name, active = True, id = None):
        self.name = name
        self.active = active
        self.id = id
        
    def deactivate_label(self):
        self.active = False #this is a simple method to have here, to flip a active from true to false
    
    def rectivate_label(self):
        self.active = True #method to flip a active from false to true
        # test in run_tests.py