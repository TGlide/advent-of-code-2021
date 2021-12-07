def getInputFileLines(file_number: str) -> list:
    import os

    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(current_dir, f'../inputs/{file_number}.txt')

    with open(input_file) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]
