from constants import R, T, F
import math

def ghk_eqn(
    Pk,
    PNa,
    PCl,
    K_out,
    K_in,
    Na_out,
    Na_in,
    Cl_out,
    Cl_in,
):
    """Calculate the GHK equation for the cell membrane.

    Parameters
    ----------
    Pk : float
        The permeability of potassium.
    PNa : float
        The permeability of sodium.
    PCl : float
        The permeability of chloride.
    K_out : float
        The concentration of potassium outside the cell.
    K_in : float
        The concentration of potassium inside the cell.
    Na_out : float
        The concentration of sodium outside the cell.
    Na_in : float
        The concentration of sodium inside the cell.
    Cl_out : float
        The concentration of chloride outside the cell.
    Cl_in : float
        The concentration of chloride inside the cell.

    Returns
    -------
    float
        The GHK equation for the cell membrane in mV
    """
    return round(R*T/F * math.log((Pk*K_out + PNa*Na_out + PCl*Cl_in)/(Pk*K_in + PNa*Na_in + PCl*Cl_out)) * 1000, 2)


print(ghk_eqn(100, 4, 10, 55, 140, 105, 10, 119, 2))