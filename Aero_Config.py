from numpy import exp, sign

from Rocket_Config import RocketConfig

class Aero:
    def  __init__(self, rocket: RocketConfig) -> None:
        self.rocket = rocket
        pass
    
    def air_density(self, altitude):
        # alternate method would be to intepulate with data
    
        # Need to verify Constants or switch to interpulation
        beta = 0.1354/1000.0 # Density Constant - confrim Constant
        density_sealevel = 1.225 # kg/m^3 at sea level
        density = density_sealevel * exp(-beta*altitude)
        return density

    # Dynamic pressure calc
    def F_aero_drag(self, velocity: float, altitude: float) -> float:
        """ Computes force of aerodynamics drag from the velocity in air stream and the atmosphic pressure

        Args:
            velocity (float): velocity in airstream - meters/second
            altitude (float): atltitude - meters

        Returns:
            float: force of aerodynamic drag  - Newtons
        """        
        density = self.air_density(altitude)
        f_aero_drag = self.rocket.drag_coefficient* 0.5 * density * self.rocket.cross_sect_area * velocity**2 *sign(velocity)
        return f_aero_drag