# Q16 Simulated method overloading - @JIYO P V 2026-07-13
class SmartCalculator:
    def add(self, a, b, c=0):
        return a + b + c

    def multiply(self, *args):
        p = 1
        for n in args:
            p *= n
        return p

    def process(self, data):
        if isinstance(data, str):
            print(data.upper())
        elif isinstance(data, list):
            total = 0
            for n in data:
                total += n
            print(total)
        else:
            print("Unsupported type")


sc = SmartCalculator()
print(sc.add(2, 3))
print(sc.add(2, 3, 4))
print(sc.multiply(2, 3, 4))
sc.process("hello")
sc.process([1, 2, 3, 4])
