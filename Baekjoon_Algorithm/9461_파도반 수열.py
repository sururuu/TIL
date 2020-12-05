T = int(input())
P = [int(input()) for _ in range(T)]
sequence = [1,1,1]
for i in range(3, 101):
    sequence.append(sequence[i - 3] + sequence[i - 2])
for i in range(T):
    print(sequence[P[i]-1])
