"""
The data and code inspiration have been gained from the book "Mastering Concurrency" by Packt.
"""
import multiprocessing
import os
import cv2
import time


def get_single_image(input_path, name, threshold_method, output_path):
    image = cv2.imread(os.path.join(input_path, name))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_image = cv2.adaptiveThreshold(gray_image, 255, threshold_method, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(os.path.join(output_path, name), threshold_image)
    return image


def process(output_path, names, input_path, n_processes=multiprocessing.cpu_count() // 2):
    with multiprocessing.Pool(n_processes) as pool:
        result = pool.starmap(get_single_image, [(input_path, name, THRESHOLD_METHOD, output_path) for name in names])


if __name__ == "__main__":
    THRESHOLD_METHOD = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    INPUT = r".\data\input"
    OUTPUT = r".\data\output"

    number = 20
    names = [f'ship_{j}_{i}.jpg' for i in range(number) for j in range(number)]
    for n_processes in range(1, 5):
        start = time.time()
        process(output_path=OUTPUT, input_path=INPUT, names=names, n_processes=n_processes)
        end = time.time()
        print(end - start)





