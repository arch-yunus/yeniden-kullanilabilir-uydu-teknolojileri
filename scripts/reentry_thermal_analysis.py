"""
Re-entry Thermal Analysis - Stagnation Point Heat Flux
------------------------------------------------------
This script calculates the convective stagnation point heat flux for a 
spacecraft during atmospheric re-entry using the Sutton-Graves equation.

Formula: q_s = k * sqrt(rho / Rn) * V^3
Where:
    q_s : Heat flux (W/m^2)
    k   : Planetary constant (Earth: 1.7415e-4 kg^0.5 / m)
    rho : Atmospheric density (kg/m^3)
    Rn  : Nose radius (m)
    V   : Velocity (m/s)

Usage:
    python reentry_thermal_analysis.py
"""

import math

def calculate_heat_flux(rho, velocity, nose_radius, k=1.7415e-4):
    """
    Calculates the stagnation point heat flux.
    """
    if nose_radius <= 0:
        raise ValueError("Nose radius must be greater than zero.")
    
    # Sutton-Graves Equation
    q_s = k * math.sqrt(rho / nose_radius) * (velocity**3)
    
    return q_s

def get_tps_recommendation(heat_flux_wm2):
    """
    Provides a TPS material recommendation based on heat flux levels (W/cm^2).
    """
    # Convert W/m^2 to W/cm^2
    heat_flux_wcm2 = heat_flux_wm2 / 10000
    
    if heat_flux_wcm2 < 10:
        return "Low-temp Insulation (FRSI / AFRSI)"
    elif heat_flux_wcm2 < 50:
        return "HRSI Tiles (High-temperature Reusable Surface Insulation)"
    elif heat_flux_wcm2 < 200:
        return "RCC (Reinforced Carbon-Carbon) or Lightweight Ablators"
    else:
        return "High-density Ablator (PICA / PICA-X / Avcoat)"

if __name__ == "__main__":
    print("-" * 60)
    print("RE-ENTRY THERMAL ANALYSIS TOOL (Sutton-Graves Model)")
    print("-" * 60)
    
    # Typical Re-entry Scenario (LEO Return)
    v_entry = 7500  # m/s (approx orbital velocity)
    nose_rad = 0.5   # m (e.g., Small capsule or wing lead)
    
    # Altitudes to simulate (Altitude in km, Density in kg/m^3)
    # Density data based on US Standard Atmosphere (approx)
    trajectories = [
        {"alt": 80, "rho": 1.8e-5},
        {"alt": 70, "rho": 8.2e-5},
        {"alt": 60, "rho": 3.0e-4},
        {"alt": 50, "rho": 1.0e-3}
    ]
    
    print(f"{'Alt (km)':<10} {'Density (kg/m3)':<20} {'Heat Flux (W/cm2)':<20} {'TPS Selection'}")
    print("-" * 85)
    
    for point in trajectories:
        q_s = calculate_heat_flux(point["rho"], v_entry, nose_rad)
        q_s_wcm2 = q_s / 10000
        tps = get_tps_recommendation(q_s)
        
        print(f"{point['alt']:<10} {point['rho']:<20.2e} {q_s_wcm2:<20.2f} {tps}")
    
    print("-" * 85)
    print("Warning: This is a convective heating model. Radiative heating")
    print("becomes dominant at velocities > 10 km/s (Lunar/Interplanetary).")
