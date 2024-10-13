from __future__ import annotations

import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt
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



def simulation(inital_conditions: tuple[int, int, float], time: Time, rocket: RocketConfig, motor: Motor) -> tuple[ArrayLike, ArrayLike ]:
    """Main Simulation fucntion that integrate the system dynamics

    Args:
        inital_conditions (tuple): Inital condition of the system [altitude - m, velocity - m/s, mass -kg]
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
    state_dot = np.array([derivative(t, state, rocket, motor) for t, state in zip(solution.t, solution.y.T)]).T # transpose so size will match time

    return time, state, state_dot


class SimulationData:  
    """Class to store simulaiton data.
    
        Attr:
        meta_data (dict): Stores meta data of attributes: Label, Units, Data
    """    
    def __init__(self, parent_gui = None):
        self.time = np.empty(1)
        self.altitude = np.empty(1)
        self.velocity = np.empty(1)
        self.mass = np.empty(1)
        self.acceleration = np.empty(1)
        self.mass_dot = np.empty(1)

        # Conditonaly set attribute if parnet gui widget is provided
        setattr(self, "parent_gui", parent_gui) if parent_gui is not None else None
    
    meta_data = {
            "Altitude": {"label": "Altitude (m)", "units": "(m)", "data": "altitude"},
            "Velocity": {"label": "Velocity (m/s)", "units": "(m/s)", "data": "velocity"},
            "Acceleration": {"label": "Acceleration (m/s^2)", "units": "(m/s^2)", "data": "acceleration"},
            "Mass": {"label": "Mass (kg)", "units": "(kg)", "data": "mass"},
            "Mass_dot":{"label": "Mass_dot (kg/s)", "units": "(kg/s)", "data": "mass_dot"},
        }
    
    def update_data(self, time: np.ndarray = None, state: np.ndarray = None, state_dot: np.ndarray = None, parent_gui = None):
        """Stores the simulation data for analysis

        Args:
            time (np.ndarray, optional): Stores the time values. Defaults to None.
            state (np.ndarray, optional): Stores simulation values. Defaults to None.
            state_dot (np.ndarray, optional): Stores the derivative values. Defaults to None.
            parent_gui (QWidget, optional): parent widget when using a GUI. Defaults to None.
        """ 
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
        
        
if __name__ == "__main__":
    
    # testing rocket data
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
    
    time = Time(0, 63, 0.001)
    inital_conditions = np.array([0, 0, rocket.rocket_mass_0])
    
    time_array, state, state_dot = simulation(inital_conditions, time, rocket, Nmotor)
    
    data = SimulationData()
    data.update_data(time_array, state, state_dot)
    
    selected_data = "Altitude"
    
    fig, ax = plt.subplots()
    ax.plot(data.time, getattr(data, data.meta_data[selected_data]["data"]))
    ax.grid()
    ax.set_title(selected_data)
    ax.set_ylabel(data.meta_data[selected_data]["label"])
    ax.set_xlabel("Time (s)")
    plt.show()
    
    """plt.figure()
    plt.plot(t,zout)
    plt.title('Altitude')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid()"""
        

