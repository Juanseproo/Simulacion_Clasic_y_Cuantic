import Simulaciones as c
import unittest
import math
class TestCplxOperatins(unittest.TestCase):

    def test_canicas(self):
        canicas = c.canicas([6, 2, 1, 5, 3, 10],[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]], 2)
        self.assertAlmostEqual(canicas, "[0, 0, 9, 5, 12, 1]")
        canicas = c.canicas([6, 2, 1, 5, 3, 10],[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]], 3)
        self.assertAlmostEqual(canicas, "[0, 0, 1, 5, 9, 12]") 
    
    def test_rendijas_clasic_y_cuantica(self):
        rendijas_clasic_y_cuantica = c.rendijas_clasic_y_cuantica([1, 0, 0, 0, 0, 0, 0, 0],[[0, 0, 0, 0, 0, 0, 0, 0], 
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [0, 1/math.sqrt(6), 0, 1, 0, 0, 0, 0],
                       [0, 1/math.sqrt(6), 0, 0, 1, 0, 0, 0],
                       [0, 1/math.sqrt(6), 1/math.sqrt(6), 0, 0, 1, 0, 0],
                       [0, 0, 1/math.sqrt(6), 0, 0, 0, 1, 0],
                       [0, 0, 1/math.sqrt(6), 0, 0, 0, 0, 1]], 1)
        self.assertAlmostEqual(rendijas_clasic_y_cuantica, "[0, 0.7071067811865475, 0.7071067811865475, 0.0, 0.0, 0.0, 0.0, 0.0]")
        rendijas_clasic_y_cuantica = c.rendijas_clasic_y_cuantica([1, 0, 0, 0, 0, 0, 0, 0],[[0, 0, 0, 0, 0, 0, 0, 0], 
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [0, 1/math.sqrt(6), 0, 1, 0, 0, 0, 0],
                       [0, 1/math.sqrt(6), 0, 0, 1, 0, 0, 0],
                       [0, 1/math.sqrt(6), 1/math.sqrt(6), 0, 0, 1, 0, 0],
                       [0, 0, 1/math.sqrt(6), 0, 0, 0, 1, 0],
                       [0, 0, 1/math.sqrt(6), 0, 0, 0, 0, 1]], 3)
        self.assertAlmostEqual(rendijas_clasic_y_cuantica, "[0.0, 0.0, 0.0, 0.2886751345948129, 0.2886751345948129, 0.5773502691896258, 0.2886751345948129, 0.2886751345948129]") 
        rendijas_clasic_y_cuantica = c.rendijas_clasic_y_cuantica([1, 0, 0, 0, 0, 0, 0, 0],[[0, 0, 0, 0, 0, 0, 0, 0], 
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [0, -1+1j/math.sqrt(6), 0, 1, 0, 0, 0, 0],
                       [0, -1-1j/math.sqrt(6), 0, 0, 1, 0, 0, 0],
                       [0, 1-1j/math.sqrt(6), -1+1j/math.sqrt(6), 0, 0, 1, 0, 0],
                       [0, 0, -1-1j/math.sqrt(6), 0, 0, 0, 1, 0],
                       [0, 0, 1-1j/math.sqrt(6), 0, 0, 0, 0, 1]], 1)
        self.assertAlmostEqual(rendijas_clasic_y_cuantica, "[0, 0.7071067811865475, 0.7071067811865475, 0j, 0j, 0j, 0j, 0j]") 
        rendijas_clasic_y_cuantica = c.rendijas_clasic_y_cuantica([1, 0, 0, 0, 0, 0, 0, 0],[[0, 0, 0, 0, 0, 0, 0, 0], 
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0],
                       [0, -1+1j/math.sqrt(6), 0, 1, 0, 0, 0, 0],
                       [0, -1-1j/math.sqrt(6), 0, 0, 1, 0, 0, 0],
                       [0, 1-1j/math.sqrt(6), -1+1j/math.sqrt(6), 0, 0, 1, 0, 0],
                       [0, 0, -1-1j/math.sqrt(6), 0, 0, 0, 1, 0],
                       [0, 0, 1-1j/math.sqrt(6), 0, 0, 0, 0, 1]], 3)
        self.assertAlmostEqual(rendijas_clasic_y_cuantica, "[0j, 0j, 0j, (-0.7071067811865475+0.2886751345948129j), (-0.7071067811865475-0.2886751345948129j), 0j, (-0.7071067811865475-0.2886751345948129j), (0.7071067811865475-0.2886751345948129j)]") 


if __name__ == "__main__":
    unittest.main()
