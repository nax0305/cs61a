import hog

# def strat0(s0, s1):
#     if s0 == 0: return 3
#     if s0 == 7: return 5
#     return 8

# def strat1(s0, s1):
#     if s0 == 0: return 1
#     if s0 == 4: return 2
#     return 6

# s0, s1 = hog.play(strat0, strat1, score0=0, score1=0, goal=21,
# dice=hog.make_test_dice(2, 2, 3, 4, 2, 
#                         2, 2, 2, 2, 3, 
#                         5, 2, 2, 2, 2, 
#                         2, 2, 2, 6, 1))


# print(s0)


# def count(n):
#     def say(s0, s1):
#         print(n, s0)
#         return count(n + 1)
#     return say
# s0, s1 = hog.play(hog.always_roll(1), hog.always_roll(1), dice=hog.make_test_dice(3), goal=10, say=count(1))

f0 = hog.announce_highest(1)
f1 = f0(12, 0)
f2 = f1(12, 10)
f2_again = f1(12, 9)