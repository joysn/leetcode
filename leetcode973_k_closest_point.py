# https://leetcode.com/problems/k-closest-points-to-origin/
# 973. K Closest Points to Origin
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

from heapq import heappop, heappush, heappushpop

class Point:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist
        
    def __lt__(self,other):
        return self.dist >= other.dist
    
    def __repr__(self):
        return str([self.x,self.y,round(self.dist,2)])
    
    
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        if K < 0:
            return
        
        def distance(p1):
            return math.sqrt(p1[0]**2 + p1[1]**2)
        
        l = len(points)
        
        closest_points = []

        for i in range(l):
            point = Point(points[i][0],points[i][1],distance(points[i]))
            if len(closest_points) < K:
                heappush(closest_points,point)
            else:
                heappushpop(closest_points,point)
                
        op = []
        for i in range(len(closest_points)):
            temp_p = heappop(closest_points)
            op.append([temp_p.x,temp_p.y])
            
        return op
        