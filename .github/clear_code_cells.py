from pathlib import Path
import nbformat


def clear_code_cells(home: str = '.'):
    for ipynb_path in Path(home).glob('Lesson */*.ipynb'):
        if 'Lesson 0' in ipynb_path.parts:
            continue
        print(f'Found {ipynb_path}')

        nb = nbformat.read(ipynb_path, as_version=4)
        for cell in nb.cells:
            if cell.cell_type == 'code':
                cell.source = ''
                cell.outputs = []
                cell.execution_count = None
        nbformat.write(nb, ipynb_path)
        print(f'Cleared {ipynb_path}')


if __name__ == '__main__':
    for home in ('.',):
        clear_code_cells(home)
