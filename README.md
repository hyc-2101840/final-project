# Cataract vs Normal Eye Model

It tells the user if a given eye image has cataract. It starts checking the image when the image is uploaded onto its user interface and the code is activated.

[A normal eye.](https://cdn.britannica.com/79/150179-120-3A8438B1/human-eye.jpg)
[An eye with cataracts.](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Dense_white_mature_cataract.jpg/200px-Dense_white_mature_cataract.jpg)


## The Algorithm

It is trained to recognize normal eyes and eyes with cataracts. It does this by comparing the pixels in the images. To use it, you have to upload an image into it. When it gives out the answer in the form of another image, there will be a percentage and whatever it thinks the image is on the top left corner.

## Running this project

1. Clone this repository.
2. Install flask on to the machine using `sudo apt-get install python3-flask`.
3. Navigate to this directory and run the main.py file using `python3 main.py`.
4. Open a web browser and visit the local web interface provided in your terminal (After running the previous code).
5. Google search an image and then right click and copy the image address.
6. Click classify on the interface.
7. If the output box gives an error, use another image instead because the website doesn't allow the image to be downloaded.

[Video about the project.](https://drive.google.com/file/d/1WkQjOooDcOGRjuq5r4HivJh0zdXdKA8s/view?usp=drive_link)
