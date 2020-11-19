class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1, len(coordinates)):
            xyc = coordinates[i]
            xyp = coordinates[i-1]
            print(xyc, xyp)
            if xyc[0] == xyp[0]:
                return False
        pslope = (coordinates[1][1]-coordinates[0][1])//(coordinates[1][0]-coordinates[0][0])
        for i in range(1, len(coordinates)):
            xyc = coordinates[i]
            xyp = coordinates[i-1]
            if xyc[0] == xyp[0]:
                return False
            slope = (xyc[1]-xyp[1])//(xyc[0]-xyp[0])
            if pslope != slope:
                return False
            slope = pslope
        return True

    # pretty dirty implementation, need a better solution
    # though i believe this is O(n)