class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        value = stream.get_next()
        print(value)

if __name__ == '__main__':
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == 'even':
            stream = EvenStream()
        else:
            stream = OddStream()
        print_from_stream(n, stream)