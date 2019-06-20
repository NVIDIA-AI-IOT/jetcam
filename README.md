# JetCam

JetCam is an easy to use camera interface for NVIDIA Jetson.

### Setup

1. Flash your Jetson Nano using the [JetCard](https://github.com/NVIDIA-AI-IOT-private/jetcard) SD card image

2. Install the JetCam python package

    ```bash
    git clone https://github.com/NVIDIA-AI-IOT-private/jetcam.git
    cd jetcam
    sudo python3 setup.py install
    ```

### Usage

#### Create CSI camera

Call ``CSICamera`` to use a compatible CSI camera.  ``capture_width``, ``capture_height``, and ``capture_fps`` will control the capture shape and rate that images are aquired.  ``width`` and ``height`` control the final output shape of the image as returned by the ``read`` function.

```python
from jetcam.csi_camera import CSICamera

camera = CSICamera(width=224, height=224, capture_width=1080, capture_height=720, capture_fps=30)
```

#### Create USB camera

Call ``USBCamera`` to use a compatbile USB camera.  The same parameters as ``CSICamera`` apply, along with a parameter ``capture_device`` that indicates the device index.  You can check the device index by calling ``ls /dev/video*``.

```python
from jetcam.usb_camera import USBCamera

camera = USBCamera(capture_device=1)
```

#### Read

Call ``read()`` to read the latest image as a ``numpy.ndarray`` of data type ``np.uint8`` and shape ``(224, 224, 3)``.  The color format is ``BGR8``.

```python
image = camera.read()
```

The ``read`` function also updates the camera's internal ``value`` attribute.

```python
camera.read()
image = camera.value
```

#### Callback

You can also set the camera to ``running = True``, which will spawn a thread that acquires images from the camera.  These will update the camera's ``value`` attribute automatically.  You can attach a callback to the value using the [traitlets](https://traitlets.readthedocs.io/en/stable/api.html#callbacks-when-trait-attributes-change) library.  This will call the callback with the new camera value as well as the old camera value

```python
camera.running = True

def callback(change):
    new_image = change['new']
    # do some processing...

camera.observe(callback, names='value')
```

### Cameras

#### CSI Cameras

These cameras work with the [``CSICamera``](jetcam/csi_camera.py) class.  Try them out by following the example [notebook](notebooks/csi_camera/csi_camera.ipynb).

| Model | URL |
|:-------|-------|
| Raspberry Pi Camera V2 | [Amazon](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?keywords=raspberry+pi+v2+camera&qid=1554831689&s=electronics&sr=1-3) | 
| Raspberry Pi Camera V2 (NOIR) | [Amazon](https://www.amazon.com/RPi-Camera-V2-Official-Raspberry/dp/B07P7GBJTK/ref=sr_1_1_sspa?keywords=raspberry+pi+v2+camera&qid=1554831658&s=electronics&sr=1-1-spons&psc=1) | 
| Arducam IMX219 CS lens mount | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-cs-lens-2718-raspberry-pi.html?gclid=EAIaIQobChMIzMKg38bD4QIVrR6tBh3UoAdjEAYYCSABEgLg-_D_BwE) | 
| Arducam IMX219 M12 lens mount | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-m12-lens-ls40136-raspberry-pi.html) |
| LI-IMX219-MIPI-AF-NANO | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-af-nano/) | 
| LI-IMX219-MIPI-FF-NANO | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-ff-nano/) |

#### USB Cameras

These cameras work with the [``USBCamera``](jetcam/usb_camera.py) class.  Try them out by following the example [notebook](notebooks/usb_camera/usb_camera.ipynb).

| Model | URL |
|:-------|-------|
| Logitech C270 | [Amazon](https://www.amazon.com/Logitech-Widescreen-designed-Calling-Recording/dp/B004FHO5Y6) | 
