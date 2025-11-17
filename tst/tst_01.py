import torch

from torch_repr_shape import enable_torch_repr_shape

enable_torch_repr_shape()

a = torch.tensor([0, 1, 2, 3])
print(a)
