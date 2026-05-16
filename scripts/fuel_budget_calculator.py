"""
OSAM Fuel Budget & Delta-V Calculator
-------------------------------------
Estimates the fuel mass required for RPO manevras and orbital changes
using the Tsiolkovsky Rocket Equation.

Usage:
    python fuel_budget_calculator.py
"""

import math

def calculate_fuel_mass(m_wet, delta_v, isp, g0=9.80665):
    """
    m_wet: Initial mass (kg)
    delta_v: Change in velocity (m/s)
    isp: Specific impulse (s)
    """
    # Rocket Equation: delta_v = isp * g0 * ln(m0 / mf)
    # mf = m0 / e^(delta_v / (isp * g0))
    
    m_dry = m_wet / math.exp(delta_v / (isp * g0))
    fuel_needed = m_wet - m_dry
    
    return fuel_needed, m_dry

if __name__ == "__main__":
    print("-" * 50)
    print("OSAM MISSION FUEL BUDGET CALCULATOR")
    print("-" * 50)
    
    initial_mass = 500.0  # kg
    
    # Maneuver Delta-V Requirements (m/s)
    maneuvers = {
        "Hohmann Transfer (LEO-GEO)": 3900.0,
        "Station Keeping (per year)": 50.0,
        "RPO Approach (Docking)": 20.0,
        "De-orbit Burn (VLEO)": 150.0
    }
    
    # Propulsion Systems (Specific Impulse in seconds)
    engines = {
        "Cold Gas": 70,
        "Chemical (Hydrazine)": 230,
        "Ion Thruster (Xenon)": 3000
    }
    
    print(f"Initial Satellite Mass: {initial_mass} kg\n")
    
    for engine_name, isp in engines.items():
        print(f"Engine: {engine_name} (Isp: {isp}s)")
        print(f"{'Maneuver':<30} {'Fuel Needed (kg)':<15}")
        print("-" * 45)
        for man, dv in maneuvers.items():
            fuel, dry = calculate_fuel_mass(initial_mass, dv, isp)
            print(f"{man:<30} {fuel:<15.2f}")
        print("-" * 45 + "\n")
