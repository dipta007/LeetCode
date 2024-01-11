class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        from collections import Counter
        pos = Counter(positive_feedback)
        neg = Counter(negative_feedback)

        students = {}
        for s, r in zip(student_id, report):
            split_r = r.split(' ')
            students[s] = 0
            for sr in split_r:
                if sr in pos: students[s] += 3
                if sr in neg: students[s] -= 1
            
        
        students = [(-v, k) for k, v in students.items()]
        students.sort()
        # print(students)
        return [x for _, x in students[:k]]