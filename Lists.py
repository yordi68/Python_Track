if __name__ == '__main__':
   
    N = int(raw_input())
    answer = []
    for i in range(N):
        x = raw_input().split()
        for j in range(1, len(x)):
            x[j] = int(x[j])
        
        if x[0] =="insert":
            answer.insert(x[1], x[2])
        elif  x[0] =="print":
            print(answer)
        elif  x[0] =="remove":
            answer.remove(x[1])
        elif  x[0] =="append":
            answer.append(x[1])
        elif  x[0] =="sort":
            answer.sort()
        elif  x[0] =="pop":
            answer.pop()
        elif  x[0] =="reverse":
            answer.reverse()
