"""
REUSABLE_SAT Mission Control CLI
--------------------------------
A unified terminal interface to access all orbital simulation tools.

Usage:
    python mission_control_cli.py
"""

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print("      🛰️  REUSABLE_SAT MISSION CONTROL SYSTEM  🛰️")
    print("=" * 60)
    print("  Unified Command Center for Orbital Engineering Tools")
    print("=" * 60 + "\n")

def run_script(script_name):
    print(f"\n[SYSTEM] Launching {script_name}...")
    try:
        # Check if scripts/ prefix is needed
        path = f"scripts/{script_name}" if os.path.exists(f"scripts/{script_name}") else script_name
        os.system(f"{sys.executable} {path}")
    except Exception as e:
        print(f"[ERROR] Could not execute script: {e}")
    input("\n[SYSTEM] Press Enter to return to main menu...")

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("  [1] Orbital Decay & Drag Simulator (VLEO)")
        print("  [2] Atomic Oxygen (ATOX) Corrosion Model")
        print("  [3] OSAM Fuel Budget & Delta-V Calculator")
        print("  [4] View Technical Glossary (TERIMLER.md)")
        print("  [Q] Shutdown System (Exit)")
        print("\n" + "=" * 60)
        
        choice = input("\n[INPUT] Select terminal command: ").strip().lower()
        
        if choice == '1':
            run_script("vleo_drag_calculator.py")
        elif choice == '2':
            run_script("atox_corrosion_model.py")
        elif choice == '3':
            run_script("fuel_budget_calculator.py")
        elif choice == '4':
            print("\n[SYSTEM] Loading TERIMLER.md...")
            if os.name == 'nt':
                os.system('type TERIMLER.md')
            else:
                os.system('cat TERIMLER.md')
            input("\n[SYSTEM] Press Enter to return...")
        elif choice == 'q':
            print("\n[SYSTEM] Shutting down. Fly safe, engineer.")
            break
        else:
            print("\n[ERROR] Unknown command. Please try again.")
            import time
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
