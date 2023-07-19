Documentatia in limba romana poate fi gasita [aici](/romana.md).

# RLC Simulator

<p align="center">
  <img src="https://github.com/lukapopovici/rlc-simulator/assets/128390767/2bc999be-a161-4157-9126-17725b1d005d" width="450">
</p>

This is the code for an RLC circuit simulator. The program renders an interactive representation of an RLC circuit with options to change the value of the components, render the graph of the voltage across the capacitor, and get the value of certain variables.

## Requirements

The only requirements for compiling the main executable of the program and running it are [pyinstaller](https://pyinstaller.org/en/stable/) and any Windows installation above Vista.

## Compilation

To compile it, you simply need to run the "compile.bat" script with administrator privileges.

## Usage

To start using the program, open circuit.exe within the root folder of the program.

### Checking the value of a component

To check the value of a component, simply click on the corresponding image on the circuit, and the value, along with the unit it's measured in, will be displayed on top.


https://github.com/lukapopovici/rlc-simulator/assets/128390767/33729698-fb73-43d9-8964-5e2ecc260402


### Modifying the value of a component

To modify the value of a component, click on the "Valori RLC" button on the bottom-left of the window. This will open a menu as a parallel process that allows you to edit the value of the desired component. Simply change the number next to its name and then click on "START!". Floating-point numbers are allowed.


https://github.com/lukapopovici/rlc-simulator/assets/128390767/9475f492-f90e-4f50-b515-16d91fae9b97


### Rendering the voltage graph

To render the graph of the voltage across the capacitor, press the button on the middle-bottom of the window. This action triggers the rendering of the capacitor's voltage function, specifically for the initial 300 nanoseconds of the circuit's operation.



https://github.com/lukapopovici/rlc-simulator/assets/128390767/db104274-1b3e-47b8-9892-dd4cf3feea31



### Getting circuit variables

On the bottom-right corner of the window, you can press the "Calcule" button to get the value of a variable specific to the circuit. Simply select its name from the menu that will pop up, then click on the "Calculeaza" button. The value will be printed on the top of the main window.


https://github.com/lukapopovici/rlc-simulator/assets/128390767/636c06cf-1fe5-4c4a-94cc-e026764adda8


## Use Case

![image](https://github.com/lukapopovici/rlc-simulator/assets/128390767/89bcdb35-69e0-4d99-94ef-c8efdb5884e8)

This program is meant to be used within my [University's](https://www.tuiasi.ro/) physics lab during the study of the RLC circuit. Outside of this, it has little practicality.




