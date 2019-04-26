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

| Model | Class | URL | Example |
|:-------|-------|-----|-----|
| Raspberry Pi Camera V2 | [IMX219](jetcam/imx219.py#L9) | [Amazon](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?keywords=raspberry+pi+v2+camera&qid=1554831689&s=electronics&sr=1-3) | [Notebook](notebooks/imx219/imx219.ipynb) |
| Raspberry Pi Camera V2 (NOIR) | [IMX219](jetcam/imx219.py#L9) | [Amazon](https://www.amazon.com/RPi-Camera-V2-Official-Raspberry/dp/B07P7GBJTK/ref=sr_1_1_sspa?keywords=raspberry+pi+v2+camera&qid=1554831658&s=electronics&sr=1-1-spons&psc=1) | [Notebook](notebooks/imx219/imx219.ipynb) |
| Arducam IMX219 CS lens mount | [IMX219](jetcam/imx219.py#L9) | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-cs-lens-2718-raspberry-pi.html?gclid=EAIaIQobChMIzMKg38bD4QIVrR6tBh3UoAdjEAYYCSABEgLg-_D_BwE) | [Notebook](notebooks/imx219/imx219.ipynb) |
| Arducam IMX219 M12 lens mount | [IMX219](jetcam/imx219.py#L9) | [RobotShop](https://www.robotshop.com/en/arducam-8mp-sony-imx219-camera-module-m12-lens-ls40136-raspberry-pi.html) | [Notebook](notebooks/imx219/imx219.ipynb) |
| LI-IMX219-MIPI-AF-NANO | [IMX219](jetcam/imx219.py#L9) | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-af-nano/) | [Notebook](notebooks/imx219/imx219.ipynb) |
| LI-IMX219-MIPI-FF-NANO | [IMX219](jetcam/imx219.py#L9) | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-ff-nano/) | [Notebook](notebooks/imx219/imx219.ipynb) |
