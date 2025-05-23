from numpy import exp, sign, genfromtxt, interp
from pathlib import Path

from rocket_model.config.rocket_config import RocketConfig

# Air density data taken from http://www.braeunig.us/space/atmos.htm
data_path = Path(__file__).parent
data = genfromtxt(data_path/"atmospheric_properties.csv", delimiter=",", skip_header=1)


class Aero:
    def  __init__(self, rocket: RocketConfig) -> None:
        """Provides the aerodynamic charicatistices of a rocket

        Args:
            rocket (RocketConfig): Rocket class container
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
        density = self.atmospheric_density(altitude)
        f_aero_drag = self.rocket.drag_coefficient* 0.5 * density * self.rocket.cross_sect_area * velocity**2 * sign(velocity)
        return f_aero_drag

    def air_density(self, altitude: float) -> float:
        """Calculates the atmosphearic air density at an altitude 
        using Ideal Gas Law.
        
        *Switch to interpulate air density in future release*

        Args:
            altitude (float): Alitude - meters

        Returns:
            float: Air Desnity - Pascales 
        """        
        # alternate method would be to intepulate with data
        beta = 0.1354/1000.0 # Density Constant - confrim Constant
        density_sealevel = 1.225 # kg/m^3 at sea level
        density = density_sealevel * exp(-beta*altitude)
        return density

    def atmospheric_density(self, altitude: float) -> float:
        """Calculates the atmospheric air density at an altidude from tabluated data. 
         Air density data taken from http://www.braeunig.us/space/atmos.htm .

        Args:
            altitude (float): Atitude of rocket - meteres

        Returns:
            float: Air Density kilograms/meter^3
        """        
        return interp(altitude, data[:,0], data[:,3])
