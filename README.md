# RocketModel

Rocket model is an easy and approachable way to get first round rocket flight simulations without having to build a Open Rocket model or diving into RocketPy simulations. It features a GUI for easy edditing of simulation parameters and a variety of plots for the simulation. Before using Rocket Model one should note the major assumptions of the model:
  - Gravity is considered constant
  - The rockets angle of attack is zero for the flight
  - The rockets is stable and rigid
  - The motor burns consistently and evenly at average thrust


## Installation 

### Application Download
RocketModel application can be installed from [Releases.](https://github.com/andrerhenry/RocketModel/releases)

### Cloning Repository
To install for development or to run the source code, clone the the repository with:
```bash 
git clone https://github.com/andrerhenry/RocketModel
cd RocketModel
```

### Setting Up Environment
UV is implemented to manage the project environment. After cloning the repository, run:
```bash
uv sync
```

This will install the dependencies and set up the virtual environment.

To activate the environment, use:
```bash
source .venv/bin/activate
```



## Running Rocket Model
After installing dependencies, the project can now be run with: 
```bash
uv run src/rocket_model/main.py
```
or 
```bash
python src/rocket_model/main.py
```


## User Guide
### Running the Rocket Model Application
To start an simulation, first edit the Rocket Configuration. This is the basic attributes of your rocket.

![Screenshot of Rocket Configuration section.](https://github.com/user-attackments/assets/b0e8b07d-c86d-4e4d-b959-236128776c02)

Next, fill out the Motor Configuration with you data from your motor data sheet:

![Example Rocket Motor datasheet](https://github.com/user-attackments/assets/b6a80b14-fda1-4d6c-b557-83f3dfa79031)

![Screenshot of Motor Configuration section.](https://github.com/user-attackments/assets/cbbe864a-ef3f-454d-acd7-3c64210bc925)

Adjust the simulation time and simulation resolution as needed:

![Screenshot of time parameters](https://github.com/user-attackments/assets/2efcc23b-6bb7-44a6-b0c3-d8c0a374d575)

The figure section shows plots of simulation. The current plot can be changed with the drop down menu at the bottom of the window. 

![Screenshot of figure area](https://github.com/user-attackments/assets/bb52cc3e-6fcd-402f-82e8-88c0aa9de203)


### Running Rocket Model Script
The simulation module can be run as a standalone file if you prefer to run the simulation in a script form. Edit the if __name__== __main__section and than run the simulation module with either of the following commands:
```bash
uv run src/rocket_model/simulation.simulation.py
```
or 
```bash
python src/rocket_model/simulation.simulation.py
```

## Acknowledgements 

I would like to give a special thanks to Dr. Carlos Montalvo of University of South Alabama and his video series that showed me that simulations of rockets in Python is more accessible than I initially imagined.

I would also like to extend my thanks to the Reddit community, r/learnpython,  for the countless lessons and invaluable interactions that greatly aided my journey in learning Python.

## License
Rocket Module is licensed under the MIT License.
