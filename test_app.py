import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_invsqrt(self):
        m=np.diag([4.,9.]);np.testing.assert_allclose(invsqrt(m)@m@invsqrt(m),np.eye(2))
    def test_centering(self):
        x=np.arange(60.).reshape(20,3);m=fit(x,x,k=2);np.testing.assert_allclose(((x-m['mx'])@m['px']).mean(axis=0),0,atol=1e-8)
    def test_zero_vectors(self):self.assertTrue(np.isfinite(normalize_rows(np.zeros((3,4)))).all())
