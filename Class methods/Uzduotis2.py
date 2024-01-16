class StringReversion:
    @classmethod
    def reversed_string(cls, txt):
        return f"{txt}"[::-1]


stringreversion = StringReversion()

result = stringreversion.reversed_string("labas")
print(result)
