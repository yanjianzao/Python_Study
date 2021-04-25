class A():
    def test_a(self):
        self.m = "hello"

    def test_b(self):
        self.test_a()
        n = self.m + "world"
        print(n)
if __name__ == '__main__':
    A().test_b()
