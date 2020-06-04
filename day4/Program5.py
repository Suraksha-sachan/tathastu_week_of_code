from collections import Counter 
votes =['mahesh','suresh','shyam','ram','suresh','mahesh',
      'ram','shyam','ram','mahesh','mahesh','shyam','suresh','ram'] 

vote_count=Counter(votes)
max_votes=max(vote_count.values())
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
print(sorted(lst)[0])
