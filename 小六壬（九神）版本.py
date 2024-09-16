#!usr/bin/python
# Define the nine spirits in order
spirits = ['大安', '留连', '速喜', '赤口', '小吉', '空亡','病符','桃花','天德']
#Explain what the procedure is
print('本程序适用于快速起卦赛博占卜小六壬（九神版本）','清斋九宫小六壬-九神分为“大安, 留连, 速喜, 赤口, 小吉, 空亡,病符,桃花,天德”','本程序只起卦不解卦，具体解卦请自我查询')
# Function to perform divination based on three numbers
def calculate_xiaoliu_ren(numbers):
    position = 0  # Start with '大安'
    result = []
    
    for number in numbers:
        position = (position + number - 1) % len(spirits)  # Move clockwise
        result.append(spirits[position])
    
    return result

# Function to get user input for three numbers
def get_user_input():
    numbers = []
    for i in range(3):
        while True:
            try:
                # Prompt user to input a number
                number = int(input(f"请输入第{i + 1}个数字/Enter number{i+1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("请输入有效的整数！/Please enter a valid integer!")
    return numbers

# Get user input for three numbers
user_numbers = get_user_input()

# Calculate divination results
result_spirits = calculate_xiaoliu_ren(user_numbers)

# Output the results
print("卦象结果/Result:", result_spirits)