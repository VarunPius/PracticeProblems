class Solution:
    def nextClosestTime(self, time: str) -> str:
        return


"""
While there are some very clever solutions in the discussion, this is a simple (and fast) solution that I'd expect someone to come up with in an interview.

The core idea here is time wraps around minute and hour values, both of which can only be two digit values. 
We generate all the possible two digit values (there are at most 16) in order to solve for both.

The minute value of the solution will be:

    the smallest generated number higher than the input minute, if it is valid minute
    OR
    the smallest generated number, since we have to wrap around the next hour

Likewise, the hour value of the solution will be

    the smallest generated number higher than the input hour, if it is a valid hour
    OR
    the smallest generated number, since we have to wrap around the next day

class Solution(object):
    def nextClosestTime(self, time):
        ""
        :type time: str
        :rtype: str
        ""
        hour, minute = time.split(":")
        
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        two_digit_values = [a+b for a in nums for b in nums]

        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ":" + two_digit_values[i+1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ":" + two_digit_values[0]
        
        # Return the earliest time of the next day
        return two_digit_values[0] + ":" + two_digit_values[0]

"""
