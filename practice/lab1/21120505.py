import numpy as np

# input: ma trận mở rộng của hệ phương trình
# output: ma trận bậc thang (rút gọn)
def Gauss_elimination(A) :
    # số hàng của ma trận A
    nrow = len(A)
    # số cột của ma trận A
    ncol = len(A[0])

    # duyệt qua các hàng của ma trận A
    for r in range(nrow):
        # nếu phần tử A[r][c] trong hàng r là 0
        c = r
        while A[r][c] == 0:
            # tìm trong cột đó, phần tử khác 0, nếu có thì đổi hàng
            for i in range(r+1, nrow):
                if A[i][c] != 0:
                    A[r], A[i] = A[i], A[r]
                    break
            # nếu không có phần tử khác 0 trong cột đó thì xét qua cột tiếp theo
            if A[r][c] == 0:
                c += 1
            if c == ncol:
                break
        # nếu hàng đó không có phần tử khác 0 thì dừng
        if c == ncol:
            break
        # nếu phần tử đó khác 0 thì chia hết các phần tử cùng hàng cho nó
        A[r] = A[r] / A[r][c]
        #  đưa các phần tử cùng cột đó về 0
        for k in range(0, nrow):
            if k != r:
                A[k] = A[k] - A[k][c] * A[r]

    return A

# input: ma trận bậc thang từ ma trận mở rộng của Ax = b
# output : nghiệm của hpt : duy nhất, vô số, vô nghiệm
def back_substitution(A, fout) :
    # số hàng của ma trận A
    nr = len(A)
    # số cột của ma trận A
    nc = len(A[0])

    # trường hợp nghiệm duy nhất
    # số hàng có hệ số A[i][i] khác 0 của ma trận A
    nr_nZero = 0
    for i in range(nr):
        if A[i][i] == 0:
            break
        else:
            nr_nZero += 1
    # nếu số hàng có hệ số tại A[i][i] khác 0 của ma trận A bằng số ẩn của hệ phương trình
    if nr_nZero == nc - 1:  
        fout.write("Phuong trinh co nghiem duy nhat: (")
        for i in range(nr_nZero):
            if i == nr_nZero-1:
                fout.write(str(int(A[i][nc-1]) if A[i][nc-1] == int(A[i][nc-1]) else round(A[i][nc-1], 1)) + ")")
            else:
                fout.write(str(int(A[i][nc-1]) if A[i][nc-1] == int(A[i][nc-1]) else round(A[i][nc-1], 1)) + " ; ")
        fout.write("\n")
        return
    # trường hợp vô nghiệm
    for i in range(nr):
        for j in range(nc):
            if j == nc - 1 and A[i][j] != 0:
                fout.write("Phuong trinh vo nghiem !\n")
                return
            if A[i][j] != 0:
                break
    # trường hợp vô số nghiệm
    fout.write("Phuong trinh co vo so nghiem dang: ")
    # số ẩn của hệ phương trình
    nVar = nc - 1
    # số ẩn không cần đặt tham số 
    count = 0
    for i in range(nr):
        for j in range(nc - 1):
            if A[i][j] != 0:
                count += 1
                break
    # số ẩn cần phải đặt tham số tự do
    nPara = nVar - count
    # đặt ẩn tham số theo thứ tự a,b,c,...
    listPara = [chr(i) for i in range(97, 97 + nPara)]
    listSolutions = []    # danh sách các nghiệm
    for i in range(count):
        if A[i][i] != 0:
            # đưa vào xâu rỗng để xử lý sau
            listSolutions.append("")
        else:
            # nếu A[i][i] = 0 thì đặt tham số cho ẩn đó và đưa vào danh sách nghiệm
            listSolutions.append(listPara.pop(0))
            # tìm phần tử khác 0 đầu tiên trong cùng hàng nếu có
            for j in range(i+1, nc - 1):
                if A[i][j] != 0:
                    # đưa vào xâu rỗng để xử lý sau
                    listSolutions.append("")
                    break
    # nếu còn ẩn tham số thì đưa vào danh sách nghiệm
    for i in range(len(listPara)):
        listSolutions.append(listPara.pop(0))
    # xử lý các nghiệm
    for i in range(nVar - 1, -1, -1):
        if listSolutions[i] == "" and A[i][i] != 0:
            if A[i][nc-1] != 0 :
                listSolutions[i] += str(int(A[i][nc-1]) if int(A[i][nc-1]) == A[i][nc-1] else round(A[i][nc-1], 1))
            # duyệt qua các phần tử cùng hàng phía sau để trừ đi
            for j in range(i + 1, nc-1):
                if A[i][j] != 0:    # x + by = d => x = d - by
                    if A[i][j] > 0:
                        listSolutions[i] += " - " 
                        if int (A[i][j]) == 1 and A[i][j] == int(A[i][j]):  # né trường hợp ghi ra - 1a
                            listSolutions[i] += ""
                        else:
                            listSolutions[i] += str(int(A[i][j]) if A[i][j] == int(A[i][j]) else round(A[i][j], 1))
                    else:
                        listSolutions[i] += " + "
                        if int(A[i][j]) == -1 and A[i][j] == int(A[i][j]):  # né trường hợp ghi ra + 1b
                            listSolutions[i] += ""
                        else:
                            listSolutions[i] += str(int(-1*A[i][j]) if A[i][j] == int(A[i][j]) else round(-1*A[i][j], 1)) 
                    if len(listSolutions[j]) == 1:  # nếu nghiệm đang cần chèn vào chỉ có dạng a hoặc b ..
                        listSolutions[i] += listSolutions[j]
                    else:   # nghiệm đang cần chèn có dạng x = 2a - 3c thì cần chèn trong () sau hệ số 
                        listSolutions[i] += "(" + listSolutions[j] + ")"
    # in ra dạng nghiệm của hệ phương trình
    fout.write("(")
    for i in range(nVar):
        if i == nVar-1:
            fout.write(listSolutions[i] + ")\n")
        else :
            fout.write(listSolutions[i] + " ; ") 

