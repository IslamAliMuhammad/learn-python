# python script to convert numbers to words.

class NumberToWords:
    def __init__(self):
        self.ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
        self.thousands = ["", "one thousand", "two thousand", "three thousand", "four thousand", "five thousand", "six thousand", "seven thousand", "eight thousand", "nine thousand"]
       

    def convert(self, number):
        if number < 10: # 1 - 9
            return self.ones[number]
        elif number < 20:   # 10 - 19
            return self.teens[number - 10]
        elif number < 100: # 20 - 99
            return self.tens[number // 10] + " " + self.ones[number % 10]
        elif number < 1000: # 100 - 999
            return self.hundreds[number // 100] + " " + self.convert(number % 100) # floor division // rounds the result down to the nearest whole number 15 / 7 = 7.5 => 15 // 7 = 7
        elif number < 1000000: # 1000 - 999999
            return self.thousands[number // 1000] + " " + self.convert(number % 1000)

num_to_words = NumberToWords()
print(num_to_words.convert(129))



