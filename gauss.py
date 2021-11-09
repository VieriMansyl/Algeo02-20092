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
        for col in range(len(mat[0])):
            mat[row][col], mat[change_row][col] = mat[change_row][col], mat[row][col]

    return ischange, mat


# konversi elemen menjadi 1 utama disesuaikan pada baris ke-row tersebut
def bagi1utama(mat, row, col):
    pembagi = mat[row][col]
    for col in range(len(mat[0])):
        mat[row][col] /= pembagi
    return mat


# konversi elemen menjadi 0 yang berada di bawah 1 utama disesuaikan pada seluruh row
def makeZero(mat, row, col, pas):
    j = col
    divisor = mat[pas][j]
    divident = mat[row][j]
    while (j < len(mat[0])):
        mat[row][j] -= (divident / divisor) * mat[pas][j]
        j += 1

    return mat


def gauss(mat):
    colEff = 0  # kolom efektif , dimana 1 utama belum terdefinisi

    for pas in range(len(mat)):
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

            if (row > pas and isChange):
                # prekondisi : selalu berada dibawah 1 utama
                # membentuk nilai 0 dibawah 1 utama disesuaikan pada baris ke-row tersebut
                mat = makeZero(mat, row, colEff, pas)

            elif (not isChange):
                row = len(mat)
            row += 1

        colEff += 1

    return mat


def gaussJordan(mat):

    for p in range(len(mat)-1):
        for r in range(p+1, len(mat), 1):
            ratio = mat[p][r]
        for s in range(len(mat[0])):
            mat[p][s] -= ratio * mat[r][s]

    return mat
