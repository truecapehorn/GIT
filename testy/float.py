import numpy as np
data_bytes = np.array([0x64, 0xD8, 0x6E, 0x3F,0x64, 0xD8], dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)

print(data_as_float)
print(type(data_as_float))
list=data_as_float.tolist()
print(list)
print(type(list))





