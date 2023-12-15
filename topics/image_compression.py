import cv2
import numpy as np
import pywt  # PyWavelets
import pickle  # For simple file saving/loading

# Subband Decomposition using Wavelets
def subband_decomposition(image, wavelet='haar'):
    coeffs = pywt.dwt2(image, wavelet)
    cA, (cH, cV, cD) = coeffs
    return coeffs

# Scalar Quantization
def scalar_quantization(coeffs, step_size):
    cA, (cH, cV, cD) = coeffs
    q_cA = np.round(cA / step_size) * step_size
    q_cH = np.round(cH / step_size) * step_size
    q_cV = np.round(cV / step_size) * step_size
    q_cD = np.round(cD / step_size) * step_size
    return q_cA.astype(np.float32), (q_cH.astype(np.float32), q_cV.astype(np.float32), q_cD.astype(np.float32))

# Entropy Encoding - Placeholder
def entropy_encode(image):
    # Implement or use a library for Huffman coding
    return image

# Entropy Decoding - Placeholder
def entropy_decode(encoded_data):
    # Inverse of entropy encoding
    return encoded_data

# Subband Reconstruction
def subband_reconstruction(coeffs, wavelet='haar'):
    # Ensure that the coefficients are correctly formatted
    cA, (cH, cV, cD) = coeffs
    return pywt.idwt2((cA, (cH, cV, cD)), wavelet)


# PSNR Calculation
def calculate_psnr(original, reconstructed):
    mse = np.mean((original - reconstructed) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def main(image):
  # convert image to black and white
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  quantization_step = int(input("Enter the quantization step (i.e. 10): "))
  
  # Perform subband decomposition
  coeffs = subband_decomposition(image)
  
  # Perform scalar quantization on each subband
  quantized_coeffs = scalar_quantization(coeffs, quantization_step)
  
  # Placeholder for entropy encoding
  encoded = entropy_encode(quantized_coeffs)

  # Save to file (simple approach)
  with open('encoded_image.dat', 'wb') as file:
    pickle.dump(encoded, file)
    
  # Read from file
  with open('encoded_image.dat', 'rb') as file:
    encoded_data = pickle.load(file)
  
  # Placeholder for entropy decoding
  decoded = entropy_decode(encoded_data)
  
  # Perform subband reconstruction
  reconstructed = subband_reconstruction(decoded)
  
  # Calculate PSNR between original and reconstructed image
  psnr = calculate_psnr(image, reconstructed)
  print(f"PSNR: {psnr} dB")
  
  # return the reconstructed image
  return reconstructed
