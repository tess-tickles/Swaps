import Ssort
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        inList = [5,4,3,2,1,0]
        outList = [5,4,2,3,1,0]
        assert Ssort.bob(inList,2)==outList #Test 1 fails

if __name__ == '__main__':
    unittest.main()
