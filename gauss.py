import numpy as np

def getRowMain(mat, i):
    found1Utama = False
    row = i+1

    while (row > 0 and not(found1Utama)):
        row -= 1
        col = 0
        nonZero = False

        while (col <= i-1 and not(nonZero)):
            if(mat[row][col] != 0):
                nonZero = True
            else:
                col += 1

        if (not(nonZero) and (mat[row][col] == 1)):
            found1Utama = True

    if ((row == 0) and not (found1Utama)):
        row = 999
    return row

# mengembalikan nilai tiap variabel (x1,x2,...x ke-n) bersesuaian pada matriks


def getValue(mat):
    idx_UNDEF = 999
    paramCol = 0

  # inisialisasi matriks solusi -> menyimpan nilai konstanta berserta keof. parameternya
    solusi = [[0 for i in range(len(mat[0]))] for j in range(len(mat[0]))]

    # Kalau baris paling bawah 1, berarti dia kepake parameternya (atau nggak full 0)
    for i in range(len(mat)-1, -1, -1):  # dari X ke-n s.d. X1
        if (getRowMain(mat, i) == idx_UNDEF):
            paramCol += 1
            solusi[i][paramCol] = 1
            solusi[len(solusi) - 1][paramCol] = 1
        else:
            rowMain = getRowMain(mat, i)
            # C , p , q , dst (C : constant ; p,q,... : parameter)
            for j in range(0, paramCol + 1):
                for k in range(i+1, len(mat), 1):
                    solusi[i][j] -= mat[rowMain][k] * solusi[k][j]

    return solusi

# mengembalikan matriks berisikan vektor-vektor eigen



def isColZero(mat, row, col):
    isfound = False

    while (row < len(mat) and not(isfound)):
        if(abs(mat[row][col]) > 0):
            isfound = True
        else:
            row += 1
    return row


# Menukar baris dengan elemen terdefinisi pada kolom ke-col
def changeplace(mat, row, col):
    ischange = False
    # memberikan nilai baris yang elemen pada col memiliki nilai != 0
    change_row = isColZero(mat, row, col)
    if ((change_row != row) and (change_row != len(mat))):
        ischange = True
        mat[row], mat[change_row] = mat[change_row], mat[row]

    return ischange, mat


# konversi elemen menjadi 1 utama disesuaikan pada baris ke-row tersebut
def bagi1utama(mat, row, col):
    pembagi = mat[row][col]
    for col in range(len(mat[0])):
        mat[row][col] /= pembagi
    return mat


# konversi elemen menjadi 0 yang berada di bawah 1 utama disesuaikan pada seluruh row
def makeZero(mat, row, col, pas):
    j = col  # j = 4
    divisor = mat[pas][j]  # divisor = 1
    divident = mat[row][j]  # divdent = -10
    # print(j)
    # print(divident)
    # print(divisor)
    while (j < len(mat[0])):
        mat[row][j] -= (divident / divisor) * mat[pas][j]
        j += 1

    return mat


def makeGauss(mat):
    colEff = 0  # kolom efektif , dimana 1 utama belum terdefinisi
    pas = 0

    while pas < len(mat):
        if(colEff >= len(mat[0])):
            break

        row = pas
        isChange = True
        while (row < len(mat)):
            if (mat[row][colEff] == 0 and (row == pas)):
                # memutar baris apabila m[row][col] = 0
                # isChange menjadi penentu terjadi pertukaran baris atau tidak
                isChange, mat = changeplace(mat, row, colEff)

            if ((row == pas) and (mat[row][colEff] != 1) and isChange):
                # m[row][col] bukan 1 utama dan bukan 0 serta bukan tepat di bawah sebuah 1 utama
                mat = bagi1utama(mat, row, colEff)

            if (row > pas and mat[row][colEff] != 0):
                # prekondisi : selalu berada dibawah 1 utama
                # membentuk nilai 0 dibawah 1 utama disesuaikan pada baris ke-row tersebut
                mat = makeZero(mat, row, colEff, pas)

            elif (not isChange):
                row = len(mat)
                pas -= 1

            row += 1

        colEff += 1
        pas += 1

    return mat



