n = 6

# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()


# left side triangle
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# number triangle
# for i in range(n):
#     for j in range(1, i+2):
#         print(j, end="")
#     print()

# number top to bottom triangle
# for i in range(n):
#     for j in range(1, n-i):
#         print(j, end="")
#     print()


# top to bottom triangle
# for i in range(n):
#     for j in range(1,n-i):
#         print("*", end="")
#     print()


# number repeat triangle
# for i in range(n):
#     for j in range(1,i+2):
#         print(i+1, end="")
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()


# for i in range(n):
#     for j in range(1,n-i+1):
#         print(j, end="")
#     print()


# daimond shape
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")

    for j in range(2*i+1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i):
        print(" " , end="")

    for j in range(2*(n-1-i)+1):
        print("*", end="")
    print()


