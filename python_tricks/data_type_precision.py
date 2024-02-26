import torch

import numpy as np

array = np.array([0.123456789], dtype=np.float16)
print("array is 16 bits: ", array[0])

array = np.array([0.123456789], dtype=np.float32)
print("array is 32 bits: ", array[0])


matrix_A = torch.randn(100, 100, dtype=torch.float32, device="cpu")
matrix_B = torch.randn(100, 100, dtype=torch.float32, device="cpu")

import time

start_time = time.time()

result = torch.matmul(matrix_A, matrix_B)

print(
    "Matrix calculation time in float32: --- %s seconds ---"
    % (time.time() - start_time)
)

matrix_A = torch.randn(100, 100, dtype=torch.float16, device="cpu")
matrix_B = torch.randn(100, 100, dtype=torch.float16, device="cpu")

start_time = time.time()

result = torch.matmul(matrix_A, matrix_B)

print(
    "Matrix calculation time in float16: --- %s seconds ---"
    % (time.time() - start_time)
)

a_half_tensor = torch.HalfTensor(4096)
print(a_half_tensor.shape)

a_float_tensor = torch.FloatTensor(4096)

a_half_tensor.fill_(1)
print("a half tensor sum: ", a_half_tensor.sum())
a_half_tensor.fill_(2)
print("a half tensor sum: ", a_half_tensor.sum())
a_half_tensor.fill_(4)
print("a half tensor sum: ", a_half_tensor.sum())
a_half_tensor.fill_(8)
print("a half tensor sum: ", a_half_tensor.sum())
a_half_tensor.fill_(16)


a_float_tensor.fill_(16.0)


print("a half tensor sum: ", a_half_tensor.sum())
print("a float tensor sum: ", a_float_tensor.sum())


small_half_tensor = torch.HalfTensor([1.0])
very_small_half_tensor = torch.HalfTensor([[0.0001]])

small_float_tensor = torch.FloatTensor([1.0])
very_small_float_tensor = torch.FloatTensor([[0.0001]])

print(small_half_tensor + very_small_half_tensor)
print(small_float_tensor + very_small_float_tensor)
