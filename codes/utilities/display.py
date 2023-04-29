import cv2


class Display:
    def display_results(overlay, original_image, matched_pixels_start, block_size):
        alpha = 0.5
        orig = original_image.copy()

        for starting_points in matched_pixels_start:
            p1 = starting_points[0]
            p2 = starting_points[1]

            overlay[p1[0] : p1[0] + block_size, p1[1] : p1[1] + block_size] = (0, 0, 255)
            overlay[p2[0] : p2[0] + block_size, p2[1] : p2[1] + block_size] = (0, 255, 0)

        cv2.addWeighted(overlay, alpha, original_image, 1, 0, original_image)

        cv2.imshow("Original Image", orig)
        cv2.imshow("Detected Forged/Duplicated Regions", original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
