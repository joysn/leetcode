# 85. Maximal Rectangle
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Example 3:
# Input: matrix = [["1"]]
# Output: 1


class Solution:
    def Max_Histo_Area(self,heights):
        import queue
        width = []
        area = []

        #For the left side: Next Smaller Left
        left_s=queue.deque()
        left = []
        for i in range(len(heights)):
            if len(left_s) == 0:
                left.append(0)
                left_s.append([heights[i],i])
            elif len(left_s) > 0 and heights[i] > left_s[-1][0]:
                left.append(left_s[-1][1]+1)
                left_s.append([heights[i],i])
            elif len(left_s) > 0 and heights[i] <= left_s[-1][0]:
                while len(left_s) > 0 and heights[i] <= left_s[-1][0]:
                    left_s.pop()
                if len(left_s) == 0:
                    left.append(0)
                else:
                    left.append(left_s[-1][1]+1)
                left_s.append([heights[i],i])
            # print(i,left)

        #For the right side: Next Smaller Right
        right_s = queue.deque()
        right = []
        pseudo_indx1 = len(heights)
        for i in range(len(heights)-1,-1,-1):
            if len(right_s)==0:
                right.append(pseudo_indx1-1)
            elif len(right_s)>0 and heights[i]>right_s[-1][0]:
                right.append(right_s[-1][1]-1)
            elif len(right_s)>0 and heights[i]<=right_s[-1][0]:
                while len(right_s)>0 and heights[i]<=right_s[-1][0]:
                    right_s.pop()
                if len(right_s)==0:
                    right.append(pseudo_indx1-1)
                else:
                    right.append(right_s[-1][1]-1)
            right_s.append([heights[i],i])
        right=right[::-1]
        # print(right)
        
        for i in range(len(left)):
            width.append(right[i]-left[i]+1)
            
        for i in range(len(heights)):
            area.append(heights[i]*width[i])
            
        return max(area)
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        temp = []
        if len(matrix)==0:
            return 0
        m = len(matrix[0])
        n = len(matrix)
        for j in range(m):
            temp.append(int(matrix[0][j]))
        # print(temp)
        mx = self.Max_Histo_Area(temp)
        for i in range(1,n):
            for j in range(0,m):
                if int(matrix[i][j])==0:
                    temp[j]=0
                else:
                    temp[j]=temp[j]+int(matrix[i][j])
            # print(temp)
            mx=max(mx , self.Max_Histo_Area(temp))
        return mx
        
# Runtime: 649 ms, faster than 15.13% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 16 MB, less than 7.12% of Python3 online submissions for Maximal Rectangle.