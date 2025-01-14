# Image Upscaling with OpenCV's Super-Resolution

This project demonstrates how to upscale images using OpenCV's Super-Resolution module with pre-trained EDSR and LapSRN models.

## Features

- Upscales images by a factor of 4 using the EDSR model.
- Upscales images by a factor of 8 using the LapSRN model.
- Displays the original and upscaled images side-by-side for comparison.

## Requirements

- Python 3.x
- OpenCV (with contrib module)
- Matplotlib

3. The upscaled images will be saved as `upscaled_x4.png` and `upscaled_x8.png` in the project directory.


## Colab Notebook

You can also run this project in Google Colab:

1. Create a new Colab notebook.
2. Copy and paste the code above into a code cell.
3. Upload your image file to the Colab environment.
4. Run the code cell.
5. The upscaled images will be saved in the Colab environment. You can download them from the "Files" tab.

## Example

The `Picture2.png` image is provided as an example. You can replace it with your own image to test the upscaling.

## Acknowledgements

- OpenCV: https://opencv.org/
- EDSR: https://github.com/Saafke/EDSR_Tensorflow/blob/master/models/ <br/>
- LapSRN: https://github.com/fannymonori/TF-LapSRN/blob/master/export/LapSRN_x8.pb

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
