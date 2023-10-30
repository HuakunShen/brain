# 630. Course Schedule III

https://leetcode.com/problems/course-schedule-iii/


## Solution 1

Time Complexity: $O(n^2)$

Space Complexity: $O(1)$

```java
/**
Runtime: 808 ms, faster than 7.09% of Java online submissions for Course Schedule III.
Memory Usage: 48.6 MB, less than 5.44% of Java online submissions for Course Schedule III.
 */
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        int time = 0, count = 0;
        for (int i = 0; i < courses.length; i++) {
            if (time + courses[i][0] <= courses[i][1]) {
                // if adding current course is acceptable
                time += courses[i][0];
                count++;
            } else {
                int max_time_index = i;
                for (int j = 0; j < i; j++) {
                    if (courses[j][0] > courses[max_time_index][0]) {
                        // currrent course takes less time than this one (j)
                        max_time_index = j;
                    }
                }
                if (courses[max_time_index][0] > courses[i][0]) {
                    // replace max time course so far with current job
                    time += courses[i][0] - courses[max_time_index][0];
                }
                courses[max_time_index][0] = -1;
            }
        }
        return count;
    }
}
```