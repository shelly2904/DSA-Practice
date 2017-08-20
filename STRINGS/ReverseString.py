class Stack(object):
    def __init__(self):
        self.arr= []
        self.top = -1

    def push(self, data):
        self.arr.append(data)
        self.top += 1

    def pop(self):
        if not self.arr:
            return False
        top = self.arr[self.top]
        del self.arr[self.top]
        self.top-=1
        return top

def reverse(string):
    st = Stack()
    for i in range(0, len(string)):
        st.push(string[i])
    string = ''
    while st.arr:
        string += st.pop()
    return string

if __name__ == "__main__":
    # dt = "i.like.mornings"
    dt = raw_input("Enter the string separated by .")
    word_list = dt.split(".")
    for i in xrange(0, len(word_list)):
        word_list[i] = reverse(word_list[i])

    print ".".join(word_list)