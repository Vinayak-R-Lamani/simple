def find_symmetric(array: list):
    seen = set()
    symmetric_pairs = []

    for pair in array:
        reversed_pair = tuple(reversed(pair))  # Reverse the tuple
        if reversed_pair in seen:
            symmetric_pairs.append(pair)
        else:
            seen.add(pair)

    # Print the output in the expected format
    for pair in symmetric_pairs:
        print(pair)

if __name__ == "__main__":
    arr = [(1,2), (2,1), (3,4), (4,5), (5,4)]
    find_symmetric(arr)
