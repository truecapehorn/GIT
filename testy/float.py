import numpy as np
data_bytes = np.array([0x64, 0xD8, 0x6E, 0x3F,0x64, 0xD8, 0x6E, 0x3F], dtype=np.uint16)
data_as_float = data_bytes.view(dtype=np.float32)
print(data_as_float)




