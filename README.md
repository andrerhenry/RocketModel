# RocketModel

Rocket model is any easy and approachable way to get first round rocket flight simulations without having to build a Open Rocket model or diving into RocketPy simulations. It features a GUI for easy edditing of simlation perameters and a veriety of plots for the simulation. Before using Rocket Model one should note the major assuptions of the model:
  - Gravity is concidered constant
  - The rockets angle of attach is zero for the flight
  - The rockets is stable and ridged
  - The motor burns consitanly and evenly at average thrust


## Installation 

### Applcation Download
RocketModel application can be installed from [Releases.](https://github.com/andrerhenry/RocketModel/releases)

### Cloning Repository
To install for devlopement or to run the source code, clone the the reposity with:
```bash 
git clone https://github.com/andrerhenry/RocketModel
cd RocketModel
```

### Installing Dependacies
Poetry has been implemented to manage the project dependacies. Before you install dependencies, ensure you have poetry installed:
```bash
  
```
Then install the project dependancies with:
```bash
poetry install
```
> **Note**: 
> Poetry may install virtual environments in deep directory structures by default, which can cause long path issues on some systems.  
> To avoid this, you can set a custom, shorter path for your virtual environments by running:
> 
> ```bash
> poetry config virtualenvs.path C:\venvs
> ```
> 
> You can replace `C:\venvs` with a directory of your choice.


## Running Rocket Model
After installing dependacies, the project can now be run with: 
```bash
poetry run python src/main.py
```
or 
```bash
python src/main.py
```


## User Guide
### Running the Rocket Model Application
To start an simulation, first edit the Rocket Configureation. This is the basic attributes of your rocket.

![Screenshot of Rocket Configuration section.](https://github.com/user-attachments/assets/b0e8b07d-c86d-4e4d-b959-236128776c02)

Next, fill out the Motor Configuration with you data from your motor data sheet:

![Example Rocket Motor datasheet](https://github.com/user-attachments/assets/b6a80b14-fda1-4d6c-b557-83f3dfa79031)

![Screenshot of Motor Configuration section.](https://github.com/user-attachments/assets/cbbe864a-ef3f-454d-acd7-3c64210bc925)

Adjust the simulation time and simulation resaluiton as needed:

![Screenshot of time perameters](https://github.com/user-attachments/assets/2efcc23b-6bb7-44a6-b0c3-d8c0a374d575)

The figure section shows plots of simulation. The current plot can be changed with the drop down menu at the bottom of the window. 

![Screenshot of figure aera](https://github.com/user-attachments/assets/bb52cc3e-6fcd-402f-82e8-88c0aa9de203)


### Running Rocket Model Script
The simulaiton module can be run as a standalone file if you perfer to run the simulation in a script form. Edit the if __name__== __main__section and then run the simulation module with either of the following commands:
```bash
poetry run python src/rocket_model/simulation.simulation.py
```
or 
```bash
python src/rocket_model/simulation.simulation.py
```

## Acknoledgements 

I would like to give a special thanks to Dr. Carlos Montalvo of University of South Alabama and his video series that showed me that simulations of rockets in Python is more accessible then I initally imagined.

I would also like to extend my thanks to the Reddit community, r/learnpython,  for the countless lessons and invaluable interactions that greatly aided my journey in learning Python.

## License
Rocket Module is licensed under the MIT License.
