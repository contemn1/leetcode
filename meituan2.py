import sys
def main(zipped_rank, size):
    counter = 0
    print(zipped_rank)
    for start, end in zipped_rank:
        if end < start:
            counter += 1
            continue
        for idx in range(start - 1, -1, -1):
            if  end < zipped_rank[idx][1]:
                counter += 1
                break

    print(counter)



if __name__ == "__main__":
    array_size = int(input())
    start_rank = [int(ele) for ele in  sys.stdin.readline().strip().split(" ")]
    end_rank = [int(ele) for ele in  sys.stdin.readline().strip().split(" ")]
    new_start = {x: y for x, y in sorted(enumerate(start_rank), key=lambda x: x[1])}
    new_end = {y: x for x, y in sorted(enumerate(end_rank), key=lambda x: x[1]) }
    print(new_start)
    print(new_end)
    rank_array = [None] * array_size
    for i in range(array_size):
        rank_array[new_start[i] - 1] = (i, new_end[new_start[i]])

    main(rank_array, array_size)