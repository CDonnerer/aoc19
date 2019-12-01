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
    fuel_sum = np.sum([calculate_fuel(mass) for mass in masses])
    print(fuel_sum)


if __name__ == "__main__":
    main()
