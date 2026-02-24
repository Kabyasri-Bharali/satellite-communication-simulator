import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# ============================================
# BER vs SNR Analysis for Satellite Communication
# BPSK Modulation
# ============================================

# SNR range in dB
snr_db = np.linspace(0, 20, 100)

# Convert SNR from dB to linear scale
snr_linear = 10 ** (snr_db / 10)

# BER Calculation for BPSK (Theoretical)
ber = 0.5 * erfc(np.sqrt(snr_linear))

# ============================================
# Plotting
# ============================================

plt.figure(figsize=(8, 6))

plt.semilogy(snr_db, ber, linewidth=2, label="BPSK BER")

plt.title("BER vs SNR Performance (BPSK Modulation)")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid(True, which="both")
plt.legend()

# Save figure
plt.savefig("ber_vs_snr_bpsk.png", dpi=300)

plt.show()
