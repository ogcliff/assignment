X = [1,3,7,12,18,26,35,45,56,69,83,98]
Y = [2,4,5,6,8,9,10,11,13,14,15]

def min_x_index_greater_than_n(n):
    l = [i for i in X if i > n]
    if len(l) == 0:
        return -1
    num = min(l)
    return X.index(num)

def generate_sequencies(N):
    n = len(Y)
    while n < N:
        while True:
            index = min_x_index_greater_than_n(Y[-1])
            if index == -1:
                print("mbola")
                break
            print("passed")

            if X[index] - Y[-1] == 1:
                Y.append(X[index] + 1)

            new_list = []
            for i in range(Y[-1], X[index]):
                new_list.append(i)
            Y.extend(new_list[1:])
            if len(new_list) > 1:
                break
            print(Y)
            if len(Y) > N + 1:
                break

        while True:
            if len(Y) >= len(X):
                X.append(X[len(X)-1] + Y[len(X)-1])
            else:
                break
        
        n = min(Y[len(Y) - 1], X[len(X) - 1])

def main():
    n = int(input("Enter index to be searched for: "))
    generate_sequencies(n)
    print(X)
    print(Y)
    # return x[n]

main()