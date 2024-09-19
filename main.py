import numpy as np
from concurrent.futures import ThreadPoolExecutor

def sum_part(arr, start, end):
    return np.sum(arr[start:end])

def main():
    size = 500000
    parts = 4

    # Ініціалізація масиву зі значеннями 1
    arr = np.ones(size, dtype=int)

    # Розбивка на частини та запуск потоків
    with ThreadPoolExecutor(max_workers=parts) as executor:
        futures = []
        for i in range(parts):
            start = i * (size // parts)
            end = size if i == parts - 1 else start + (size // parts)
            futures.append(executor.submit(sum_part, arr, start, end))

        # Отримання результатів
        partial_sums = [future.result() for future in futures]

    # Обчислення загальної суми
    total_sum = sum(partial_sums)

    print(f"Загальна сума: {total_sum}")

if __name__ == "__main__":
    main()
