def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) <= 3:
        scores.sort()
        scores.reverse()
        return scores
    top3 = []
    while len(top3) <= 2:
        top3.append(max(scores))
        scores.remove(max(scores))
    top3.sort()
    top3.reverse()
    return top3
