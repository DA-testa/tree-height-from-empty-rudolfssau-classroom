#221RDB085 Rudolfs Saukums 12 grupa
import sys
import threading
import numpy as np


def compute_tree_height(n, parents):
    height_array = np.zeros(n)

    def compute_node_height(i):
        if height_array[i] != 0:
            return height_array[i]
        if parents[i] == -1:
            height_array[i] = 1
        else:
            height_array[i] = compute_node_height(parents[i]) + 1
        return height_array[i]

    for i in range(n):
        compute_node_height(i)

    return int(max(height_array))


def main():
    input_mode = input()
    if "I" in input_mode:
        n = int(input())
        parent_nodes = list(map(int, input().split()))
    elif "F" in input_mode:
        filename = input()
        if "a" not in filename:
            with open(str("test/" + filename), mode="r") as file:
                n = int(file.readline())
                parent_nodes = list(map(int, file.readline().split()))
        else:
            print("Error: invalid file name.")
    else:
        print("Invalid input mode.")
        return

    tree_height = compute_tree_height(n, parent_nodes)
    print(tree_height)


sys.setrecursionlimit(10 ** 7)  # maximum depth of recursion
threading.stack_size(2 ** 27)  # new thread will get a stack of this size
threading.Thread(target=main).start()