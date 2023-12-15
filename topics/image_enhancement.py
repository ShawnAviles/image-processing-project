# Image Enhancement functions

import cv2
import numpy as np

def adjust_brightness(image, alpha):
    # Using OpenCV's convertScaleAbs function
    # Ensure alpha is within a reasonable range
    # alpha = max(0, min(alpha, 5.0))
    # return cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    
    # Custom implementation
    height, width = image.shape[:2]
    bright_image = np.zeros_like(image)
    for j in range(height):
        for k in range(width):
            bright_image[j, k] = np.clip(image[j, k] * alpha, 0, 255)
    return bright_image

def adjust_contrast(image, alpha):
    # Using OpenCV's convertScaleAbs function
    # Clamp the contrast factor to a reasonable range
    # alpha = max(1, min(alpha, 5.0))
    # return cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    
    # Custom implementation
    mean = np.mean(image)
    height, width = image.shape[:2]
    contrast_image = np.zeros_like(image)
    for j in range(height):
        for k in range(width):
            contrast_image[j, k] = np.clip((image[j, k] - mean) * alpha + mean, 0, 255)
    return contrast_image

def add_gaussian_noise(image, mean=0, sigma=25):
    # Using OpenCV's randn function
    # gauss = np.random.normal(mean, sigma, image.shape).astype('uint8')
    # noisy_image = cv2.add(image, gauss)
    # return noisy_image

    # Custom implementation
    height, width = image.shape[:2]
    noisy_image = np.zeros_like(image)
    for j in range(height):
        for k in range(width):
            gaussian_noise = np.random.normal(mean, sigma, 3)
            noisy_image[j, k] = np.clip(image[j, k] + gaussian_noise, 0, 255)
    return noisy_image.astype(np.uint8)

def add_speckle_noise(image):
    # Using OpenCV's randn function
    # speckle = np.random.randn(*image.shape) * 255
    # noisy_image = image + speckle
    # return noisy_image.astype('uint8')
    
    # Custom implementation
    height, width = image.shape[:2]
    speckle_image = np.zeros_like(image)
    for j in range(height):
        for k in range(width):
            speckle_noise = np.random.randn(3)
            speckle_image[j, k] = np.clip(image[j, k] + image[j, k] * speckle_noise, 0, 255)
    return speckle_image.astype(np.uint8)

def apply_blur(image, kernel_values = 3):
    # Using OpenCV's GaussianBlur function
    # return cv2.GaussianBlur(image, kernel_size=(5,5), 0)
    
    # Custom implementation
    kernel_values = max(3, min(kernel_values, 20))
    kernel_size = (kernel_values, kernel_values)
    height, width = image.shape[:2]
    blurred_image = np.zeros_like(image)
    k_height, k_width = kernel_size

    # Padding for the border pixels
    padded_image = cv2.copyMakeBorder(image, k_height // 2, k_height // 2, k_width // 2, k_width // 2, cv2.BORDER_REPLICATE)

    for j in range(height):
        for k in range(width):
            # Apply a simple average blur
            blurred_image[j, k] = np.mean(padded_image[j:j+k_height, k:k+k_width], axis=(0, 1))

    return blurred_image.astype(np.uint8)

def sharpen_image(image):
    kernel = np.array([
      [-1, -1, -1],          
      [-1,  9, -1],
      [-1, -1, -1]
    ])
    
    # Using OpenCV's filter2D function
    # return cv2.filter2D(image, -1, kernel)
    
    # Custom implementation
    height, width = image.shape[:2]
    sharpened_image = np.zeros_like(image)

    # Handle padding to avoid border issues
    padded_image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_REPLICATE)

    # Apply the kernel to each pixel
    for j in range(1, height + 1):
        for k in range(1, width + 1):
            # Applying the kernel on each pixel, considering all color channels
            red_channel = np.sum(kernel * padded_image[j-1:j+2, k-1:k+2, 0])
            green_channel = np.sum(kernel * padded_image[j-1:j+2, k-1:k+2, 1])
            blue_channel = np.sum(kernel * padded_image[j-1:j+2, k-1:k+2, 2])

            # Keeping values within 0-255 range
            sharpened_pixel = [np.clip(red_channel, 0, 255),
                               np.clip(green_channel, 0, 255),
                               np.clip(blue_channel, 0, 255)]

            sharpened_image[j-1, k-1] = sharpened_pixel
    
    return sharpened_image.astype(np.uint8)

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
      kernel_values = input("Enter the blur factor (3,20): ")
      image = apply_blur(image, int(kernel_values))
    elif selected_option == '6':
      image = sharpen_image(image)
    else:
      print("Invalid option selected. Aborting...")
      return image
    
    return image
