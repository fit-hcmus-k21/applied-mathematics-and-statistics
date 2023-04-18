import math

# Bài 1:
# input: v1, v2 là hai vector cùng kích thước
# output: tích vô hướng của hai vector
def innerproduct(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[i]
    return sum

# Bài 2:
# hàm lấy độ dài của vector
def lenV(v):
    return math.sqrt(innerproduct(v, v))

# hàm nhân vector với một  số k
def multiplyV(v, k) :
    return [k * v[i] for i in range(len(v))]

# hàm chia vector v cho một số k
def divideV(v, k) :
    return [v[i] / k for i in range(len(v))]

# hàm trừ hai vector
def subV(v1, v2) :
    return [v1[i] - v2[i] for i in range(len(v1))]

# hàm nhân hai ma trận
def NhanMaTran(A, B) :
    # khoi tao ma tran ket qua
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Nhan hai ma tran
    m = len(A) # so dong cua A
    n = len(A[0]) # so cot cua A
    p = len(B[0]) # so cot cua B
    if n == len(B):
        for i in range(m):
            for j in range(p):
                total = 0
                for k in range(n):
                    total = total + A[i][k] * B[k][j]
                # trường hợp = 0 nhưng do sai số nên ra số vô cùng nhỏ
                if total < 10 ** -9:
                    total = 0
                C[i][j] = total
        return C
    print("Hai ma tran khong phu hop")

# Hàm chuyển vị ma trận
def transpose(A):
    # khoi tao ma tran ket qua
    AT = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    m = len(A) # so dong cua A
    n = len(A[0]) # so cot cua A
    for i in range(m):
        for j in range(n):
            AT[j][i] = A[i][j]
    return AT


# input: A là ma trận có m dòng n cột với các phần tử là các số thực
# output: ma trận Q và ma trận R
def QR_factorization(A) :
    # số hàng:
    nrow = len(A)
    # số cột:
    ncol = len(A[0])


    # đưa ma trận về mảng các vector cột {b1, b2, ..., bn}
    B = []
    for i in range(ncol) :
        B.append([A[j][i] for j in range(nrow)])

    # tìm một cơ sở trực giao {u1, u2, ..., un}
    U = []
    for i in range(len(B)):
        Ai = B[i]
        Ui = Ai
        for j in range(len(U)):
            Ui = subV(Ui, multiplyV(U[j], innerproduct(Ai, U[j]) / innerproduct(U[j], U[j])))
        U.append(Ui)

    # tìm cơ sở trực chuẩn {v1, v2, ..., vn}
    V = []
    for i in range(len(U)):
        Vi = divideV(U[i], lenV(U[i]))
        V.append(Vi)


    # Khởi tạo ma trận Q
    Q = []
    for i in range(nrow):
        Q.append([0 for _ in range(ncol)])

    # ma trận Q = [v1, v2, ..., vn]
    for i in range(nrow):
        for j in range(ncol):
            Q[i][j] = V[j][i]

    # ma trận R = Q chuyển vị * A
    T = transpose(Q)
    R = NhanMaTran(T, A)

    return Q,R

if __name__ == '__main__' :
    # test bài 1 
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(f"innerproduct({v1}, {v2}) = {innerproduct(v1, v2)}")

    # test bài 2
    # đọc dữ liệu từ file
    with open('output.txt', 'w') as fout:
        with open('input.txt', 'r') as fin:
            # đọc số ma trận A
            n = int(fin.readline())
            for i in range(n):
                # đọc cỡ ma trận
                nrow, ncol = [int(x) for x in fin.readline().split()]

                # đọc ma trận
                A = []
                for j in range(nrow):
                    A.append([float(x) for x in fin.readline().split()])
                # tính Q, R
                Q, R = QR_factorization(A)
                # ghi kết quả ra file
                fout.write(f"Ma tran A thu {i+1}:\n")
                fout.write(f"- Ma tran Q:\n")
                for i in range(len(Q)):
                    for j in range(len(Q[0])):
                        fout.write(f"{Q[i][j]} ")
                    fout.write('\n')
                fout.write(f"- Ma tran R:\n")
                for i in range(len(R)):
                    for j in range(len(R[0])):
                        fout.write(f"{R[i][j]} ")
                    fout.write('\n')

