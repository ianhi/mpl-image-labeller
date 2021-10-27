from mpl_image_labeller import image_labeller
import numpy as np
import matplotlib.pyplot as plt


images = np.random.randn(5, 10, 10)
labeller = image_labeller(
    images, classes=["good", "bad", "meh"], label_keymap=["a", "s", "d"]
)
plt.show()
print(labeller.labels)
