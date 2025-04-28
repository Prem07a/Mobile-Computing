# CDMA Simulation Using Walsh Codes

This project simulates a simple CDMA (Code Division Multiple Access) communication system using Walsh codes for orthogonal spreading. The simulation shows how different users can transmit and decode signals even in the presence of noise.

## Overview

- **Walsh Matrix Generation**: A recursive function generates a \(2^n \times 2^n\) Walsh matrix.
- **Message Transmission**: A set of bits is spread using a specific Walsh code (chip sequence) assigned to a user.
- **Noise Addition**: Gaussian noise is added to the transmitted signal to simulate a noisy channel.
- **Reception and Decoding**: Each user attempts to decode the transmitted signal by correlating with their respective Walsh code.
- **Performance Metrics**: Signal-to-Noise Ratio (SNR), signal power, and noise power are calculated for each user.

## Files

- `simulate_cdma.py` - Contains the simulation code.
- `README.md` - This documentation.

## How It Works

1. **Walsh Matrix Generation**  
   A \(2^n \times 2^n\) Walsh matrix is generated using recursion.

2. **Transmission**  
   - A message of 4 bits (`[1, -1, 1, -1]`) is transmitted using the Walsh code for user 4.
   - Each bit is spread by multiplying with the selected Walsh code.

3. **Noise Addition**  
   Gaussian noise (mean = 0, standard deviation = 0.5) is added to simulate a real-world channel.

4. **Reception**  
   Each user tries to decode the received noisy signal by correlating it with their own Walsh code.

5. **Performance Evaluation**  
   For each user:
   - **Decoded Bits** are printed.
   - Comparison with the original message bits is shown.
   - **SNR (Signal-to-Noise Ratio)** is calculated and displayed.
   - Average **Signal Power** and **Noise Power** are printed.

## Code Example

```python
def walshmatrix(n):
    if n == 1:
        return np.array([[1, 1], [1, -1]])
    else:
        W = walshmatrix(n - 1)
        return np.vstack((np.hstack((W, W)), np.hstack((W, -W))))
```

```python
def simulate_cdma():
    wm = walshmatrix(np.log2(num))
    ...
    received_signal = transmitted_data + noise  
    ...
```

## Requirements

- Python 3.x
- numpy

You can install the required package with:

```bash
pip install numpy
```

## Running the Simulation

Simply run the Python script:

```bash
python simulate_cdma.py
```

It will output decoded results, success status, SNR, noise power, and signal power for each user.

## Notes

- In this example, 8 Walsh codes are generated.
- Only user 4 is actively transmitting; all other users attempt to decode based on their codes.
- SNR calculation uses the formula:  
  \[
  \text{SNR (dB)} = 10 \times \log_{10}\left(\frac{\text{Signal Power}}{\text{Noise Power}}\right)
  \]

## License

This project is provided for educational purposes.

