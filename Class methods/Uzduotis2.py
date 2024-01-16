class StringReversion:
    @classmethod
    def reversed_string(cls, txt):
        return f"{txt}"[::-1]


stringreversion = StringReversion()

result = stringreversion.reversed_string("Hello,")
print(result)

# class StringReversion:
#     @staticmethod
#     def reversed_string(txt):
#         return txt[::-1]
#
# print(stringreversion.reversed_string("world!"))