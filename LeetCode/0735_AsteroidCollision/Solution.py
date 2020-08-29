class Solution:
    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    def asteroidCollision(self, asteroids):
        result = []

        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(result) and asteroid < 0 and result[-1] > 0:
                # Both asteroids are equal, destroy both.
                if result[-1] == -asteroid:
                    result.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif result[-1] < -asteroid:
                    result.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif result[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                result.append(asteroid)

        return result


"""
Not as clean as the given solution, but perhaps easier to understand.

Some observations:

Negative asteroids without any positive asteroids on the left can be ignored as they will never interact with the upcoming asteroids regardless of their direction.
Positive asteroids (right-moving) may interact with negative asteroids (left-moving) that come later.
We can use a stack called res to efficiently simulate the collisions. We can iterate through the list of asteroids and handle the following scenarios as such:

If res is empty, we push that asteroid into it regardless of directions. Because negative asteroids will be part of the final result while positive asteroids may interact with future negative asteroids.
If the asteroid is positive, push it into res. It will never interact with existing asteroids in res but may interact with future negative asteroids.
If the asteroid is negative, we need to simulate the collision process by repeatedly popping the positive asteroids from the top of the stack and compare to see which asteroid survives the collision. We may or may not need to push the negative asteroid to res depending on the value of the positive asteroids it encounters. Push the negative asteroid if it survives all the collisions.
Scenarios 1 and 2 can be handled in the else case and scenario 3 is the while case.
"""