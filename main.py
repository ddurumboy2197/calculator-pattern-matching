def calculator(num1: float, num2: float, operator: str) -> float:
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError("Bo'lishda 0 bo'lishi mumkin emas!")
        case _:
            raise ValueError("Qabul qilinadigan operatorlar: +, -, *, /")
```

```python
# Test qilish
print(calculator(10, 2, "+"))  # 12.0
print(calculator(10, 2, "-"))  # 8.0
print(calculator(10, 2, "*"))  # 20.0
print(calculator(10, 2, "/"))  # 5.0
try:
    print(calculator(10, 0, "/"))  # ValueError: Bo'lishda 0 bo'lishi mumkin emas!
except ValueError as e:
    print(e)

try:
    print(calculator(10, 2, "%"))  # ValueError: Qabul qilinadigan operatorlar: +, -, *, /
except ValueError as e:
    print(e)
