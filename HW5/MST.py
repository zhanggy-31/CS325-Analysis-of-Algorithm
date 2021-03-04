import math
import sys


def min_edge(key, in_mst, n): # find the shortest edge of the vertex
    min = sys.maxsize
    for v in range(n):
        if key[v] < min and in_mst[v] is False:
            min = key[v]
            index = v
    return index    # return the index of the minimum distance vertex


def Prim(n, edge):  # n is number of vertices, edge is a 2d-array of distance
    key = [sys.maxsize] * n # set distances to maximum first
    p = [None] * n  #
    key[0] = 0
    in_mst = [False] * n    # a set contain the vertices in mst

    for i in range(n):
        u = min_edge(key, in_mst, n)    # find the minimum distance from others to vertices in mst
        in_mst[u] = True                # set the vertice with minimum distance in mst
        for v in range(n):
            if 0 < edge[u][v] < key[v] and in_mst[v] is False:
                key[v] = edge[u][v]
                p[v] = u

    total_weight = 0
    for i in range(1, n):
        total_weight = total_weight + edge[i][p[i]]
    print("Total weight:", total_weight)


def main():
    f = open("graph.txt")
    cases = int(f.readline().strip())   # read cases
    for k in range(cases):
        vertices = int(f.readline().strip())    # read vertices number
        ver = []
        edge = []
        for m in range(vertices):   # put vertices into array
            x, y = map(int, f.readline().strip().split())
            ver.append([x, y])

        for i in range(vertices):   # calculate distance of every vertices to others
            temp = []
            for j in range(len(ver)):
                distance = round(math.sqrt(pow((ver[i][0] - ver[j][0]), 2) + pow((ver[i][1] - ver[j][1]), 2)))
                temp.append(distance)
            edge.append(temp)
        Prim(vertices, edge)    # run Prim


main()
