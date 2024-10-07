import numpy as np
import scipy.integrate as sci
from datetime import datetime

from config.Rocket_Config import RocketConfig, Motor
from config.Aero_Config import Aero



# Main differential equation 
def derivative(state: np.array, t: float, rocket: RocketConfig, motor: Motor) -> np.ndarray:
    """State space equation to be integrated numericaly. 

    Args:
        state (np.array): State Vector [altitude - m, velocity - m/s, mass -kg]
        t (float): Time of current step in integratoin - seconds
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
    stateout = sci.odeint(derivative, inital_conditions, time_array, args=(rocket, motor,))
    
    altitude = stateout[:,0]
    velocity = stateout[:,1]
    mass = stateout[:,2]
    
    return stateout

class SimulationData:  
    def __init__(self, parent_gui = None):
        self.altitude = np.empty(1)
        self.velocity = np.empty(1)
        self.mass = np.empty(1)
        self.time = np.empty(1)
        # Conditonaly set attribute if parnet gui widget is provided
        setattr(self, "parent_gui", parent_gui) if parent_gui is not None else None
        
    
    def update_data(self, statevector: np.ndarray = None, time: np.ndarray = None, parent_gui = None):
        current_time = datetime.now().strftime('%H:%M:%S')

        if statevector is not None:
            self.altitude = statevector[:,0]
            self.velocity = statevector[:,1]
            self.mass = statevector[:,2]
        
        if time is not None:
            self.time = time
        
        if parent_gui is not None:

            parent_gui.appendText(f'\nSim ({current_time}):')
            parent_gui.appendText(f'Apogee:  {np.max(self.altitude):.2f}')
            parent_gui.appendText(f'Maxium Velocity:  {np.max(self.velocity):.2f}')
        else:
            print(f'\nSimu ({current_time}):')
            print(f'Apogee:  {np.max(self.altitude):.2f}')
            print(f'Maxium Velocity:  {np.max(self.velocity):.2f}')
        
        
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