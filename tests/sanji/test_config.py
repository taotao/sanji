import unittest
import sys
import os

try:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../sanji')
    from model_initiator import ModelInitiator
except ImportError:
    print "Please check the python PATH for import test module."
    exit(1)

import os
import shutil

class TestModelInitiatorClass(unittest.TestCase):
    """
    " Test class
    """

    model_name = "test_myself"
    model_path = "/tmp/sanji-sdk/tests/test_myself"
    model_db_folder = "/tmp/sanji-sdk/tests/test_myself/data"
    model_factory_db = \
        "/tmp/sanji-sdk/tests/test_myself/data/test_myself.factory.json"
    model_db = "/tmp/sanji-sdk/tests/test_myself/data/test_myself.json"

    def setUp(self):
        """
        " Prepare
        """
        os.makedirs(self.model_path)
        self.model_initaitor = ModelInitiator(self.model_name, self.model_path)


    def tearDown(self):
        """
        " Clean up
        """
        if os.path.exists(self.model_path):
            shutil.rmtree(self.model_path)

        self.model_initaitor = None


    def test_init(self):
        """
        " Test __init__()
        """
        self.assertEquals(self.model_initaitor.model_name, self.model_name)


    def test_mkdir(self):
        """
        " It Should generate a data folder.
        """
        result = self.model_initaitor.mkdir()
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.model_db_folder))


    def test_create_db(self):
        """
        " It should generate a factory db.
        """
        self.model_initaitor.mkdir()
        try:
            with open(self.model_factory_db, 'a'):
                os.utime(self.model_factory_db, None)
        except Exception:
            self.fail("Maybe there is no folder to create file.")

        self.assertRaises(self.model_initaitor.create_db)

        result = self.model_initaitor.create_db()
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.model_db))


if __name__ == "__main__":
    unittest.main()