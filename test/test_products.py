import os , logging
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from service.products import ProductService
from service.models import db, ProductModel
from service.routes import app

logging.disable(logging.CRITICAL)
BASE_URL = "/products"
CONTENT_TYPE_JSON = "application/json"
######################################################################
#  <your resource name>   P R O D U C T S   T E S T   C A S E S
######################################################################
class TestProducts(unittest.TestCase):
    """ Test Cases for Product Class """

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.logger.setLevel(logging.CRITICAL)
        ProductModel.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        db.session.close()

    def setUp(self):
        """Runs before each test"""
        self.app = app.test_client()
        db.drop_all()  # clean up the last tests
        db.create_all()  # create new tables

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_index_page_success(self):
        self.assertNotEqual(ProductService.index_page(), None)
    
    def test_get_all_products_success(self):
        self.assertNotEqual(ProductService.get_all_products(), "")  
    
    def test_create_product_success(self):
        ProductService.create_product("Demo", 35, "Demo Description")

    def test_create_product_failure(self):
        pass

if __name__ == '__main__':
    unittest.main()