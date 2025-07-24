#2559. 2 arrays are given , one of strings, the other of queries. 
# words = ["aba","bcb","ece","ee","a"]
# queries = [[0,2],[1,4],[1,1]] -> represents the different ranges. 
# answer array = [2,3,0] -> number of strings that follow the rule 
'''
IDEA 
go through queries array, get the start and final position 
go through words array in that range, and see if it follows the given rule of the first and last letter of the str to be vowel 

'''

