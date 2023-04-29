import numpy


class QuantizationMatrix:
    # Quantization Matrix for 50%
    quantization_matrix50 = numpy.array(
        [
            [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99],
        ]
    )

    # Quantization Matrix for 75%
    quantization_matrix75 = numpy.array(
        [
            [8, 6, 5, 8, 12, 20, 26, 31],
            [6, 6, 7, 10, 13, 29, 30, 28],
            [7, 7, 8, 12, 20, 29, 35, 28],
            [7, 9, 11, 15, 26, 44, 40, 31],
            [9, 1, 19, 28, 34, 55, 52, 39],
            [12, 18, 28, 32, 41, 52, 57, 46],
            [25, 32, 39, 44, 52, 61, 60, 52],
            [36, 46, 48, 49, 56, 50, 52, 50],
        ]
    )

    # Quantization Matrix for 90%
    quantization_matrix90 = numpy.array(
        [
            [3, 2, 2, 3, 5, 8, 10, 12],
            [2, 2, 3, 4, 5, 12, 12, 11],
            [3, 3, 4, 6, 10, 17, 16, 12],
            [4, 4, 7, 11, 14, 22, 21, 15],
            [3, 3, 3, 5, 8, 11, 14, 11],
            [5, 7, 11, 13, 16, 12, 23, 18],
            [10, 13, 16, 17, 21, 24, 24, 21],
            [14, 18, 19, 20, 22, 20, 20, 20],
        ]
    )

    # Random Quantization Matrix
    quantization_matrix_rand = numpy.array(
        [
            [4, 4, 6, 11, 24, 24, 24, 24],
            [4, 5, 6, 16, 24, 24, 24, 24],
            [6, 6, 14, 24, 24, 24, 24, 24],
            [11, 16, 24, 24, 24, 24, 24, 24],
            [24, 24, 24, 24, 24, 24, 24, 24],
            [24, 24, 24, 24, 24, 24, 24, 24],
            [24, 24, 24, 24, 24, 24, 24, 24],
            [24, 24, 24, 24, 24, 24, 24, 24],
        ]
    )

    # Returns quantization matrix based on quality factor
    def get_quantization_matrix(self, quality_factor=0.75):
        if quality_factor == 0:
            return self.quantization_matrix_rand
        elif quality_factor == 0.5:
            return self.quantization_matrix50
        elif quality_factor == 0.75:
            return self.quantization_matrix75
        elif quality_factor == 0.9:
            return self.quantization_matrix90
