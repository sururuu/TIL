import sys
sys.setrecursionlimit(10000)
def post_order(start, end):
    if start > end:
        return
    else:
        root = pre[start]
        div = end + 1 # 두개로 나누는 분기
        for pos in range(start+1, end+1):
            if root < pre[pos]:
                div = pos
                break
        post_order(start+1, div-1)
        post_order(div, end)
        print(root)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
post_order(0, len(pre)-1)