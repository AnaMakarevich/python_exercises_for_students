from collections import namedtuple

Candidate = namedtuple('Candidate', ['name', 'age', 'yoe'])
candidates = [Candidate('Alex', 26, 5), Candidate('Roman', 22, 2), Candidate('Olena', 30, 10), Candidate('Kateryna', 28, 8)]

print(list(filter(lambda c: c.age > 25 and c.yoe > 10, candidates)))
