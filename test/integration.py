import unittest
import pyaz


class Integration(unittest.TestCase):

    def test_az_version_positive(self):
        """happy path test for pyaz.version"""
        result = pyaz.version()
        self.assertIsInstance(result, dict)
        
        # test that the result has a key named azure-cli
        version = result["azure-cli"]
        self.assertIsNotNone(version)


    def test_az_version_negative(self):
        """test that calling pyaz.version with an argument raises an error"""
        with self.assertRaises(TypeError):
            result = pyaz.version("test")
    
    
    def test_az_account_list_positive(self):
        """happy path test for az account list"""
        result = pyaz.account.list()
        self.assertIsInstance(result, list)
        
        # test that the first item in the result has a key named homeTenantId
        tenant_id = result[0]["homeTenantId"]
        self.assertIsNotNone(tenant_id)
        
        