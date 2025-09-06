import numpy as np
from PIL import Image

class Decomposer:
    def __init__(self, imagePath):
        with Image.open(imagePath) as img:
            self.imgMatrix = np.asarray(img, dtype=np.float64)
        
        self.rows, self.cols, self.channels = self.imgMatrix.shape
            
        self.row_approx = np.ones((self.channels, self.rows))
        self.col_approx = np.ones((self.channels, self.cols))

    def decompose(self, iterations=10):
        for i in range(iterations):
            col_sums = self.col_approx.sum(axis=1, keepdims=True)
            self.row_approx = self.imgMatrix.sum(axis=1).T / col_sums
            
            row_sums = self.row_approx.sum(axis=1, keepdims=True)
            self.col_approx = self.imgMatrix.sum(axis=0).T / row_sums

    def save(self, filename="data"):
        with open(f"{filename}.txt", "w") as fl:
            fl.write(f"{self.rows}\n{self.cols}\n")
            
            for i in range(3):
                fl.write(" ".join(map(str, self.row_approx[i])))
                fl.write("\n")
                fl.write(" ".join(map(str, self.col_approx[i])))
                fl.write("\n")

        print(f"saved to {filename}")


class Recomposer:
    def __init__(self, filename="data"):
        self.filename = filename
        self.load_data()
    
    

    def load_data(self):
        with open(self.filename, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        self.rows = int(lines[0])
        self.cols = int(lines[1])   

        self.row_approx = np.zeros((3, self.rows))
        self.col_approx = np.zeros((3, self.cols))

        self.row_approx[0] = np.array(list(map(float, lines[2].split(" "))))
        self.col_approx[0] = np.array(list(map(float, lines[3].split(" "))))

        self.row_approx[1] = np.array(list(map(float, lines[4].split(" "))))
        self.col_approx[1] = np.array(list(map(float, lines[5].split(" "))))

        self.row_approx[2] = np.array(list(map(float, lines[6].split(" "))))
        self.col_approx[2] = np.array(list(map(float, lines[7].split(" "))))

    def rebuild(self):
        rebuilt_channels = []
        for i in range(3):
            channel_matrix = np.outer(self.row_approx[i], self.col_approx[i])
            rebuilt_channels.append(channel_matrix)
        
        rebuilt_matrix = np.stack(rebuilt_channels, axis=-1)
        rebuilt_matrix = np.clip(rebuilt_matrix, 0, 255).astype(np.uint8)
        
        return Image.fromarray(rebuilt_matrix)


if __name__ == "__main__":
    print("--- DECOMPOSITION PROCESS ---")
    decomposer = Decomposer("original.jpg")
    decomposer.decompose(iterations=20)
    decomposer.save(filename="deetah")
    
    print("\n" + "="*30 + "\n")
    
    print("--- RECOMPOSITION PROCESS ---")
    recomposer = Recomposer(filename="deetah.txt")
    
    rebuilt = recomposer.rebuild()
    rebuilt.save("recomposed.jpg")
    rebuilt.show()