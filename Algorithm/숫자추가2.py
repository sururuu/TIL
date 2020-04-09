# 단일 연결 리스트
class Node:
    def __init__(self, data, link):
        self.data = data  # 정수 값
        self.link = link  # 다음 노드 주소

def addLast(data):
    global pHead
    if pHead is None:
        pHead = Node(data,None)
        return

    p=pHead
    while p.link is not None :
        p = p.link
    p.link = Node(data,None)
    return

def insert(idx,data):
    global pHead # 위치찾기
    p = pHead
    n=0
    if idx == 0 :
        pHead = Node(data,pHead)
        return

    while n < idx-1 :
        p = p.link
        n += 1
    p.link = Node(data,p.link)
    return

def get(idx):
    global pHead
    p = pHead
    n = 0
    while p is not None and n<idx:
        p = p.link
        n += 1
    if p is not None:
        return p.data
    else:
        return -1


t=int(input())
for tc in range(1,t+1):
    n,m,l = map(int,input().split())
    pHead = None
    s = list(map(int,input().split()))
    for i in range(n):
        addLast(s[i])
    for i in range(m):
        cmd = list(input().split())
        insert(int(cmd[0]), int(cmd[1]))

    print("#{} {}".format(tc,get(l)))