if __name__ == '__main__' :
    # input : file input.txt
            # dòng đầu tiên chứa số lượng ma trận mở rộng
            # dòng tiếp theo chứa số hàng, cột m n của ma trận mở rộng thứ 1
            # m dòng tiếp theo chứa các phần tử của ma trận mở rộng thứ 1
            # tương tự cho các ma trận mở rộng còn lại

    # output : file output.txt
            # dòng đầu tiên chứa số lượng ma trận bậc thang
            # dòng tiếp theo chứa số hàng, cột m n của ma trận bậc thang thứ 1
            # m dòng tiếp theo chứa các phần tử của ma trận bậc thang thứ 1
            # tương tự cho các ma trận bậc thang còn lại
    with open("output.txt", "w") as fout:

        with open("input.txt", "r") as fin:
            # đọc số lượng ma trận mở rộng
            n = int(fin.readline())
            # ghi vào file output
            fout.write(str(n) + "\n")

            # duyệt qua các ma trận mở rộng
            for i in range(n):
                # đọc số hàng, cột m n của ma trận mở rộng thứ i
                m, n = map(int, fin.readline().split())
                # print(f"m, n: {m}, {n}")
                # ghi m,n vào file output
                fout.write(str(m) + " " + str(n) + "\n")

                # khởi tạo ma trận mở rộng thứ i
                A = np.zeros((m, n))

                # đọc các phần tử của ma trận mở rộng thứ i
                for j in range(m):
                    A[j] = list(map(float, fin.readline().split()))

                # đưa về ma trận bậc thang 
                A = Gauss_elimination(A)

                # ghi ma trận mở rộng thứ i vào file output
                for j in range(m):
                    for k in range(n):
                        fout.write(str(int(A[j][k]) if A[j][k] == int(A[j][k]) else round(A[j][k], 1)) + " ")
                    fout.write("\n")
                
                # in nghiệm của hệ phương trình tương ứng với ma trận mở rộng thứ i
                back_substitution(A, fout)
    
