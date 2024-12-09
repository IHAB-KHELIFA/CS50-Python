# Define the speed of light constant in meters per second
SPEED_OF_LIGHT = 300000000

# Prompt the user for mass as an integer (in kilograms)
mass = int(input("Enter mass in kilograms: "))

# Calculate the energy using the formula E = mc^2
energy = mass * (SPEED_OF_LIGHT ** 2)

# Output the energy in Joules as an integer
print(energy)
