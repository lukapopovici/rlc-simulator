# RLC Simulator

<p align="center">
  <img src="https://github.com/lukapopovici/rlc-simulator/assets/128390767/2bc999be-a161-4157-9126-17725b1d005d" width="450">
</p>

Aceasta este codul sursa pentru un simulator de circuit RLC. Programul randareaza o simulare interactiva a unui circuit RLC in serie, unde utilizatorul poate schimba valoarea componentelor, poate genera graful functiei de tensiune pe condensator, si de asemenea poate sa calculeze valoare a mai multor variabile specifice acestui tip de circuit.

## Requirements

Singurele "necesitati" pentru a compila fisierul executabil principal al programului și a-l rula sunt [pyinstaller](https://pyinstaller.org/en/stable/) și orice instalație Windows mai recenta decat Vista.

## Compilare

Pentru a compila executabilul princiapal trebuie rulat scriptul "compile.bat" cu privilegii de administrator.

## Utilizare

Pentru a porni programul, trebuie deschis fișierul "circuit.exe" din folderul principal.

### Verificarea valorii unei componente

Pentru a verifica valoarea unei componente trebuie dat click pe simbolul ei corespunzator, conform standardului [IEC](https://std.iec.ch/iec60617). Valoarea ei va fi afisata in partea de sus a ferestrei, cu tot cu unitatea de masura. 


https://github.com/lukapopovici/rlc-simulator/assets/128390767/33729698-fb73-43d9-8964-5e2ecc260402


### Modificarea valorii unei componente

Pentru a modifica valoarea unui componente, apăsați butonul "Valori RLC" din partea de stânga-jos a ferestrei. Se va deschide un meniu (ca un proces paralel) care permite editarea valorii componentei dorite. Pur și simplu trebuie modificat numărul de lângă numele său și apoi apăsați pe "START!". Sunt permise și numere cu virgulă mobilă.


https://github.com/lukapopovici/rlc-simulator/assets/128390767/9475f492-f90e-4f50-b515-16d91fae9b97


### Generarea grafului functiei de tensiune pe condensator.

Pentru a afișa graficul tensiunii pe condensator, apăsați butonul din partea de jos, în centrul ferestrei, intitulat "Graf uc(t)". Graficul afișat va acoperi doar primele 300 de nanosecunde de la pornirea circuitului.

https://github.com/lukapopovici/rlc-simulator/assets/128390767/db104274-1b3e-47b8-9892-dd4cf3feea31



### Calcularea variabilelor de circuit

În colțul din dreapta-jos al ferestrei, puteți apăsa butonul "Calcule" pentru a calcula valoarea unei variabile specifice circuitului RLC. Selectați numele acesteia din meniul care va apărea, apoi apăsați pe butonul "Calculează". Valoarea va fi afișată în partea de sus a ferestrei principale (fara unitatea de masura).

https://github.com/lukapopovici/rlc-simulator/assets/128390767/636c06cf-1fe5-4c4a-94cc-e026764adda8

Este posibila calcularea:
- pulsatiei oscilatiilor propii
- frecventa oscilatiilor propii
- perioada oscilatiilor propii
- coeficientului de amortizare
- timpului de injumatatire
- factorului de calitate
- decrementului logaritmic
- timpului de relaxare
- oscilatiilor efectuate intr-o perioada

## Caz de utilizare

![image](https://github.com/lukapopovici/rlc-simulator/assets/128390767/89bcdb35-69e0-4d99-94ef-c8efdb5884e8)

Programul este destinat studiului circuitului RLC in laboratorul de fizica al [universitatii mele](https://www.tuiasi.ro/), unde este instalat pe calculatoarele utilizate de studenti.
