if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    liste = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if (i + j + k) != n:
                    liste.append([i,j,k])
                    
    print(liste)

#other way to write this code
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l_x = range(x+1)
    l_y = range(y+1)
    l_z = range(z+1)
    
    return_list = [[a, b, c] for a in l_x for b in l_y for c in l_z if a+b+c != n]
    print(return_list)
