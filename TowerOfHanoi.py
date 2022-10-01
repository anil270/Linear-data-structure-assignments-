## Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n, first, second, third):
    if n == 0:
        return
    TowerOfHanoi(n-1, first, third, second)
    print("Move disk", n, "first", first, "second", second)
    TowerOfHanoi(n-1, third, second, first)


N=int(input("Enter the Number :"))
TowerOfHanoi(N, 'A', 'C', 'B')