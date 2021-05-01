from napari_arnheim.widgets import ArnheimWidget
from bergen import Bergen
import napari
import numpy as np


x = np.zeros((1024,1024,30,1))




with napari.gui_qt():
    napari.view_image(x, rgb=True)
    