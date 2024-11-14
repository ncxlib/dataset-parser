from util import load_data 

dataset = "mnist"

data = load_data(dataset)
print(f"Train Data Shape: {len(data['X_train']), len(data['X_train'][0])}")
print(f"Train Labels Size: {len(data['y_train']), 1}")
print(f"Test Data Shape: {len(data['X_test']), len(data['X_test'][0])}")
print(f"Test Label Size: {len(data['y_test']), 1}")


