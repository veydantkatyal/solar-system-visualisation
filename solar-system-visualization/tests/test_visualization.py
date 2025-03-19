import unittest
from src.visualization import create_sphere, create_orbit

class TestVisualization(unittest.TestCase):
    def test_create_sphere(self):
        sphere = create_sphere(5, 100, 'blue')
        self.assertIsNotNone(sphere)

    def test_create_orbit(self):
        orbit = create_orbit(100)
        self.assertIsNotNone(orbit)

if __name__ == '__main__':
    unittest.main()
