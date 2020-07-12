my_lst = ["line", 14, False, {12, 7}, (1, 4), {1: 4, 3: []}, 12.6, bin(12), oct(8), hex(17), complex(5, 6), [],
          b"r", "rg".encode('utf-8'), bytes('gh', encoding='utf-8'), bytes([1, 3]), None, bytearray(b'g'), 0b110]
for i in my_lst:
    print(f"Элемент {i} относится к {type(i)}")
