# nodeinfo에 각 노드의 좌표가 1번 노드부터 순서대로 들어있다.
# 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 배열로 담아 return
import sys

sys.setrecursionlimit(10 ** 6)
preorder = []
postorder = []


def solution(nodeinfo):
    # 일단 y부터 상위 순서대로 추출
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    # 각 노드에 번호를 붙여야 나중에 바로 print할수 있음. 이때 바로 전위순위를 찾을 수 있게끔 y축은 내림차순 x축은 오름차순 정렬
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)), key=lambda x: (-x[1][1], x[1][0]))
    order(nodes, levels, 0)

    return [preorder, postorder]


# 재귀함수를 짭시다
def order(nodes, levels, cnt):
    # 현재 최상단, 제일 왼쪽의 노드 번호를 전위순위에 append
    pre = nodes.pop(0)
    preorder.append(pre[0])

    # 남아있는 노드 개수만큼 반복
    for i in range(len(nodes)):
        if nodes[i][1][1] == levels[cnt + 1]:  # 현재level에서 하나 더 내려간 level로 이동해야함!
            if nodes[i][1][0] < pre[1][0]:  # 더 왼쪽에 있으면
                order([x for x in nodes if x[1][0] < pre[1][0]], levels, cnt + 1)
            else:
                order([x for x in nodes if x[1][0] > pre[1][0]], levels, cnt + 1)
    postorder.append(pre[0])