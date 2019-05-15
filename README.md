# JetCam

JetCam is an easy to use camera interface for NVIDIA Jetson.

## Setup

1. Flash your Jetson Nano using the [JetCard](https://github.com/NVIDIA-AI-IOT-private/jetcard) SD card image

2. Install the JetCam python package

    ```bash
    git clone https://github.com/NVIDIA-AI-IOT-private/jetcam.git
    cd jetcam
    sudo python3 setup.py install
    ```

## Cameras

### CSI Cameras

These cameras work with the [``CSICamera``](jetcam/csi_camera.py) class.  Try them out by following the example [notebook](notebooks/csi_camera/csi_camera.ipynb).

| Model | URL |
|:-------|-------|
| Raspberry Pi Camera V2 | [Amazon](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?keywords=raspberry+pi+v2+camera&qid=1554831689&s=electronics&sr=1-3) | 
| Raspberry Pi Camera V2 (NOIR) | [Amazon](https://www.amazon.com/RPi-Camera-V2-Official-Raspberry/dp/B07P7GBJTK/ref=sr_1_1_sspa?keywords=raspberry+pi+v2+camera&qid=1554831658&s=electronics&sr=1-1-spons&psc=1) | 
| Arducam IMX219 CS lens mount | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-cs-lens-2718-raspberry-pi.html?gclid=EAIaIQobChMIzMKg38bD4QIVrR6tBh3UoAdjEAYYCSABEgLg-_D_BwE) | 
| Arducam IMX219 M12 lens mount | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-m12-lens-ls40136-raspberry-pi.html) |
| LI-IMX219-MIPI-AF-NANO | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-af-nano/) | 
| LI-IMX219-MIPI-FF-NANO | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-ff-nano/) |

### USB Cameras

These cameras work with the [``USBCamera``](jetcam/usb_camera.py) class.  Try them out by following the example [notebook](notebooks/usb_camera/usb_camera.ipynb).

| Model | URL |
|:-------|-------|
| Logitech C270 WEBCAM | [Amazon](https://www.amazon.com/Logitech-Widescreen-designed-Calling-Recording/dp/B004FHO5Y6) | 
