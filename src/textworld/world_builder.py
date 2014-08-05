import abc
import math
import curses


class Point(object):

	def __init__(self, dimensions):
		self.dimensions = dimensions

	def __sub__(self, other, dims=None):
		dist = 0
		dist += sum(abs(x) for x in self.displacement(other, dims=dims))

		return math.sqrt(dist)

	def displacement(self, other, dims=None):
		if not dims:
			dims = set(range(len(self.dimensions)))
		return [(D[0] - D[1])**2 for i, D in
				enumerate(zip(self.dimensions, other.dimensions))
				if i in dims]

class Feature(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self, location):
		'''Location is a Point'''
		self.location = location

	def distance(self, p):
		return p - self.location

	@abc.abstractmethod
	def alter_perception(self, world):
		'''All locations in the map have N dimensions.
		The dimensions at various points are provided to the agent
		Features can alter their own or other points perception
		by changing those points values in the map'''
		raise NotImplementedError



class DistanceFeature(Feature):
	
	def alter_perception(self, world):
		world.set_percep(self.location, self.location - world.perspective)



class World(object):

	def __init__(self, p):
		self.perspective = p
		self.features = {}

	def set_percep(self, p, value):
		self.features[p] = value

	def from_file(self, f):
		'''Takes file f, creates feature map.
			f should be formatted as a newline delimited list of vectors
			with space-separated dimensions
		'''
		pass
		

	def add_line(self, cls, p1, p2):
		pass	

	def update(p):
		'''Update the map distance values from Point p's perspective'''
		pass
