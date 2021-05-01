
from qasync import QEventLoop, QThreadExecutor
from napari_arnheim.widgets import ArnheimWidget
from bergen import Bergen
import napari
import asyncio
import sys
from skimage import data

with napari.gui_qt() as app:
    #viewer = napari.view_image(data.astronaut(), rgb=True)
    viewer = napari.Viewer()
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    arnheim = ArnheimWidget()
    viewer.window.add_dock_widget(arnheim, area="right")

    with loop:
        loop.run_until_complete(arnheim.connectBergen())


        viewer.add_image(data.astronaut(), rgb=True)
        sys.exit(loop.run_forever())