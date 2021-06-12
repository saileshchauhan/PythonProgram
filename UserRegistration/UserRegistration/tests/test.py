import pytest
from lib.hello import *

class Test_Code:

    def test_calculate(self):
        multiple=calculate(2,3)
        assert multiple==6

# if __name__=="__main__":
#     main()
