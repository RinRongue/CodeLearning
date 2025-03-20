def decimal_to_binary(decimal):
    # 分离整数部分和小数部分
    integer_part = int(decimal)
    fractional_part = decimal - integer_part

    # 转换整数部分
    binary_integer_part = bin(integer_part).replace("0b", "")

    # 转换小数部分
    binary_fractional_part = []
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part.append(str(bit))
        fractional_part -= bit
        # 限制小数部分的长度，避免无限循环
        if len(binary_fractional_part) > 10:
            break

    return binary_integer_part + "." + "".join(binary_fractional_part)

# 示例
decimal_number = 0.1
binary_number = decimal_to_binary(decimal_number)
print(f"十进制 {decimal_number} 转换为二进制: {binary_number}")