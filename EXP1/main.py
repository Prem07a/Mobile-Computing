import numpy as np

def walshmatrix(n): 
    "2^n x 2^n" 
    if n == 1:
        return np.array([[1,1],[1,-1]])
    else:
        W = walshmatrix(n-1)
        return np.vstack((np.hstack((W, W)), np.hstack((W,-W))))
num = 8 

def simulate_cdma():
    wm = walshmatrix(np.log2(num))

    in_ = 4 

    message_bits = np.array([1,-1,1,-1])

    transmitted_data = []

    for bit in message_bits:
        transmitted_data.append(bit*wm[in_])
    transmitted_data = np.array(transmitted_data)
    # print(transmitted_data)
    
    noise = np.random.normal(0, 0.5, transmitted_data.shape)

    received_signal = transmitted_data + noise  
    print(received_signal)
    for user in range(num):
        print("User",user)
        decoded_bit = []
        noise_arr = []
        signal_arr = []
        snr_arr = []
        for bits in received_signal:
            corr = np.dot( bits , wm[user])/ len(wm[user])

            signal_power = corr**2 
            # recived - recontracted signal
            noise = np.var(bits - corr*wm[user])
            bit_d = 1 if corr > 0 else -1
            snr = float("inf") if noise == 0 else 10*np.log10(signal_power/noise)
            snr_arr.append(snr)
            noise_arr.append(noise)
            signal_arr.append(signal_power)
            decoded_bit.append(bit_d)

        print("Decoded:",decoded_bit)
        print("Transmitted:",message_bits)
        print("Success?", (decoded_bit==message_bits).all())
        print("SNR(DB): ", np.mean(snr))
        print("Noise:", np.mean(noise_arr))
        print("SignalPow:", np.mean(signal_arr))
        print("="*60)


simulate_cdma()