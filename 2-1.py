def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("請輸入大於0的整數。")
        except ValueError:
            print("無效輸入，請輸入一個整數。")

def calculate_range_sum(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

num1 = get_positive_integer("請輸入第一個大於0的整數: ")
num2 = get_positive_integer("請輸入第二個大於0的整數: ")

result = calculate_range_sum(num1, num2)

print(f"\n{num1} 到 {num2} 之間所有整數的總和是：{result}")
