import numpy
from operator import itemgetter


class LexicographicSort:
    def lexographic_sort(quantized_row_matrices):
        """
        Operations performed:
            - Finding matched blocks
            - Euclidean operations for calculating shift vectors

        Returns:
            shift_vec_count(list): The count of shift vectors
            matched_blocks (dict): Dictionary of the blocks matched
        """
        sorted_blocks = sorted(quantized_row_matrices, key=itemgetter(1))

        matched_blocks = []

        shift_vec_count = {}

        for i in range(len(sorted_blocks) - 1):
            if sorted_blocks[i][1] == sorted_blocks[i + 1][1]:
                point1 = sorted_blocks[i][0]
                point2 = sorted_blocks[i + 1][0]

                # shift vector
                s = numpy.linalg.norm(numpy.array(point1) - numpy.array(point2))

                # increment count for s
                shift_vec_count[s] = shift_vec_count.get(s, 0) + 1
                matched_blocks.append(
                    [sorted_blocks[i][1], sorted_blocks[i + 1][1], point1, point2, s]
                )

        return shift_vec_count, matched_blocks
