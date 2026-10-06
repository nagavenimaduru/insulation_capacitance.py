print("====================================")
print("   INSULATION CAPACITANCE CALCULATOR")
print("====================================")

epsilon_r = float(input("Enter relative permittivity: "))
area = float(input("Enter insulation area (m²): "))
thickness = float(input("Enter insulation thickness (m): "))

# Permittivity of free space
epsilon_0 = 8.854e-12

if epsilon_r <= 0 or area <= 0 or thickness <= 0:
    print("\nPlease enter positive values.")
else:
    capacitance = (epsilon_0 * epsilon_r * area) / thickness

    capacitance_pf = capacitance * 1e12

    print("\n------------- RESULTS -------------")
    print(f"Relative Permittivity : {epsilon_r:.2f}")
    print(f"Area                  : {area:.4f} m²")
    print(f"Thickness             : {thickness:.6f} m")
    print(f"Capacitance           : {capacitance:.6e} F")
    print(f"Capacitance           : {capacitance_pf:.4f} pF")
    print("-----------------------------------")
