# # Approach 1 : Keep count and compare
# class Solution(object):
#     def judgeCircle(self, moves):
#         """
#         :type moves: str
#         :rtype: bool
#         """
#         if (moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")):
#             return True
#         else:
#             return False

# Approach 2 : Consider it as a 2d plain and keep track of x and y co-ordinates 
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
