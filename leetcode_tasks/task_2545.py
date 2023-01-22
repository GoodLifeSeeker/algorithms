'''
There is a class with m students and n exams. You are given a 0-indexed m x n
integer matrix score, where each row represents one student and score[i][j]
denotes the score the ith student got in the jth exam. The matrix score
contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the
matrix) by their scores in the kth (0-indexed) exam from the highest to the
lowest.

Return the matrix after sorting it.

Constraints:

- m == score.length
- n == score[i].length
- 1 <= m, n <= 250
- 1 <= score[i][j] <= 105
- score consists of distinct integers.
- 0 <= k < n
'''

from typing import List

## 1) Using quick sort algorythm (recursion)
#def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
#    if len(score) < 2:
#        return score
#    else:
#        pivot = score[0]
#        left = [i for i in score[1:] if i[k] <= pivot[k]]
#        right = [i for i in score [1:] if i[k] > pivot[k]]
#        return sortTheStudents(right, k) + [pivot] + sortTheStudents(left, 2)
#
#print(sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))

# 2) Using ready-made func sorted
def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    return sorted(score, key=lambda a: a[k], reverse=True)

print(sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))