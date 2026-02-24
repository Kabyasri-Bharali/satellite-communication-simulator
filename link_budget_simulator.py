import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Constants
# ==============================

c = 3e8
k = 1.38e-23

frequency = 12e9
wavelength = c / frequency

tx_power_dbw = 20
tx_gain_db = 35
rx_gain_db = 35

system_temp = 500
bandwidth = 36e6

# ==============================
# Distance ranges
# ==============================

leo_distance = np.linspace(500e3, 2000e3, 100)
geo_distance = np.linspace(35786e3, 40000e3, 100)

# ==============================
# Functions
# ==============================

def free_space_loss(d):
    return 20 * np.log10(4 * np.pi * d / wavelength)

def received_power(d):
    return tx_power_dbw + tx_gain_db + rx_gain_db - free_space_loss(d)

def snr_calc(pr_db):
    noise = 10 * np.log10(k * system_temp * bandwidth)
    return pr_db - noise

# Rain attenuation model (simple)
def rain_loss(d, rain_rate=5):
    return rain_rate * (d / 1e6)

# ==============================
# Calculations
# ==============================

leo_pr = received_power(leo_distance)
geo_pr = received_power(geo_distance)

leo_snr = snr_calc(leo_pr)
geo_snr = snr_calc(geo_pr)

# Rain effect
leo_snr_rain = leo_snr - rain_loss(leo_distance)
geo_snr_rain = geo_snr - rain_loss(geo_distance)

# ==============================
# BER Calculation (BPSK)
# ==============================

snr_linear = 10**(leo_snr / 10)
ber = 0.5 * np.exp(-snr_linear)

# ==============================
# Plot 1 — SNR Comparison
# ==============================

plt.figure(figsize=(8,5))

plt.plot(leo_distance/1000, leo_snr, label="LEO Clear Sky")
plt.plot(geo_distance/1000, geo_snr, label="GEO Clear Sky")

plt.plot(leo_distance/1000, leo_snr_rain, '--', label="LEO Rain")
plt.plot(geo_distance/1000, geo_snr_rain, '--', label="GEO Rain")

plt.xlabel("Distance (km)")
plt.ylabel("SNR (dB)")
plt.title("Satellite Link SNR Comparison")
plt.legend()
plt.grid()

plt.savefig("snr_advanced.png", dpi=300)
plt.show()

# ==============================
# Plot 2 — BER Curve
# ==============================

plt.figure(figsize=(8,5))

plt.semilogy(leo_snr, ber)

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR (BPSK Modulation)")
plt.grid()

plt.savefig("ber_curve.png", dpi=300)
plt.show()
