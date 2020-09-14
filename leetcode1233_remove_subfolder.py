# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# 1233. Remove Sub-Folders from the Filesystem
# Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it.
# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.
# Example 1:
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
# Example 2:
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
# Example 3:
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]

# ["/a/b","/a","/c/d","/c/d/e","/c/f"]
# ["/aa/ab/ac/ae","/aa/ab/af/ag","/ap/aq/ar/as","/ap/aq/ar","/ap/ax/ay/az","/ap","/ap/aq/ar/at","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao"]

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        if folder is None:
            return []
        
        if len(folder) == 0:
            return []
        
        folder.sort()
        op = [folder[0]]
        prev, prev_l = op[0]+'/', len(op[0])+1
        for e in folder[1:]:
            if e[:prev_l] != prev:
                op.append(e)
                prev, prev_l = e+'/', len(e)+1
        return op
        