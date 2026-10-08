names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names,scores):
    n=0
    for i in range(len(scores)):
        if scores[i]>scores[n]:
            m=scores[i]
            n=i
    return names[n]
def average(scores):
    if scores!=0:
        return float(f'{(sum(scores)/len(scores))}')
    else:
        return 0.0
def ranking(names,scores):
    indices = list(range(len(names)))
    sorted_indices = sorted(indices, key=lambda i: scores[i], reverse=True)
    result = []
    for i in sorted_indices:
        result.append(names[i])
    return result
def above_average(names,scores):
    if not scores:
        return []
    average = sum(scores) / len(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > average:
            result.append(names[i])
    return result
print(winner(names,scores))
print(average(scores))
print(ranking(names,scores))
print(above_average(names,scores))
