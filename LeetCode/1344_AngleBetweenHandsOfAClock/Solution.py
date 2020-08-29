class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = ((hour % 12) * 30) + ((minutes/60) * 30)
        minutes_angle = (minutes * 6)

        angle = abs(hour_angle - minutes_angle)

        if angle > 180:
            angle = 360.0 - angle

        return angle

"""
Hour Hand
In 12 hours Hour hand complete whole circle and cover 360°
So, 1 hour = 360° / 12 = 30°

Since 1 hours = 30°
In 1 minute, hours hand rotate -> 30° / 60 = 0.5°
So total angle because of minutes by hour hand is minutes/60 * 30 or minutes * 0.5

Minute Hand
In 60 minutes Minute Hand completes whole circle and cover 360°.
So, 1 minute -> 360° / 60 = 6°

"""