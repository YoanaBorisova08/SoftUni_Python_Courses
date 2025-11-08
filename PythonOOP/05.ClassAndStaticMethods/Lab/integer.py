roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        float_value = int(float_value)
        return cls(float_value)

    @classmethod
    def from_roman(cls, roman_value: str):
        int_value = 0
        for i in range(len(roman_value)):
            if roman_value[i] in roman_numerals:
                if i + 1 < len(roman_value) and roman_numerals[roman_value[i]] < roman_numerals[roman_value[i + 1]]:
                    int_value -= roman_numerals[roman_value[i]]
                else:
                    int_value += roman_numerals[roman_value[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, string_value: str):
        if not isinstance(string_value, str):
            return "wrong type"
        try:
            num = int(string_value)
        except ValueError:
            return "wrong type"

        return cls(num)

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string("abs"))
