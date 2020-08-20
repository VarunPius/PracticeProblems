"""
Jack plays a game of battleships with his friend Stacy. The game is played on a square map of N
rows, numbered from 1 to N. Each row contains N cells, labeled with consecutive English upper-case
letters (A, B, C, etc.). Each cell is identified by a string composed of its row number followed by its
column number: for example, "9C" denotes the third cell in the 9th row, and "15D" denotes the
fourth cell in the 15th row.
Jack marks the positions of all his ships on the map (which is not shown to Stacy). Ships are defined
by rectangles with a maximum area of 4 cells. Stacy picks map cells to hit some ships. A ship is
considered to be hit if at least one of its constituent cells is hit. If all of a ship's cells are hit, the ship is
sunk.
The goal is to count the number of sunk ships and the number of ships that have been hit but not
sunk.
For example, the picture below shows a map of size N = 4 with two blue ships and five hits marked
with the letter 'X':

<figure1.png>

In this example, one ship has been sunk and the other has been hit but not sunk. In the next picture,
the sunken ship is shown in grey and the ship that has been hit but not yet sunk appears in red:

<figure2.png>

The positions of ships are given as a string S, containing pairs of positions describing respectively the
top-left and bottom-right corner cells of each ship. Ships' descriptions are separated with commas.
The positions of hits are given as a string T, containing positions describing the map cells that were
hit: for the map in the example shown above, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A". Ships in
S and hits in T may appear in any order.
Write a function:
class Solution { public String solution(int N, String S, String T); }
that, given the size of the map N and two strings S, T that describe the positions of ships and hits
respectively, returns a string with two numbers: the count of sunken ships and the count of ships that
have been hit but not sunk, separated with a comma.
For instance, given N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A", your function should return
"1,1", as explained above.
Given N = 3, S = "1A 1B,2C 2C" and T = "1B", your function should return "0,1", because one ship
was hit but not sunk.
The positions of ships are given as a string S, containing pairs of positions describing respectively the
top-left and bottom-right corner cells of each ship. Ships' descriptions are separated with commas.
The positions of hits are given as a string T, containing positions describing the map cells that were
hit: for the map in the example shown above, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A". Ships in
S and hits in T may appear in any order.
Write a function:

class Solution { public String solution(int N, String S, String T); }

that, given the size of the map N and two strings S, T that describe the positions of ships and hits
respectively, returns a string with two numbers: the count of sunken ships and the count of ships that
have been hit but not sunk, separated with a comma.

For instance, given N = 4, S = "1B 2C,2D 4D" and T = "2B 2D 3D 4D 4A", your function should return
"1,1", as explained above.

Given N = 3, S = "1A 1B,2C 2C" and T = "1B", your function should return "0,1", because one ship
was hit but not sunk.

<figure3.png>

Given N = 12, S = "1A 2A,12A 12A" and T = "12A", your function should return "1,0", because one
ship was hit and sunk.
Assume that:

N is an integer within the range [1..26];
string S contains the descriptions of rectangular ships of area not greater than 4 cells;
there can be at most one ship located on any map cell (ships do not overlap);
each map cell can appear in string T at most once;
string S and string T contains only valid positions given in specified format.
In your solution, focus on correctness. The performance of your solution will not be the focus of the
assessment.
"""


def battleship(N, s, t):
    matrix = [[0] * N for _ in range(N)]

    ships = s.split(",")
    hits = t.split(" ")
    for i in range(len(ships)):
        ships[i] = ships[i].split(" ")

    original = set()
    for i in range(len(ships)):
        top_left = ships[i][0]
        bottom_right = ships[i][1]
        top_x = int(top_left[:-1]) - 1
        top_y = ord(top_left[-1]) - 65
        bottom_x = int(bottom_right[:-1]) - 1
        bottom_y = ord(bottom_right[-1]) - 65
        vertical = bottom_x - top_x + 1
        horizonal = bottom_y - top_y + 1
        for m in range(top_x, top_x + vertical):
            for n in range(top_y, top_y + horizonal):
                matrix[m][n] = i + 1
        original.add(i + 1)

    hitted = set()
    for hit in hits:
        x = int(hit[:-1]) - 1
        y = ord(hit[-1]) - 65
        if matrix[x][y] != 0:
            hitted.add(matrix[x][y])
            matrix[x][y] = 0

    updated = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                updated.add(matrix[i][j])

    sunk = len(original - updated)
    hitted_but_not_sunk = len(hitted & updated)

    return sunk, hitted_but_not_sunk

"""
from collections import defaultdict


def battleships(n: int, s: str, t: str) -> str:
    # SETUP A MAP OF LETTER : COLUMN MAPPING
    letter_col = {chr(ord('A') + i): i for i in range(26)}

    # TAG EACH BATTLESHIP PART TO ITS SHIP
    part_ship = dict()
    ship_parts = defaultdict(set)

    # KEEP A MAP OF {SHIP : [PART1, PART2...]} AND {PART : SHIP}
    for ship in s.split(','):
        tl, br = ship.split(' ')
        for i in range(int(tl[0:-1]), int(br[0:-1]) + 1):
            for j in range(ord(tl[-1]) - ord('A'), ord(br[-1]) - ord('A') + 1):
                part = f"{i}{chr(ord('A') + j)}"
                part_ship[part] = ship
                ship_parts[ship].add(part)

    # KEEP COUNT OF THE SUNK AND HIT SHIPS
    sunk = set()
    hit = set()

    # GO THROUGH EACH HITS
    for part_hit in t.split(" "):
        ship = part_ship.get(part_hit)
        if ship_parts.get(ship) is not None:
            ship_parts[ship].remove(part_hit)
            if len(ship_parts[ship]) == 0:
                sunk.add(ship)
                if ship in hit: hit.remove(ship)
            else:
                hit.add(ship)

    return f"{len(sunk)},{len(hit)}"


if __name__ == "__main__":
    print(battleships(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1")
    print(battleships(3, "1A 1B,2C 2C", "1B") == "0,1")
    print(battleships(12, '1A 2A,12A 12A', '12A') == "1,0")

###################################################################################

class Solution:
    def get_hits(self, n: int, s: str, t: str) -> str:
        sunk, hit = 0, 0
        ships = self.get_ships(s)
        for ship in ships:
            if set(ship).issubset(set(t.split())):
                sunk += 1
            elif len(set(ship).intersection(set(t.split()))) > 0:
                hit += 1
        return '{0},{1}'.format(sunk, hit)
    
    def get_ships(self, s: str) -> List[List[str]]:
        ships = [self.get_ship(ship.strip()) for ship in s.split(',')]
        return ships
    
    def get_ship(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tl, br = s.split()
        nums = [str(n) for n in range(int(tl[0:-1]), int(br[0:-1])+1)]
        letters = list(alpha[alpha.index(tl[-1]):alpha.index(br[-1])+1])
        ship = [n+l for l in letters for n in nums]    
        return ship

"""