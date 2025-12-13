from . import jacobian_generic as jacobian_generic, kummer_surface as kummer_surface

class HyperellipticJacobian_g2(jacobian_generic.HyperellipticJacobian_generic):
    def kummer_surface(self): ...
