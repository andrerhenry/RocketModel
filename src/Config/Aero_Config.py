from numpy import exp, sign

from config.Rocket_Config import RocketConfig



class Aero:
    def  __init__(self, rocket: RocketConfig) -> None:
        """Provides the aerodynamic charicatistices of a rocket

        Args:
            rocket (RocketConfig): _description_
        """        
        self.rocket = rocket
        pass

    def F_aero_drag(self, velocity: float, altitude: float) -> float:
        """ Computes force of aerodynamics drag from the velocity in air stream and the atmosphic pressure

        Args:
            velocity (float): Velocity in airstream - meters/second
            altitude (float): Atltitude - meters

        Returns:
            float: Force of aerodynamic drag  - Newtons
        """        
        density = self.air_density(altitude)
        f_aero_drag = self.rocket.drag_coefficient* 0.5 * density * self.rocket.cross_sect_area * velocity**2 *sign(velocity)
        return f_aero_drag

    def air_density(self, altitude: float) -> float:
        """Suporting function to calclate the atmosphearic air density at an altitude. 
        Built off Ideal Gas Law.
        
        Switch to interpulate air density in future release

        Args:
            altitude (float): Alitude - meters

        Returns:
            float: Air Desnity - Pascales 
        """        
        # alternate method would be to intepulate with data
        # Need to verify Constants or switch to interpulation
        beta = 0.1354/1000.0 # Density Constant - confrim Constant
        density_sealevel = 1.225 # kg/m^3 at sea level
        density = density_sealevel * exp(-beta*altitude)
        return density

    
if __name__ == "__main__":
    #print(Aero.F_aero_drag(100.0, 500.0))
    pass