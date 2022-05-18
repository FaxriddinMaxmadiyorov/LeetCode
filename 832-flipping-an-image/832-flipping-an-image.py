class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for k in range(n):
            i, j = 0, n - 1
            while i < j:
                image[k][i], image[k][j] = image[k][j], image[k][i]
                i += 1
                j -= 1
            for j in range(0, n):
                image[k][j] = image[k][j] ^ 1
        return image