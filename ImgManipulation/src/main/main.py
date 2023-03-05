import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Image
img = mpimg.imread('ImgManipulation\src\img\example.jpg')

# Splitting the image into 20 pieces
img_pieces = np.split(img, 20, axis=1)

# Combine of two splitted images
combined_img1 = np.concatenate(img_pieces[0::2], axis=1)
combined_img2 = np.concatenate(img_pieces[1::2], axis=1)
combined_img = np.concatenate((combined_img1, combined_img2), axis=1)

# Rotate the combined image by 90 degrees
rotated_img = np.rot90(combined_img)

# Split the rotated image into 20 pieces
rotated_img_pieces = np.split(rotated_img, 20, axis=1)

# Combine two images next to each other
rotated_combined_img1 = np.concatenate(rotated_img_pieces[0::2], axis=1)
rotated_combined_img2 = np.concatenate(rotated_img_pieces[1::2], axis=1)
rotated_combined_img = np.concatenate((rotated_combined_img1, rotated_combined_img2), axis=1)

# Rotate 3 times the image to see it properly
rotated_img2 = np.rot90(rotated_combined_img, 3)

# Split view into 2 sides to see original img and expected final image
fig, axs = plt.subplots(1, 2)
axs[0].imshow(img)
axs[0].set_title('Original Image')
axs[1].imshow(rotated_img2)
axs[1].set_title('Double-Rotated Image')
plt.show()