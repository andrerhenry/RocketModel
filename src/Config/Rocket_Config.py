from numpy import abs, pi



class RocketConfig:    
    def __init__(self, rocket_mass_0: float, drag_coefficient: float, diameter: float) -> None:
        """Initalize and storage of rocket charitaristic variables

        Args:
            rocket_mass_0 (float): Intial mass of rocket - Kg
            drag_coefficient (float): Coefficient of aerodynamic drag - unitless
            diameter (float): Diameter of rocket - meters
        """
        self.rocket_mass_0 = rocket_mass_0
        self.drag_coefficient = drag_coefficient
        self._diameter = diameter
        self._cross_sect_area = self._cross_sect_area_calc(diameter)
        pass
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, new_diameter):
        # Set Cross sectional aera on change of diameter
        self._cross_sect_area = self._cross_sect_area_calc(new_diameter)
        self._diameter = new_diameter

    @property
    def cross_sect_area(self):
        return self._cross_sect_area
    
    def _cross_sect_area_calc(self, diameter: float) -> float:
        """Calcualte the cross sectional area

        Args:
            diameter (float): Diameter of Rocket - meters

        Returns:
            float: Cross sectional aera - meters^2
        """        
        return pi*(diameter/2)**2
        

class Motor():
    GRAVITY = -9.81
    
    def __init__(self, mass_fuel: float, thrust_avg: float, total_impulse: float, total_burn_time: float) -> None:
        """Inital motor perameters

        Args:
            mass_fuel (float): Mass of fuel to burned - Kg
            thrust_avg (float): Average trust of motor - Newtons
            total_impulse (float): Total Impulse  - Newton*seconds
            total_burn_time (float): Burn Time - seconds
        """        
        self._mass_fuel = mass_fuel
        self.thrust_avg = thrust_avg
        self._total_impulse = total_impulse
        self.burn_time = total_burn_time
        self._ISP = self.spcific_impulse()
        pass
       
    @property
    def mass_fuel(self):
        return self._mass_fuel
    
    @mass_fuel.setter
    def mass_fuel(self, new_mass_fuel):
        self._mass_fuel = new_mass_fuel
        self._ISP = self.spcific_impulse()
    
    @property
    def total_impulse(self):
        return self._total_impulse
    
    @total_impulse.setter
    def total_impulse(self, new_total_impulse):
        self._total_impulse = new_total_impulse
        self._ISP = self.spcific_impulse()
        
    @property
    def ISP(self):
        return self._ISP

    def spcific_impulse(self) -> float:
        return self._total_impulse/(self._mass_fuel*abs(self.GRAVITY))

    
    def motor_output(self, t: float) -> tuple [float, float]:
        """Motor_output is the returns the thrust and mass_dot

        Args:
            t (float): Simulation time - seconds

        Returns:
            tuple [float, float]: f_thrust - Newtons, mass_dot - Kg/second
        """
                        
        if (t < self.burn_time):
            f_thrust = self.thrust_avg
        else:
            f_thrust = 0.0
            
        exit_velcoity = self.ISP * self.GRAVITY
        mass_dot = f_thrust/exit_velcoity
        return f_thrust, mass_dot
        
        __doc__ = __init__.__doc__
        

if __name__ == "__main__":
    # testing rocket
    rocket_mass_0 = 32098/1000 # kilograms
    drag_coefficient = 0.36 #cf
    diameter = 0.155 # meters
    rocket = RocketConfig(rocket_mass_0, drag_coefficient, diameter)
    
    
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
    
    
    print(getattr(rocket, "rocket_mass_0"))
    """
    Nmotor.mass_fuel = 8
    print(Nmotor.mass_fuel, Nmotor.ISP)
    Nmotor.total_impulse = 15000.0
    print(Nmotor.total_impulse, Nmotor.ISP)
   """
    #print(Nmotor.motor_output(1), type(Nmotor.motor_output(1)) )