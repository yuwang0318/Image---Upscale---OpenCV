import cv2
from cv2 import dnn_superres
import matplotlib.pyplot as plt

# initialize super resolution object
sr = dnn_superres.DnnSuperResImpl_create()

# EDSR_x4 model
# read the model
path = 'EDSR_x4.pb'
sr.readModel(path)

# set the model and scale
sr.setModel('edsr', 4)

# load the image
image = cv2.imread('Picture2.png')

# upsample the image
upscaled_x4 = sr.upsample(image)
# save the upscaled image
cv2.imwrite('upscaled_test.png', upscaled_x4)

# LapSRN model
# read the model
path = 'LapSRN_x8.pb'
sr.readModel(path)
# set the model and scale
sr.setModel('lapsrn', 8)

# upsample the image
upscaled_x8 = sr.upsample(image)
# save the upscaled image
cv2.imwrite('upscaled_test_lapsrn.png', upscaled_x8)

#show the images side by side
# Create a figure with two subplots
fig, axes = plt.subplots(1, 3)

# Display the images in the subplots
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title("Before")
axes[1].imshow(cv2.cvtColor(upscaled_x4, cv2.COLOR_BGR2RGB))
axes[1].set_title("x4")
axes[2].imshow(cv2.cvtColor(upscaled_x8, cv2.COLOR_BGR2RGB))
axes[2].set_title("x8")

# Show the figure
plt.show()