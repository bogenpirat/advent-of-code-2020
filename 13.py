input = """1004345
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,379,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,557,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"""

earliestDeparture = int(input.splitlines()[0])
buses = [ int(x) for x in list(filter(lambda x: x != 'x', input.splitlines()[1].split(','))) ]
from copy import deepcopy
busLabels = deepcopy(buses)

# part 1

while min(buses) < earliestDeparture:
    for i, timestamp in enumerate(buses):
        if buses[i] < earliestDeparture:
            buses[i] += busLabels[i]

print('labels:', busLabels)
print('buses:', buses)
minTimestamp = min(buses)
minWaitIdx = buses.index(minTimestamp)
print(f'waiting time from {earliestDeparture}: bus {busLabels[minWaitIdx]} with {minTimestamp - earliestDeparture}mins')
print(f'solution: bus label * wait time = {busLabels[minWaitIdx] * (minTimestamp - earliestDeparture)}')
print()

# part 2

"""    ,            _..._            ,
      {'.         .'     '.         .'}
     { ~ '.      _|=    __|_      .'  ~}
    { ~  ~ '-._ (___________) _.-'~  ~  }
   {~  ~  ~   ~.'           '. ~    ~    }
  {  ~   ~  ~ /   /\     /\   \   ~    ~  }
  {   ~   ~  /    __     __    \ ~   ~    }
   {   ~  /\/  -<( o)   ( o)>-  \/\ ~   ~}
    { ~   ;(      \/ .-. \/      );   ~ }
     { ~ ~\_  ()  ^ (   ) ^  ()  _/ ~  }
      '-._~ \   (`-._'-'_.-')   / ~_.-'
          '--\   `'._'"'_.'`   /--'
              \     \`-'/     /
               `\    '-'    /'
                 `\       /'
                   '-...-'

that's me right now. i'm a clown because i chose to solve this part of the problem like this.
look at my red nose. isn't it stupid?"""


offsets = []
offset = 0
for c in input.splitlines()[1].split(','):
    if c != 'x':
        offsets.append(offset)
    offset += 1

print('labels:', busLabels)
print('offsets:', offsets)

print('{ ', end='')
for i in range(0, len(busLabels)):
    print(f'Mod[t+{offsets[i]}, {busLabels[i]}] == 0', end='')
    if i != len(busLabels) - 1:
        print(', ', end='')
print('}')

# wolframalpha says that this solves to
#   840493039281088 + 896915841102983 n, n in Z
# so for a meaningful solution of the first possible time, we set n = 0
# our solution is hence 840493039281088.