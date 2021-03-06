class Calc:
    def add(self, a: int, b: int) -> int:
        return a + b

    @classmethod
    def add3(cls, a: int, b: int) -> int:
        return a + b

    @staticmethod
    def add_static(a: int, b: int) -> int:
        return a + b

    def add2(self, two: tuple):
        return two[0] + two[1]

    def div(self, a, b) -> float:
        return a / b