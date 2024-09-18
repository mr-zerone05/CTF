hex_string = "55 54 45 43 54 46 7b 68 33 6c 6c 30 5f 66 72 30 6d 5f 48 43 4d 55 54 45 5f 43 54 46 5f 32 30 32 34 7d"

# Tách chuỗi hex thành các giá trị hex riêng lẻ
hex_values = hex_string.split()

# Chuyển đổi từng giá trị hex thành ký tự và nối chúng lại thành một chuỗi
ascii_string = ''.join(chr(int(h, 16)) for h in hex_values)

print(ascii_string)
