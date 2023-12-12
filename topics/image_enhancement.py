# Core file for image enhancement

import cv2
import numpy as np

def adjust_brightness(image, alpha):
    # Ensure alpha is within a reasonable range
    alpha = max(0, min(alpha, 5.0))
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def adjust_contrast(image, alpha):
    # Clamp the contrast factor to a reasonable range
    alpha = max(1, min(alpha, 5.0))
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def add_gaussian_noise(image, mean=0, sigma=25):
    gauss = np.random.normal(mean, sigma, image.shape).astype('uint8')
    noisy_image = cv2.add(image, gauss)
    return noisy_image

def add_speckle_noise(image):
    speckle = np.random.randn(*image.shape) * 255
    noisy_image = image + speckle
    return noisy_image.astype('uint8')

def apply_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

def sharpen_image(image):
    kernel = np.array([
      [-1, -1, -1],          
      [-1,  9, -1],
      [-1, -1, -1]
    ])
    return cv2.filter2D(image, -1, kernel)

def main(image):
    # Apply the image enhancement techniques
    selected_option = input("Which enhancement technique would you like to apply?\n1. Brightness\n2. Contrast\n3. Gaussian Noise\n4. Speckle Noise\n5. Blur\n6. Sharpen\nEnter the number of your choice (1-6): ")
    if selected_option == '1':
      input_alpha = input("Enter the brightness factor (0-5): ")
      alpha = float(input_alpha)
      image = adjust_brightness(image, alpha)
    elif selected_option == '2':
      input_alpha = input("Enter the contrast factor (1-5): ")
      alpha = float(input_alpha)
      image = adjust_contrast(image, alpha)
    elif selected_option == '3':
      image = add_gaussian_noise(image)
    elif selected_option == '4':
      image = add_speckle_noise(image)
    elif selected_option == '5':
      image = apply_blur(image)
    elif selected_option == '6':
      image = sharpen_image(image)
    else:
      print("Invalid option selected. Aborting...")
      return image
    
    return image

if __name__ == "__main__":
    main()
