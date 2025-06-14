input_str = "Hello"

for char in input_str:
    if input_str.count(char) == 1:
        print(char)


# first non repeated charector 

sec_input = "teeter"

for char in sec_input:
    if sec_input.count(char) == 1:
        print(f"\n\n {char}");
        break