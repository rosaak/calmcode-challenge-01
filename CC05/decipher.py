from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("ghost.png")

plt.imshow(image)
plt.axis('off')
plt.show()

channels = image.split()

# Set up subplots
fig, axes = plt.subplots(1, len(channels), figsize=(20, 10))

# Titles for channels
channel_titles = ["Red", "Green", "Blue"]
if len(channels) == 4:
    channel_titles.append("Alpha")

# Display each channel
for ax, channel, title in zip(axes, channels, channel_titles):
    ax.imshow(channel, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
