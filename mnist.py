import struct 
from util import save_data, new, prefix
import dtypes

name = "mnist"

images_hash, labels_hash = 0x00000803, 0x00000801

files = [
    {
        "file": "train-images-idx3-ubyte",
        "hash": images_hash,
        "key": "X_train",
    },
    {
        "file": "train-labels-idx1-ubyte",
        "hash": labels_hash,
        "key": "y_train",
    },
    {
        "file": "t10k-images-idx3-ubyte",
        "hash": images_hash,
        "key": "X_test",
    },
    {
        "file": "t10k-labels-idx1-ubyte",
        "hash": labels_hash,
        "key": "y_test",
    },
]

def process(data, file):
    file_path = prefix(name) + file["file"]
    hash = file["hash"]
    key = file["key"]

    with open(file_path, 'rb') as f:

        magic = struct.unpack(dtypes.INT, f.read(4))[0]
        if magic != hash:
            raise AssertionError(f"Magic number {magic} doesn't match for {file_path}")
        
        n = struct.unpack(dtypes.INT, f.read(4))[0]

        if magic == images_hash:
            n_rows = struct.unpack(dtypes.INT, f.read(4))[0]
            n_cols = struct.unpack(dtypes.INT, f.read(4))[0]
            image_size = n_rows * n_cols

            image_data = f.read(n * image_size)

            pixels = struct.unpack(f">{n * image_size}B", image_data)

            for i in range(n):
                image = pixels[i * image_size : (i + 1) * image_size]
                data[key].append(image)

        elif magic == labels_hash:
            label_data = f.read(n)

            labels = struct.unpack(f">{n}B", label_data)
            data[key].extend(labels)

if __name__ == "__main__":
    data = new()
    [process(data, f) for f in files]
    save_data(data, name)