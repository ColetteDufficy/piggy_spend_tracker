import unittest
from models.retailer import Retailer
from models.label import Label
from models.transaction import Transaction

class TestTask(unittest.TestCase):
    
    def setUp(self):
        self.retailer = Retailer("Tesco", True)
        self.label = Label("Groceries", True)
        self.transaction = Transaction("Tesco", "Groceries", 60)
    
    
    def test_retailer_has_name(self):
        self.assertEqual("Tesco", self.retailer.name)
         
    def test_label_has_name(self):
        self.assertEqual("Groceries", self.label.name)
           
    def test_transaction_has_value(self):
        self.assertEqual(60, self.transaction.value)
    
    def test_transaction_has_a_label(self):
        self.assertEqual("Groceries", self.transaction.label)
    
    
    def test_retailer_starts_active(self):
        self.assertEqual(True, self.retailer.active)
        
    def test_retailer_is_deactivated(self):
        self.retailer.deactivate_retailer()
        self.assertEqual(False, self.retailer.active)
    
    def test_retailer_is_reactivated(self):
        self.retailer.rectivate_retailer()
        self.assertEqual(True, self.retailer.active)
    
    def test_label_starts_active(self):
        self.assertEqual(True, self.label.active)
    
    def test_label_is_deactivated(self):
        self.label.deactivate_label()
        self.assertEqual(False, self.label.active)
    
    def test_label_is_reactivated(self):
        self.label.rectivate_label()
        self.assertEqual(True, self.label.active)
   