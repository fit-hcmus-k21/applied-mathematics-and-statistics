import numpy as np

def findLinearLeastSquareSolution(A, B):
    # find pseudoinverse matrix of A -> A+ (A_plus)
    U, D, VT = np.linalg.svd(A)

    # find D+
    D_plus = np.zeros((len(A[0]), len(A)))
    for i in range(len(A[0])):
        if i >= len(D): break
        if D[i] != 0: 
            D_plus[i][i] = 1/D[i]

    # find V
    V = np.transpose(VT)

    # find UT
    UT = np.transpose(U)

    # find A+
    A_plus = V @ D_plus @ UT

    # find x
    x = A_plus @ B

    return x[0][0], x[1][0]

def computeMatrix_AB(x, y):
    # init B with len(y) rows and 1 column
    B = [[0 for _ in range(1)] for _ in range(len(y))]
    for i in range(len(y)):
        B[i][0] = y[i]

    # init A with 2 column and len(x) rows
    A = [[0 for _ in range(2)] for _ in range(len(x))]
    for i in range(len(x)):
        A[i][0] = 1
        A[i][1] = x[i]

    return A,B

def round(x):
    return float("{:.1f}".format(x))


def convertCoefficients(A, B):
    for i in range(len(B)):
        B[i][0] = np.log10(B[i][0])

    for i in range(len(A)):
        A[i][1] = A[i][1] - 1970

    return A, B


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        n = int(f.readline())
        for i in range(n):
            x = f.readline().split()
            y = f.readline().split()
            x = np.array(x, dtype=float)
            y = np.array(y, dtype=float)
            A, B = computeMatrix_AB(x, y)
        
            # a. log10(N) = b1 + b2(t - 1970)
            A, B = convertCoefficients(A, B)
            b1, b2 = findLinearLeastSquareSolution(A, B)
            b1 = round(b1)
            b2 = round(b2)
            print("a.")
            print("     b1 = ", b1, " | b2 = ", b2 )
            print("     Duong thang khop voi mo hinh log10(N) = b1 + b2(t - 1970) la: ", end = "")
            print("y = ", b1 , " + ", b2 , "x", sep="")  

            # b.
            print("b.")
            n = int(10**(b1 + b2 * (2015 - 1970)))
            print("     Du doan so bong ban dan trong bo vi xu ly duoc gioi thieu vao nam 2015: ", n)
            if (n > 4 * 10**9) :
                print("     Du doan so bong ban dan trong bo vi xu ly duoc gioi thieu vao nam 2015 > bo vi xu ly IBM Z13 ra doi nam 2015 co so bong ban dan khoang 4 x 10^9")
            elif n < 4 * 10**9:
                print("     Du doan so bong ban dan trong bo vi xu ly duoc gioi thieu vao nam 2015 < bo vi xu ly IBM Z13 ra doi nam 2015 co so bong ban dan khoang 4 x 10^9")
            else:
                print("     Du doan so bong ban dan trong bo vi xu ly duoc gioi thieu vao nam 2015 = bo vi xu ly IBM Z13 ra doi nam 2015 co so bong ban dan khoang 4 x 10^9")

            

