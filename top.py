import sys
def top(test):
    lines = test.split("\n")
    test_dict = {}
    for i in lines:
        var = i.split()
        test_dict[var[0]] = int(var[1])
    Keymax = max(zip(test_dict.values(), test_dict.keys()))[1]
    return Keymax    
test = sys.stdin.read()
#test = """123 99 java
222 100 top
223 89 head"""
print(top(test))

