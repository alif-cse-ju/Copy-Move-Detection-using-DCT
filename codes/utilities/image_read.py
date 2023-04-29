import cv2
import numpy


class ImageRead:
    def read_image(image_path):
        """
        Returns:
            img (numpy.array)              : original image in the form of numpy array
            original_image (numpy.ndarray) : orignal image
            overlay (numpy.ndarray)        : copy of orignal image
            width (int)                    : width of the image
            height (int)                   : height of the image
        """
        image = image_path
        original_image = cv2.imread(image, cv2.IMREAD_COLOR)
        image = cv2.imread(image, 0)

        overlay = original_image.copy()

        img = numpy.array(image)
        height, width = img.shape

        return img, original_image, overlay, width, height
