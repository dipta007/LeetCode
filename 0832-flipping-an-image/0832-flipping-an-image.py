class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r, c = len(image), len(image[0])

        for i in range(r):
            lft, rgt = 0, c-1
            while lft < rgt:
                image[i][lft], image[i][rgt] = image[i][rgt], image[i][lft]
                lft += 1
                rgt -= 1

            for j in range(c):
                image[i][j] = int(not image[i][j])

        return image