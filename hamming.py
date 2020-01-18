def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        if strand_a == strand_b:
            return 0
        else:
            return list(map(lambda a, b: 0 if a is b else 1, strand_a, strand_b)).count(1)
    else:
        raise ValueError("Can't compute hamming distance, odd length of strands!")
