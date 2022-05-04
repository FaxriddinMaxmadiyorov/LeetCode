class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def area(a, b, c, d, e, f):
            return abs(a*d+c*f+e*b-(e*d+a*f+c*b)) / 2
        maxi = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    maxi = max(maxi, area(*points[i], *points[j], *points[k]))
                    
        return maxi