import unittest


def unique(str) -> bool:
    character_set = {}
    for char in str:
        if char in character_set:
            return False
        character_set[char] = 1
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('efgh'), ('ijk'), ('')]
    dataF = [('aba'), ('abcda'), ('dsadda dasadsad ')]

    def test_unique(self):
        # check is True
        for test_case in self.dataT:
            result = unique(test_case)
            self.assertTrue(result)
        # check is False
        for test_case in self.dataF:
            result = unique(test_case)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
