player1 = [1,1,1,10,10,10,10]
player2 = [10,10,10,10,1,1,1]
score_p1 = 0
score_p2 = 0
mult_p1 = 1
mult_p2 = 1
count_p1 = 0 
count_p2 = 0 
for i in range(len(player1)): 
    
    if player1[i]==10 and count_p1<2 : 
        score_p1+=mult_p1*10
        mult_p1 = 2
        count_p1+=1
    elif player1[i]==10 and count_p1>=2:
        mult_p1=1
    else: 

        score_p1+=mult_p1*(player1[i])
        
    if player2[i]==10 and count_p2<2:

        score_p2+=mult_p2*10
        mult_p2=2
        count_p2+=1
    elif player2[i]==10 and count_p2>=2:
        mult_p2=1
    else: 
        
        score_p2+=mult_p2*(player2[i])
print(score_p1,score_p2)
        
if (score_p1>score_p2):
    print(1)
else: 
    print(2)