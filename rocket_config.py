from numpy import abs

class Motor():
    GRAVITY = -9.81
    
    def __init__ (self, mass_fuel, trust_avg, total_impulse):
        self.mass_fuel = mass_fuel
        self.trust_avg = trust_avg
        self.total_impulse = total_impulse
        self.ISP = self.spcificImpulse()
        
    
    def spcificImpulse(self) -> float:
            return self.total_impulse/(self.mass_fuel*abs(self.GRAVITY))
    
    def fThrust(self, t: float) -> tuple [float, float]:
                
        if (t < 4.4):
            f_thrust = self.trust_avg
        else:
            f_thrust = 0.0
        exit_velcoity = self.ISP * self.GRAVITY
        mass_dot = f_thrust/exit_velcoity
        return f_thrust, mass_dot
        
        

if __name__ == "__main__":
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse)
    
    print(Nmotor.fThrust(1), type(Nmotor.fThrust(1)) )