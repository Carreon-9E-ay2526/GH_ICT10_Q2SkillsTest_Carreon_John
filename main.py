#Periodic Table Information Finder
from pyscript import display, document


def check_details(e):
    document.getElementById('result').innerHTML = " "
    elements = str(document.getElementById('non-metal').value)
    elements = elements.capitalize()


    symbol = ['H','He','C','N','O','F','Ne','P','S','Cl','Ar','Se','Br','Kr','I','Xe','Rn']

    element = ['Hydrogen', 'Helium', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Selenium', 'Bromine', 'Krypton', 'Iodine', 'Xenon', 'Radon']

    atomic_number = [1, 2, 6, 7, 8, 9, 10, 15, 16, 17, 18, 34, 35, 36, 53, 54, 86]

    atomic_mass = [1.01, 4.00,12.01,14.01,16.00,19.00,20.18,30.97,32.06,35.45,39.95,78.97,79.90,83.80,126.90,131.29,222]

    document.getElementById('result').innerHTML = "Symbol: " + symbol[symbol.index(elements)] + "<br>" + "Element: " + element[symbol.index(elements)] + "<br>" + "Atomic Number: " + str(atomic_number[symbol.index(elements)]) + "<br>" + "Atomic Mass: " + str(atomic_mass[symbol.index(elements)])