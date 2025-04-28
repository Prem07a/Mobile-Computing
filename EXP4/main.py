import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

num_bits = 10**6
np.random.seed(100)

bits = np.random.rand(num_bits) > 0.5
bpsk_symbols = 2 * bits - 1

noise = (1 / np.sqrt(2)) * (np.random.randn(num_bits) + 1j * np.random.randn(num_bits))
EbN0_dB_range = np.arange(-3, 41)

num_errors_awgn = np.zeros(len(EbN0_dB_range))
num_errors_rayleigh = np.zeros(len(EbN0_dB_range))

for i, ebn0_db in enumerate(EbN0_dB_range):
    received_awgn = bpsk_symbols + 10 ** (-ebn0_db / 20) * noise
    detected_bits_awgn = np.real(received_awgn) > 0
    num_errors_awgn[i] = np.sum(bits != detected_bits_awgn)

    rayleigh_fading = (1 / np.sqrt(2)) * (np.random.randn(num_bits) + 1j * np.random.randn(num_bits))
    received_rayleigh = rayleigh_fading * bpsk_symbols + 10 ** (-ebn0_db / 20) * noise
    detected_bits_rayleigh = np.real(received_rayleigh / rayleigh_fading) > 0
    num_errors_rayleigh[i] = np.sum(bits != detected_bits_rayleigh)

ber_sim_awgn = num_errors_awgn / num_bits
ber_sim_rayleigh = num_errors_rayleigh / num_bits
ber_theory_awgn = 0.5 * erfc(np.sqrt(10 ** (EbN0_dB_range / 10)))
ber_theory_rayleigh = 0.5 * (1 - np.sqrt(10 ** (EbN0_dB_range / 10) / (1 + 10 ** (EbN0_dB_range / 10))))

plt.semilogy(EbN0_dB_range, ber_theory_awgn, 'b-', label='AWGN-Theory')
plt.semilogy(EbN0_dB_range, ber_sim_awgn, 'mx-', label='AWGN-Simulation')
plt.semilogy(EbN0_dB_range, ber_theory_rayleigh, 'r-.', label='Rayleigh-Theory')
plt.semilogy(EbN0_dB_range, ber_sim_rayleigh, 'go-', label='Rayleigh-Simulation')
plt.axis([-3, 40, 1e-5, 0.5])
plt.grid(True, which='both')
plt.legend()
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Bit Error Rate')
plt.title('BER for BPSK in AWGN and Rayleigh Fading Channels')
plt.show()