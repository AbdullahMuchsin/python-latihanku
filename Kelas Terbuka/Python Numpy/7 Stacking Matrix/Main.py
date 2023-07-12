import numpy as np

if __name__ == '__main__':
    a = np.array([1,2,3,4])
    b = np.array([5,6,7,8])

    aMat = np.zeros((5,6))
    bMat = np.ones((2,6))
    xMat = np.zeros((2,3))
    # Stacking Matrix / Menumpuk Matrix
    c = np.hstack((a,b))
    d = np.vstack((a,b))
    cMat = np.hstack((bMat,xMat))
    dMat = np.vstack((aMat,bMat))

    print("="*20)
    print(c)
    print("="*20)
    print(d)
    print("="*20)
    print(cMat)
    print("="*20)
    print(dMat)