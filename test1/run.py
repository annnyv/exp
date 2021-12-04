import os
import unittest

# report_path = os.path.join(os.getcwd(), 'report')

def case_l():
    case_path = os.path.join(os.getcwd(), 'case')
    case = unittest.defaultTestLoader.discover(case_path)
    return case

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(case_l())