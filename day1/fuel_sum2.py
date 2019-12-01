import numpy as np


def calculate_fuel(mass):
    """Divide mass by three, round down and subtract 2
    """
    return int(mass / 3) - 2


def load_masses(path="input.dat"):
    return np.loadtxt(path)


def main():
    """Load in the masses, calculate their fuel and sum
    """
    masses = load_masses()
    total_fuel = 0

    for mass in masses:
        fuel = calculate_fuel(mass)

        while fuel > 0:
            total_fuel += fuel
            fuel = calculate_fuel(fuel)

    print(total_fuel)


if __name__ == "__main__":
    main()
