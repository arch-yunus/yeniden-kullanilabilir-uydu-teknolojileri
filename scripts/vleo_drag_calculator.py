"""
VLEO Drag and Orbital Decay Calculator
--------------------------------------
This script calculates the aerodynamic drag force on a satellite in 
Very Low Earth Orbit (VLEO) and estimates the daily altitude loss.

Usage:
    python vleo_drag_calculator.py
"""

import math

def get_density(altitude_km):
    """
    Exponential model for atmospheric density (simplified).
    Valid for altitudes between 200km and 500km.
    """
    # Reference values (Altitude in km, Density in kg/m^3)
    # 200km: 2.5e-10
    # 300km: 1.9e-11
    # 400km: 2.8e-12
    # 500km: 5.2e-13
    
    h0 = 200  # Reference altitude
    rho0 = 2.5e-10  # Reference density at 200km
    H = 45  # Scale height in km (approx for VLEO)
    
    return rho0 * math.exp(-(altitude_km - h0) / H)

def calculate_drag(altitude_km, mass_kg, area_m2, Cd=2.2):
    """
    Calculates drag force (N) and deceleration (m/s^2).
    Cd: Drag coefficient (typically 2.2 for satellites in rarefied flow)
    """
    rho = get_density(altitude_km)
    
    # Orbital velocity (v = sqrt(G*M / r))
    R_earth = 6371  # km
    G_M = 3.986e5  # Earth Gravitational Parameter km^3/s^2
    r = R_earth + altitude_km
    v_km_s = math.sqrt(G_M / r)
    v_m_s = v_km_s * 1000
    
    # Drag Force: Fd = 0.5 * rho * v^2 * Cd * A
    drag_force = 0.5 * rho * (v_m_s**2) * Cd * area_m2
    
    # Deceleration: a = F / m
    deceleration = drag_force / mass_kg
    
    return drag_force, deceleration, v_m_s

def estimate_altitude_loss(altitude_km, mass_kg, area_m2, Cd=2.2):
    """
    Estimates daily altitude loss in km.
    Formula: delta_a / delta_t = -2 * a_drag * (r / v)
    """
    drag_force, deceleration, v_m_s = calculate_drag(altitude_km, mass_kg, area_m2, Cd)
    
    R_earth = 6371  # km
    r_m = (R_earth + altitude_km) * 1000
    
    # Altitude loss rate (m/s)
    da_dt = -2 * deceleration * (r_m / v_m_s)
    
    # Daily loss in km
    daily_loss_km = (da_dt * 86400) / 1000
    
    return daily_loss_km

if __name__ == "__main__":
    print("-" * 50)
    print("VLEO ORBITAL DECAY SIMULATOR")
    print("-" * 50)
    
    # Satellite parameters (Default: Small Sat)
    mass = 50.0  # kg
    area = 0.2   # m^2 (Cross-sectional area)
    
    altitudes = [250, 300, 350, 400]
    
    print(f"{'Altitude (km)':<15} {'Drag Force (N)':<20} {'Daily Loss (km)':<20}")
    print("-" * 55)
    
    for alt in altitudes:
        force, accel, v = calculate_drag(alt, mass, area)
        loss = estimate_altitude_loss(alt, mass, area)
        print(f"{alt:<15} {force:<20.6f} {abs(loss):<20.4f}")
    
    print("-" * 55)
    print("Note: This model uses a simplified exponential atmosphere.")
    print("Actual decay depends on solar activity and satellite orientation.")
