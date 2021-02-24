import numpy as np
import torch

# data augmenting class
class DataAugment:
    
    def shift(tensor, shift=5):
        # adds or subtracts a constant from a 1D tensor, 'shifting' it
        shift_vec = np.ones(len(tensor)) * shift * np.random.choice([-1, 1])
        
        return torch.add(tensor, torch.tensor(shift_vec))
    
    def multiply(tensor, factor=2):
        # multiplies a tensor by a factor
        return torch.mul(tensor, factor)