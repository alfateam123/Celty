import unittest
from celty import conf
from celty import communicator as comm
import time
from pyaria2 import PyAria2
from string import ascii_letters as letters

CONFIGURATION = "tests/celty.conf"
ARIA_HOST = 'localhost'
ARIA_PORT = 6800
ARIA2C_PATH = '/home/alfateam/aria2-1.18.8-win-32bit-build1/aria2c.exe'

class TestAriaCommunicatorCreation(unittest.TestCase):
    def test_createCommunicator(self):
        self.aria_rpc = comm.AriaCommunicator(port=9999, useRPCSecret=True, fixedSecret="ABCDEF")
        #this is just to check AriaCommunicator object works
        self.aria_rpc.ariaObj.shutdown() 

class TestAriaSecretGeneration(unittest.TestCase):
    def test_generateSecret(self):
        secret = comm.AriaCommunicator.generateSecret()
        self.assertEqual(len(secret), 15)
        self.assertEqual(filter(lambda chr_: chr_ not in letters, secret), str())