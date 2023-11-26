import unittest

from Holdjaro import holdjaro


class holdjaroteszt(unittest.TestCase):

  def test_forward_north(self):

    rover = holdjaro(0, 0, 'N')

    result = rover.lepes('f')

    self.assertEqual(result, (0, 1, 'N'))







if __name__ == '__main__':

  unittest.main()