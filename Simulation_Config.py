import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

from Rocket_Config import RocketConfig, Motor
from Aero_Config import Aero


# Main differential equation 
def Derivative(state: np.array, t: int, rocket: RocketConfig, motor: Motor) -> np.ndarray:
    """State space equation to be integrated numericaly. 

    Args:
        state (np.array): State Vector [altitude - m, velocity - m/s, mass -kg]
        t (int): Time of current step in integratoin - seconds
        rocket (RocketConfig): Rocketfig class containing perameters/method of rocket
        motor (Motor): Motor class conatin peramters/methods of the motor

    Returns:
        np.ndarray: State array dervivative to be integrated [altitude_dot - m/s, velcoity_dot - m/s**2, mass_dot - kg/s]
    """    
    # State vector
    altitude = state[0]
    velocity = state[1]
    mass = state[2]
    
    GRAVITY = 9.81 # m/s^2 change in gravity considered negligible
    aero = Aero(rocket)
    
   
    # Forces
    f_gravity = GRAVITY * mass
    f_aero = aero.F_aero_drag(velocity, altitude)
    f_thrust, mass_dot = motor.motor_output(t)
    
    f_net = f_thrust - f_aero - f_gravity
    acceleration = f_net/mass
    
    
    # Stop integratoin when Rocket returns to ground
    if (altitude < 0):
        statedot = np.array([0, acceleration, mass_dot])
    else:
        statedot = np.array([velocity, acceleration, mass_dot])
    
    return statedot


def simulation(inital_conditions: np.array, time_array: np.array, rocket: RocketConfig, motor: Motor) -> np.ndarray:
    """Main Simulation fucntion that integrate the system dynamics

    Args:
        inital_conditions (np.array): Inital condition of the system [altitude - m, velocity - m/s, mass -kg]
        time_array (np.array): Time array (sec)
        rocket (RocketConfig): _description_
        motor (Motor): _description_

    Returns:
        np.ndarray: State vector of simulation data [altitude - m, velocity - m/s, mass -kg]
    """
    stateout = sci.odeint(Derivative, inital_conditions, time_array, args=(rocket, motor,))
    
    zout = stateout[:,0]
    zvout = stateout[:,1]
    massout = stateout[:,2]
    
    #troubshooting outputs
    # Results 
    print('\n\n\nResults:')
    print(f'Apogee:  {np.max(zout):.2f}')
    print(f'Maxium Velocity:  {np.max(zvout):.2f}')
    print(f'ISP:  {np.max(motor.ISP):.2f}')
    print('\n')
    
    #plot
    plt.figure()
    plt.plot(time_array,zout)
    plt.title('Altitude')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid()
    plt.show()

    return stateout

class SimulationData:
        #testing
    import time
    t = np.linspace(0, 10, 101)
    x = np.sin(t + time.time())
    
    def __init__(self):
        self.altitude = np.empty(1)
        self.velocity = np.empty(1)
        self.mass = np.empty(1)
        self.time = np.empty(1)
        
    
    def update_data(self, statevector: np.ndarray = None, time: np.ndarray = None):
        if statevector is not None:
            self.altitude = statevector[:,0]
            self.velocity = statevector[:,1]
            self.mass = statevector[:,2]
        
        if time is not None:
            self.time = time
        
        
        
class Time:
    def __init__(self, start_time: int, end_time: int, step: float):
        """Holds time data perameteres \n
        time_array() function generates the time array need for simulation

        Args:
            start_time (int): Start time (sec)
            end_time (int): End time (sec)
            step (float): Simulation step time (sec)
        """        
        self._start_time = start_time
        self._end_time = end_time
        self._step = step
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, new_start_time):
        self._start_time = new_start_time
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, new_end_time):
        self._end_time = new_end_time
    
    @property
    def step(self):
        return self._step
    
    @step.setter
    def step(self, new_step):
        self._step = new_step
    
    def time_array(self) -> np.ndarray:
        """Generates a time array to simulate across

        Returns:
            np.ndarray: Time array
        """        
        return np.arange(self._start_time, self._end_time, self._step)