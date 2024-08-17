test = ["aaaabcc",
        "now is the time for all good men",
        "when in the course of human events",
        "12343848828348488599848"
]
        


class Huff:

    Tree = []
    Coder = {}
    Freq = {}

    def __init__(self, value, freq):
        self.value = value
        self.leaf = True
        self.freq = freq
        self.left = None
        self.right = None
    
    def __repr__(self):
        s = "{leaf: " + str(self.leaf) + ", "
        s = s + "value: " + str(self.value) + ", "
        s = s + "left: " + str(self.left) + ", "
        s = s + "right: " + str(self.right) + ", "
        s = s + "freq: " + str(self.freq) + "}"
        return s

    def insert(self):
        for counter in range(0, len(Huff.Tree)):
            if Huff.Tree[counter].freq >= self.freq:
                Huff.Tree.insert(counter, self)
                return True
        Huff.Tree.insert(len(Huff.Tree), self)
        return True               

    def combine(self, second):
        newNode = Huff('', self.freq + second.freq)
        newNode.value = "branch"
        newNode.leaf = False
        newNode.left = self
        newNode.right = second        
        Huff.Tree.remove(self)
        Huff.Tree.remove(second)
        newNode.insert()
        return True

# def prx(node):
#     level = 0
#     queue = [(level, node)]
#     while len(queue) > 0:
#         (next_level, next_node) = queue.pop()
#         if next_level > level:
#             print("\n", next_level)
#             level = next_level
#         if next_node == None:
#             continue
#         elif next_node.leaf:
#             print(next_node.value)
#             continue
#         else:
#             print(".")
#             queue.insert(0, (next_level + 1, next_node.left))
#             queue.insert(0, (next_level + 1, next_node.right))

def make_leaves():
    for letter, freq in Huff.Freq.items():
        new_node = Huff(letter, freq)
        new_node.insert()

def consolidate():
    while True:
        if len(Huff.Tree) > 1:
            Huff.Tree[0].combine(Huff.Tree[1])
        elif len(Huff.Tree) == 1:
            return True
        else:
            return False

def sub_calc(code, node):
    if node == None:
        return
    elif node.leaf:
        Huff.Coder[node.value] = code
        return
    else:
        sub_calc(code + '0', node.left)
        sub_calc(code + '1', node.right)

def calc_code():
    Huff.Coder = {}
    next_node = Huff.Tree[0]
    sub_calc('', next_node)

def frequencies(input_text):
    Huff.Freq = {}
    for letter in input_text:
        if letter in Huff.Freq.keys():
            Huff.Freq[letter] = Huff.Freq[letter] + 1
        else:
            Huff.Freq[letter] = 1
    return [(k, v) for k, v in Huff.Freq.items()]

def encode(freq, text):
    Huff.Tree = []
    if len(freq) <= 1:
        return None
    else:
        Huff.Freq = dict(freq)
        make_leaves()
        consolidate()
        calc_code()
        s = ""
        for letter in text:
            s = s + Huff.Coder[letter]
        return s

def decode(freq, bits):
    Huff.Tree = []
    if len(freq) <= 1:
        return None
    else:
        text = ""
        Huff.Freq = dict(freq)
        make_leaves()
        consolidate()
        cur_node = Huff.Tree[0]
        for bit in bits:
            if not cur_node.leaf:
                if bit == '0':
                    cur_node = cur_node.left
                if bit == '1':
                    cur_node = cur_node.right
            if cur_node.leaf:
                text = text + cur_node.value
                cur_node = Huff.Tree[0]
        return text

if __name__ == '__main__':
    for text in test:
        freqs = frequencies(text)
        print(text, "\n", freqs)
        coding = encode(freqs, text)
        print("tree:", Huff.Tree)
        print("tree2:", prx(Huff.Tree[0]))
        print("code:", Huff.Coder)
        print(coding, "\nlen:", len(coding))
        print("decoding:", decode(freqs, coding))