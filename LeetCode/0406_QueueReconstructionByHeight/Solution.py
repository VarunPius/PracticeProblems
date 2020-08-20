class Solution:
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    def reconstructQueue(self, people):
        people.sort(key=lambda a: [a[0], -a[1]], reverse=True)
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        print(people)
        result = people[:]
        for i in people:
            result.remove(i)
            result.insert(i[1], i)
            print(result)
        return result

    def reconstructQueueAlternative(self, people):
        people = sorted(people, key = lambda x: [-x[0], x[1]])
        result = []
        for p in people:
            result.insert(p[1], p)
        return result


"""
people.sort(key=lambda a: [a[0], -a[1]])
[[4, 4], [5, 2], [5, 0], [6, 1], [7, 1], [7, 0]]

people.sort(key=lambda a: [a[0], a[1]], reverse=True)
[[7, 1], [7, 0], [6, 1], [5, 2], [5, 0], [4, 4]]

people.sort(key=lambda a: [a[0], -a[1]], reverse=True)
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
"""

if __name__ == '__main__':
    soln = Solution()
    #x = soln.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    x = soln.reconstructQueueAlternative([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    print(x)

"""
Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
"""