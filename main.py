from napari_arnheim.widgets.dialogs.upload import createDataArrayFromLayer
from grunnlag.schema import Representation, RepresentationVariety
import napari_arnheim
from napari_arnheim.dialogs.upload import UploadFileDialog
from dask_image import ndfilters
from skimage import data
from bergen.console import console
from bergen.models import Node
import xarray as xr


with napari_arnheim.gui_qt() as interface:

    interface.viewer.add_image(data.astronaut(), rgb=True)


    @interface.client.template(Node.objects.get(package="Elements", interface="show"), kabums=False)
    async def show(rep: Representation) -> Representation:
        try:
            interface.helper.openRepresentationAsLayer(rep=rep)
        except:
            console.print_exception()
        return rep

    @interface.client.template(Node.objects.get(package="Elements", interface="gaussian_blur"), kabums=False)
    async def gaussian_filter(rep: Representation, sigma: int = 4) -> Representation:
        out = ndfilters.gaussian_filter(rep.data.data, 0.4)
        filtered = xr.DataArray(out, dims=rep.data.dims)
        return await Representation.asyncs.from_xarray(filtered, name=rep.name + "blured", sample=rep.sample.id, tags=[], variety=RepresentationVariety.VOXEL)


    @interface.client.template(Node.objects.get(package="Elements", interface="upload"), test=True)
    async def upload() -> Representation:
        layer = interface.viewer.active_layer
        dialog = UploadFileDialog(layer=layer)
        if dialog.exec_():
            name = dialog.name
            newarray = createDataArrayFromLayer(layer=layer)
            return await Representation.asyncs.from_xarray(newarray, name=name, sample=2, tags=[], variety=RepresentationVariety.VOXEL)



    interface.client.provide()