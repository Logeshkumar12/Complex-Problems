#There are N people standing in a circle waiting to be executed. 
#The counting out begins at some point in the circle and proceeds around the circle in a fixed direction.
#In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle 
#(which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. 

def Josh(person, k, index):
    if len(person) == 1:
        print(person[0])
        return
    
    index = ((index+k)%len(person))
    print("Count:" ,len(person))
    print("index :",index)
    person.pop(index)
    print(person)
    
    Josh(person,k,index)


n = int(input("No of Person: "))
k = int(input("Skip value: "))
k-=1
index = 0
person=list(range(1,n+1))
Josh(person,k,index) 