"""
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes.
If multiple found, return the pair with the longest movie.
"""


def moviesOnFlight(movieDurations, d):
    d = d - 30
    newM = movieDurations
    newM = sorted(newM, reverse=True)
    maximum = 0
    ans = []
    for i in range(len(newM)):
        for j in range(len(newM) - 1, i, -1):
            sum = newM[i] + newM[j]
            if sum <= d:
                if sum > maximum:
                    maximum = newM[i] + newM[j]
                    ans = [movieDurations.index(newM[i]), len(movieDurations) - movieDurations[::-1].index(newM[j]) - 1]
                    # ans = [movieDurations.index(newM[i]), movieDurations.index(newM[j])]
            else:
                break

    return sorted(ans)

def flightDetails(arr, k):
    k-=30
    arr = sorted(arr)
    left = 0
    right = len(arr)-1
    max_val = 0
    while left<right:
        if arr[left]+arr[right]<=k:
            if max_val < arr[left]+arr[right]:
                max_val = arr[left]+arr[right]
                i = left
                j = right
            left+=1
        else:
            right-=1
    return(arr[i],arr[j])


# [90, 85, 75, 60, 120, 150, 125], 250 | [0,6]
# [90, 85, 75, 60, 120, 150, 125], 50 | []
# [90, 85, 75, 60, 120, 150, 125], 220 | [3,6]
# [10, 50, 60] , 120 | [0,2]
# [90, 85, 75, 60, 120,110,110, 150, 125] , 250 | [5, 6]

print(moviesOnFlight([90, 85, 75, 60, 120, 110, 110, 150, 125], 250))