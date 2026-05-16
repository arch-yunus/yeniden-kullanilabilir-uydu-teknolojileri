"""
Atomic Oxygen (ATOX) Corrosion Model
------------------------------------
This script models the material erosion (mass loss) due to Atomic Oxygen
flux in VLEO based on material reactivity and orbital exposure time.

Usage:
    python atox_corrosion_model.py
"""

def calculate_erosion(flux_atoms_cm2_s, reactivity_cm3_atom, duration_days, area_cm2, density_g_cm3):
    """
    Calculates erosion depth (cm) and mass loss (grams).
    """
    total_seconds = duration_days * 86400
    total_fluence = flux_atoms_cm2_s * total_seconds
    
    # Erosion depth = Fluence * Reactivity
    erosion_depth_cm = total_fluence * reactivity_cm3_atom
    
    # Mass loss = Depth * Area * Density
    mass_loss_g = erosion_depth_cm * area_cm2 * density_g_cm3
    
    return erosion_depth_cm, mass_loss_g

if __name__ == "__main__":
    print("-" * 50)
    print("ATOX MATERIAL CORROSION SIMULATOR")
    print("-" * 50)
    
    # Environmental parameters (Typical VLEO @ 300km)
    flux = 5.0e14  # atoms / cm^2 / s
    exposure_days = 365  # 1 year
    
    # Material database (Reactivity in 10^-24 cm^3 / atom)
    materials = {
        "Kapton (Polyimide)": 3.0e-24,
        "Teflon (FEP)": 0.3e-24,
        "Carbon Fiber": 2.1e-24,
        "Silver (Ag)": 10.5e-24
    }
    
    area = 100.0  # cm^2
    density = 1.5  # g/cm^3 (approx)
    
    print(f"{'Material':<20} {'Erosion Depth (mm)':<20} {'Mass Loss (g)':<15}")
    print("-" * 55)
    
    for mat, react in materials.items():
        depth_cm, mass_loss = calculate_erosion(flux, react, exposure_days, area, density)
        depth_mm = depth_cm * 10
        print(f"{mat:<20} {depth_mm:<20.4f} {mass_loss:<15.4f}")
    
    print("-" * 55)
    print("Caution: High reactivity materials (like Silver) require specialized")
    print("coatings for VLEO missions.")
