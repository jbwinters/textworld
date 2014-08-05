from textworld.world_builder import Point, Feature, World
import unittest


class TestPoint(unittest.TestCase):
	def test_displacement(self):
		p1 = Point([0, 0])
		p2 = Point([0, 1])
		self.assertEqual([0, 1], p2.displacement(p1))
	def test_sub(self):
		p1 = Point([0, 0])
		p2 = Point([0, 1])
		self.assertEqual(1, p2 - p1)

		p3 = Point([0,0,0])
		p4 = Point([5, 5, 5])

		self.assertEqual(8.660254037844387, p4 - p3)

class TestWorld(unittest.TestCase):
	def test_world_instantiation(self):
		self.assertTrue(True)

	def test_add_line(self):
		pass
