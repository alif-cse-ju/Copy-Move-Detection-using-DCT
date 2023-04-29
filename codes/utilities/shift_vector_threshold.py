class ShiftVectorThreshold:
    def shift_vector_thresh(shift_vec_count, matched_blocks, shift_thresh):
        """
        Returns:
            matched_pixels_start (list): list of all the matched pixels by shift vector threshold
        """
        matched_pixels_start = []
        for shift in shift_vec_count:
            if shift_vec_count[shift] > shift_thresh:
                for row in matched_blocks:
                    if shift == row[4]:
                        matched_pixels_start.append([row[2], row[3]])
        
        return matched_pixels_start