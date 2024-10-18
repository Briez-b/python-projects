################################################## hello_world
print("Hello, World!")

################################################## string_concat
def string_concat():
    print("string-concat:")
    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2
    print(result)

################################################## string_len
def string_len():
    print("string-len:")
    text = "Python is awesome"
    length = len(text)
    print("Length of the string:", length)

################################################## string_lowercase
def string_lowercase():
    print("string-lowercase:")
    text = "Python is awesome"
    uppercase = text.upper()
    lowercase = text.lower()
    print("Uppercase:", uppercase)
    print("Lowercase:", lowercase)

################################################## string_replace
def string_replace():
    print("string-replace:")
    text = "Python is awesome"
    new_text = text.replace("awesome", "great")
    print("Modified text:", new_text)

################################################## string_split
def string_split():
    print("string-split:")
    text = "Python is awesome"
    words = text.split()
    print("Words:", words)

################################################## string_strip
def string_strip():
    print("string-strip:")
    text = "   Some spaces around   "
    stripped_text = text.strip()
    print("Stripped text:", stripped_text)

################################################## string_substring
def string_subsctring():
    print("string-substring:")
    text = "Python is awesome"
    substring = "is"
    if substring in text:
        print(substring, "found in the text")

################################################## float_ops
def float_ops():
    print("floatnum: ")
    # Float variables
    num1 = 5.0
    num2 = 2.5
    # Basic Arithmetic
    result1 = num1 + num2
    print("Addition:", result1)

    result2 = num1 - num2
    print("Subtraction:", result2)

    result3 = num1 * num2
    print("Multiplication:", result3)

    result4 = num1 / num2
    print("Division:", result4)

    # Rounding
    result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
    print("Rounded:", result5)

################################################## int_ops
def int_ops():
    print("int: ")
    # Integer variables
    num1 = 10
    num2 = 5

    # Integer Division
    result1 = num1 // num2
    print("Integer Division:", result1)

    # Modulus (Remainder)
    result2 = num1 % num2
    print("Modulus (Remainder):", result2)

    # Absolute Value
    result3 = abs(-7)
    print("Absolute Value:", result3)

################################################## regex_findall
def regex_findall():
    print("regex-findall: ")
    import re

    text = "The quick brown fox"
    pattern = r"brown"

    search = re.search(pattern, text)
    if search:
        print("Pattern found:", search.group())
    else:
        print("Pattern not found")

################################################## regex_match
def regex_match():
    print("regex-match: ")
    import re

    text = "The quick brown fox"
    pattern = r"quick"

    match = re.match(pattern, text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match")

################################################## regex_replace
def regex_replace():
    print("regex-replace: ")
    import re

    text = "The quick brown fox jumps over the lazy brown dog"
    pattern = r"brown"

    replacement = "red"

    new_text = re.sub(pattern, replacement, text)
    print("Modified text:", new_text)

################################################## regex_search
def regex_search():
    print("regex-search: ")
    import re

    text = "The quick brown fox"
    pattern = r"brown"

    search = re.search(pattern, text)
    if search:
        print("Pattern found:", search.group())
    else:
        print("Pattern not found")


################################################## regex_split
def regex_split():
    import re

    text = "apple,banana,orange,grape"
    pattern = r","

    split_result = re.split(pattern, text)
    print("Split result:", split_result)



# Main execution part
string_concat()
string_len()
string_lowercase()
string_replace()
string_split()
string_strip()
string_subsctring()
float_ops()
int_ops()
regex_findall()
regex_match()
regex_replace()
regex_search()
regex_split()