import math

T = 310 # in Kelvin, 37 degrees Celsius
R = 8.314 # in J/mol/K
F = 96485 # in C/mol

def nernst_potential(conc_in, conc_out, z):
    """Return the Nernst potential for a given ion concentration
    gradient and charge. in mV
    
    Arguments:
    conc_in -- concentration of the ion inside the cell in mM
    conc_out -- concentration of the ion outside the cell in mM
    z -- charge of the ion
    """
    return round((R*T/F*z)*math.log(conc_out/conc_in) * 1000, 2)

conc_in = 140
conc_out = 55
z = 1

print(nernst_potential(conc_in, conc_out, z))
