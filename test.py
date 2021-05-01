
from qasync import QEventLoop, QThreadExecutor
from napari_arnheim.widgets import ArnheimWidget
from bergen import Bergen
import napari
import asyncio

with napari.gui_qt() as app:
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(ArnheimWidget(), area="right")