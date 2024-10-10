from __future__ import annotations

import numpy as np
import scipy.integrate as sci
from datetime import datetime
from typing import TYPE_CHECKING, Sequence

from rocket_model.config.rocket_config import RocketConfig, Motor
from rocket_model.config.aero_config import Aero

if TYPE_CHECKING:
    from numpy.typing import ArrayLike


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
    
    def get_time_array(self) -> np.ndarray:
        """Generates a time array to simulate across

        Returns:
            np.ndarray: Time array
        """        
        return np.arange(self._start_time, self._end_time, self._step)


# Main differential equation 
def derivative(t: float, state: np.array, rocket: RocketConfig, motor: Motor) -> np.ndarray:
    """State space equation to be integrated numericaly. 

    Args:
        state (np.array): State Vector [altitude - m, velocity - m/s, mass -kg]
        t (float): Time of current step in integratoin - seconds
        rocket (RocketConfig): Rocketfig class containing perameters/method of rocket
        motor (Motor): Motor class conatin peramters/methods of the motor

    Returns:
        np.ndarray: State array dervivative to be integrated [altitude_dot - m/s, velcoity_dot - m/s**2, mass_dot - kg/s]
    """    
    GRAVITY = 9.81 # m/s^2 change in gravity considered negligible
    aero = Aero(rocket)

    # State vector
    altitude = state[0]
    velocity = state[1]
    mass = state[2]
    
    # Forces
    f_gravity = GRAVITY * mass
    f_aero = aero.F_aero_drag(velocity, altitude)
    f_thrust, mass_dot = motor.motor_output(t)
    
    f_net = f_thrust - f_aero - f_gravity
    acceleration = f_net/mass
    
    state_dot = np.array([velocity, acceleration, mass_dot])
    
    return state_dot


# Define an event function to stop integration when z (position) goes below zero
def ground_event(t, state, *args):
    return state[0]
ground_event.terminal = True  # Stop the integration when the event is triggered
ground_event.direction = -1   # The event occurs when z is decreasing



def simulation(inital_conditions: tuple[int, int, float], time: Time, rocket: RocketConfig, motor: Motor) -> tuple[asarray, asarray ]:
    """Main Simulation fucntion that integrate the system dynamics

    Args:
        inital_conditions (np.array): Inital condition of the system [altitude - m, velocity - m/s, mass -kg]
        time_array (np.array): Time array (sec)
        rocket (RocketConfig): _description_
        motor (Motor): _description_

    Returns:
        np.ndarray: State vector of simulation data [altitude - m, velocity - m/s, mass -kg]
        np.ndarray: State derivative vector of simulation data [velocity - m/s, acceleration - m/s^2, mass_dot - kg/s]
    """
    t_span = (time.start_time, time.end_time)
    
    solution = sci.solve_ivp(derivative, t_span, inital_conditions, t_eval=time.get_time_array(), events = ground_event, args=(rocket, motor,))
    
    time = solution.t    
    state = solution.y
    state_dot = np.array([derivative(t, state, rocket, motor) for t, state in zip(solution.t, solution.y.T)]).T # Transpost length will be the same as time
    print(np.shape(time))
    print(np.shape(state))
    print(np.shape(state_dot))
    return time, state, state_dot


class SimulationData:  
    def __init__(self, parent_gui = None):
        self.time = np.empty(1)
        self.altitude = np.empty(1)
        self.velocity = np.empty(1)
        self.mass = np.empty(1)
        self.acceleration = np.empty(1)
        self.mass_dot = np.empty(1)

        # Conditonaly set attribute if parnet gui widget is provided
        setattr(self, "parent_gui", parent_gui) if parent_gui is not None else None
        
    
    def update_data(self, time: np.ndarray = None, state: np.ndarray = None, state_dot: np.ndarray = None, parent_gui = None):
        self.current_time = datetime.now().strftime('%H:%M:%S')

        if time is not None:
            self.time = time
        
        if state is not None:
            self.altitude = state[0]
            self.velocity = state[1]
            self.mass = state[2]
            
        if state_dot is not None:
            self.acceleration = state_dot[1]
            self.mass_dot = state_dot[2]

        
        if parent_gui is not None:
            parent_gui.appendText(f'\nSim ({self.current_time}):')
            parent_gui.appendText(f'Apogee:  {np.max(self.altitude):.2f}')
            parent_gui.appendText(f'Maxium Velocity:  {np.max(self.velocity):.2f}')
            parent_gui.appendText(f'Maxium Acceleration:  {np.max(self.acceleration):.2f}')
            
        else:
            print(f'\nSim ({self.current_time}):')
            print(f'Apogee:  {np.max(self.altitude):.2f}')
            print(f'Maxium Velocity:  {np.max(self.velocity):.2f}')
            print(f'Maxium Acceleration:  {np.max(self.acceleration):.2f}')
        
        
