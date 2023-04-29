import numpy
from scipy import fft


class QuantizeDCT:
    def quantize_dct(img, width, height, block_size, stride, Q_8x8):
        """
        Actions performed:
            - Creating sliding windows
            - Applying dct transform to each block
            - Quantization of all dct coefficients

        Returns:
            quantized_row_matrices (list): quantized blocks as rows
        """
        quantized_row_matrices = []

        for i in range(0, height - block_size, stride):
            for j in range(0, width - block_size, stride):
                block = img[i : i + block_size, j : j + block_size]

                # DCT
                dct_matrix = fft.dct(block)

                # quantization of dct co-effs
                quantized_block = numpy.round(numpy.divide(dct_matrix, Q_8x8))
                block_row = list(quantized_block.flatten())

                # left-corner pixel co-ordinates and block
                quantized_row_matrices.append([(i, j), block_row])

        return quantized_row_matrices
