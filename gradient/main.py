import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")

color1 = [255, 128, 0]  
color2 = [0, 128, 255]  

for y in range(size):
    for x in range(size):
        t = (x + y) / (2 * (size - 1))
        r = lerp(color1[0], color2[0], t)
        g = lerp(color1[1], color2[1], t)
        b = lerp(color1[2], color2[2], t)
        image[y, x, :] = [r, g, b]

plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.axis("off")
plt.show()
