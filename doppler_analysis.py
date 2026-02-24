import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Constants
# ==============================

c = 3e8                 # Speed of light (m/s)
frequency = 12e9        # 12 GHz
sat_velocity = 7500     # LEO satellite velocity (m/s)

# Time array
time = np.linspace(-300, 300, 500)

# Elevation model
elevation = 90 * np.exp(-(time / 200)**2)
elevation_rad = np.radians(elevation)

# Relative velocity
relative_velocity = sat_velocity * np.cos(elevation_rad)

# Doppler shift
doppler_shift = (relative_velocity / c) * frequency


# ==============================
# GRAPH 1
# ==============================

plt.figure()
plt.plot(time, doppler_shift)
plt.title("Doppler Shift vs Time (LEO Satellite)")
plt.xlabel("Time (seconds)")
plt.ylabel("Doppler Shift (Hz)")
plt.grid(True)
plt.savefig("doppler_shift_vs_time.png", dpi=300)
plt.show()


# ==============================
# GRAPH 2
# ==============================

plt.figure()
plt.plot(time, relative_velocity)
plt.title("Relative Velocity vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.savefig("relative_velocity_vs_time.png", dpi=300)
plt.show()


# ==============================
# GRAPH 3
# ==============================

plt.figure()
plt.plot(elevation, doppler_shift)
plt.title("Doppler Shift vs Elevation Angle")
plt.xlabel("Elevation Angle (degrees)")
plt.ylabel("Doppler Shift (Hz)")
plt.grid(True)
plt.savefig("doppler_vs_elevation.png", dpi=300)
plt.show()


print("✅ All 3 graphs generated successfully!")
