# Merge Sort


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # print("M-INP:", A, p, q, r, n1, n2)
    L = []
    R = []
    # print("n:", range(0, n1), range(0, n2))
    for i in range(0, n1):
        #L[i] = A[p+i-1]
        L.append(A[p + i])
    for j in range(0, n2):
        #R[j] = A[q+j]
        R.append(A[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    # print L, R, p, r
    for k in range(p, r + 1):
        # print(L, R, 'k =', range(p, r + 1))
        # print("ijk:", i, j, k)
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

    # print("M-OUT:", A)


def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


DATA = [5, 2, 4, 7, 1, 3, 2, 6]
OUT = DATA[:]

print("Merge Sort")
print("Input:", DATA)
merge_sort(DATA, 0, len(DATA) - 1)
print("Output  :", DATA)
