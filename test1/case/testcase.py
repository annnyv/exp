import unittest
import paramunittest
import pytest
import yaml
# import data.yaml
from apis.apis import appo

def readYaml():
    with open('data.yaml', 'rb') as f:
        # return list(yaml.safe_load_all(f))
        data = yaml.safe_load(f)
        return data


# class TestAppo:
#
#     @pytest.mark.parametrize('data', readYaml())
#     def test_ap(self, data):
#         print(data,type(data))
#         r = appo.ap(self, data['a'], data['b'])
#         assert r == data['expect']


# data = [{'a':1, "b":2, "expect":3}]
# @paramunittest.parametrized(data)
class Testappo(unittest.TestCase):

    # def setParameters(self, a, b, expect):
    #     self.a = a
    #     self.b = b
    #     self.expect = expect


    # def setup(self):
        # self.l = readYaml()
        # print(self.l)
        # a = 1
        # b = 2
        # self.expect = 3

    def test_ap(self):
        r = appo.ap(self, 1, 2)
        assert r == 3


if __name__=='__main__':
    # pytest.main()
    # a = TestAppo()
    # a.test_ap()
    unittest.main()