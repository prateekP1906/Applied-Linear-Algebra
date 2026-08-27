from vec import Vec

if __name__ == "__main__":
    v1 = Vec([0, 1, 1.03])
    print(v1)
    
    v3 = 2.2 * v1 #rmul
    print(v3)
    
    v3 *= 5 #imul
    print(v3)
    
    v2 = v1 + v3 
    print(v1 + v3)

    print(len(v1)) #length of vector 1
    print(v1.norm()) #
    print(Vec.zeros(3))
    print(Vec.ones(3))
    print(Vec.uniform(3))
    
    print(v1 - v3)
    print(-v1)
    print(1 + v1)
    
    v1 += v3
    print(v1)