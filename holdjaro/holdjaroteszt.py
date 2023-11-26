import unittest

from Holdjaro import holdjaro


class holdjaroteszt(unittest.TestCase):

  def test_forward_north(self):
    rover = holdjaro(0, 0, 'N', [])
    result = rover.lepes('f')
    self.assertEqual(result, (0, 1, 'N'))

  def test_forward_south(self):
    rover = holdjaro(0, 0, 'S', [])
    result = rover.lepes('f')
    self.assertEqual(result, (0, -1, 'S'))

  def test_forward_east(self):
    rover = holdjaro(0, 0, 'E', [])
    result = rover.lepes('f')
    self.assertEqual(result, (1, 0, 'E'))

  def test_forward_west(self):
    rover = holdjaro(0, 0, 'W', [])
    result = rover.lepes('f')
    self.assertEqual(result, (-1, 0, 'W'))

  def test_backward(self):
    rover = holdjaro(0, 0, 'E', [])
    result = rover.lepes('b')
    self.assertEqual(result, (1, 0, 'E'))

  def test_left(self):
    rover = holdjaro(0, 0, 'N', [])
    result = rover.lepes('l')
    self.assertEqual(result, (0, 0, 'W'))

  def test_right(self):
    rover = holdjaro(0, 0, 'E', [])
    result = rover.lepes('r')
    self.assertEqual(result, (0, 0, 'S'))

  def test_obstacle(self):
    rover = holdjaro(0, 0, 'N', [(0, 1)])
    result = rover.lepes('f')
    self.assertEqual(result, "Vigyázz akadály")


if __name__ == '__main__':

  unittest.main()