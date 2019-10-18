

# import the necessary packages
from pyimagesearch import config
from imutils import paths
import random
import shutil
import os
 
# grab the paths to all input images in the original input directory
# and shuffle them
imagePaths = list(paths.list_images(config.ORIG_INPUT_DATASET))
random.seed(42)
random.shuffle(imagePaths)