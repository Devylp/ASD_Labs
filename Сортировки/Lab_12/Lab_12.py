# №12 Внешняя многофазная сортировка (или внешняя сортировка слиянием)
import Lab_10 as ms
import os

def read_file(input_file):
    '''Генератор: читает числа по одному из файла (используется для входного файла и временных кусков)'''
    with open(input_file, 'r') as f:
        for line in f:
            for n in line.split():
                if n.strip(): yield int(n)


def external_multiway_merge_sort(input_, output_, size=5) -> None:
    # 1. Разделение и первичная сортировка
    buffer, files, i = [], [], 0
    for num in read_file(input_):
        buffer.append(num)
        if len(buffer) >= size:
            name = f"chunk_{i}.txt"
            # Запись
            with open(name, 'w') as f:
                f.write(' '.join(map(str, ms.merge_sort(buffer))))

            files.append(name);
            buffer, i = [], i + 1
    if buffer:
        name = f"chunk_{i}.txt"
        with open(name, 'w') as f:
            f.write(' '.join(map(str, ms.merge_sort(buffer))))
        files.append(name)

    # 2. Слияние
    sources = []
    for f_name in files:
        it = read_file(f_name)
        try:
            sources.append([next(it), it])
        except StopIteration:
            pass

    with open(output_, 'w') as f_out:
        while sources:
            min_idx = 0
            for j in range(1, len(sources)):
                if sources[j][0] < sources[min_idx][0]:
                    min_idx = j

            val, it = sources[min_idx]
            f_out.write(f"{val} ")

            try:
                sources[min_idx][0] = next(it)
            except StopIteration:
                sources.pop(min_idx)

    for f_name in files:
        os.remove(f_name)



input_file = 'input.txt'
output_file = 'sorted_result.txt'

external_multiway_merge_sort(input_file, output_file, size=5)

with open(output_file, 'r') as f:
    print(f.read())
