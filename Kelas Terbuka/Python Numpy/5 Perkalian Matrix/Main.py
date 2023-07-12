import numpy as np
if __name__ == '__main__':
    a = np.array([[1,2],
                  [4,5]])
    b  = np.array([[6,5],
                   [3,3]])
    x = np.ones((2,1))
    
    # perkalian Matrix
    c1 = np.dot(a,b)
    c2 = a.dot(b)
    x1 = a.dot(x)

    print("Matrix c1 :")
    print(c1)
    print("Matrix c2 :")
    print(c2)
    print("Matrix x1 :")
    print(x1)
