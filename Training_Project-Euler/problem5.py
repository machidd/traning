#2520は1から10の数字の全ての整数で割り切れる数字であり、そのような数字の中では最小の数字である。
#では、1から20までの整数全てで割り切れる数字の中で、最小の正の数はいくらになるか。

N = 2
C = 1
ans = 0

for i in range(20):
    print(N % i)

#    for i in range(20):
#        if N % C == 0:
#           C += 1
#        else:
#            break
#        ans = i

#N/Cをして余りが0になるか判定
#だめならNをインクリメント
#0ならCをインクリメント
#Cが20になった段階で最初に％が0になったNを答えとして出力