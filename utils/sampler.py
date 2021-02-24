import numpy as np

class Sampler:
    
    def split(data, labels, test_vals, seed=False):
        # splitting data and labels into training and testing sets
        if seed:
            np.random.seed(seed)

        testing_indices = np.random.randint(len(data), size=test_vals)
        training_indices = np.delete(np.arange(len(data)), testing_indices)

        test_x = data[testing_indices]
        test_y = labels[testing_indices]

        train_x = data[training_indices]
        train_y = labels[training_indices]
        
        return test_x, test_y, train_x, train_y