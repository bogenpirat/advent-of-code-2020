input = """44
41
48
17
35
146
73
3
16
159
11
29
32
63
65
62
126
151
6
124
87
115
122
43
12
85
2
98
59
156
149
66
10
82
26
79
56
22
74
49
25
69
54
19
108
18
55
131
140
15
125
37
129
91
51
158
117
136
142
109
64
36
160
150
42
118
101
78
28
105
110
40
157
70
97
139
152
47
104
81
27
116
132
143
1
80
75
141
133
9
50
153
123
111
119
130
112
94
90
86"""

joltages = [int(x) for x in input.splitlines()]

# part 1

joltDiffs = {1: 0, 2: 0, 3: 0}
sortedJoltages = [*joltages[:], 0, max(joltages) + 3] # including outlet and device ports
sortedJoltages.sort()

for i in range(1, len(sortedJoltages)):
    diff = abs(sortedJoltages[i] - sortedJoltages[i - 1])
    joltDiffs[diff] += 1

print(joltDiffs[1] * joltDiffs[3])

# part 2

store = {}
def remove(i):
    if i == len(sortedJoltages) - 1:
        return 1
    if i in store:
        return store[i]
    
    removables = 0
    for j in range(i + 1, len(sortedJoltages)):
        if sortedJoltages[j] - sortedJoltages[i] <= 3:
            removables += remove(j)
    
    store[i] = removables

    return removables

print(remove(0))