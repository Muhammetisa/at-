
import random
import numpy as np
import matplotlib.pyplot as plt

def calculate_projectile_shot(target_position, initial_speed, target_width):
    gravity = 10
    angle = np.radians(30)
    
    def shoot(target_position, V0):
        nonlocal gravity, angle
        t_launch = V0 * np.sin(angle) / gravity
        t_flight = 2 * V0 * np.sin(angle) / gravity
        t_land = t_launch

        x_range = V0 * np.cos(angle) * t_flight
        max_height = (V0 ** 2) * (np.sin(angle) ** 2) / (2 * gravity)
        target_distance = target_position - 0.5 * target_width
        target_range = [target_distance, target_distance + target_width]

        if x_range < target_range[0]:
            return "Short"
        elif x_range > target_range[1]:
            return "Long"
        else:
            return "On Target"

    shot_count = 0
    hit_target = False
    while not hit_target:
        shot_count += 1
        status = shoot(target_position, initial_speed)
        if status == "Short":
            initial_speed = (initial_speed + 330) / 2  # Update speed (using lower bound)
        elif status == "Long":
            initial_speed = (initial_speed + 1800) / 2  # Update speed (using upper bound)
        else:
            hit_target = True

    return shot_count, initial_speed

# Randomize target position, width, and initial speed
target_distance = 20000 + 200 * random.randint(-10, 10)
target_width = 1000 + 100 * random.randint(-2, 2)
target_position = target_distance + random.randint(0, 99)  # Random target position
initial_speed = (330 + 1800) / 2  # Initial speed

# Calculate the number of shots and the final speed required to hit the target
shot_count, final_speed = calculate_projectile_shot(target_position, initial_speed, target_width)

# Print the results
print("Number of sh")
# Plot the target and shot coordinates
plt.plot(target_position, 0, 'ro', label='Target')
for i in range(shot_count):
    plt.plot(target_position + random.uniform(-target_width/2, target_width/2), 0, 'bo', label='Shot')
    plt.xlabel('Distance (meter)')
    plt.ylabel('Height (meter)')
    plt.title('Projectile Shot - Target and Shot Coordinates')
    plt.grid(True)

    plt.legend()
    plt.show()
print("test")



