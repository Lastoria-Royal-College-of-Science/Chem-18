import os
from pathlib import Path
import nbformat


def clear_code_cells(home: str, *exclude: str, dry_run: bool = True, delete: bool = False):
    for ipynb_path in Path(home).glob('*/*.ipynb'):
        if any(pattern in ipynb_path.parts for pattern in exclude):
            continue
        print(f'Found {ipynb_path}')

        if dry_run:
            continue

        nb = nbformat.read(ipynb_path, as_version=4)

        if delete:
            nb.cells = [*filter(lambda cell: cell.cell_type != 'code', nb.cells)]
            nbformat.write(nb, ipynb_path)
            print(f'Deleted code cells of {ipynb_path}')
            continue

        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            cell.source = ''
            cell.outputs = []
            cell.execution_count = None
        nbformat.write(nb, ipynb_path)
        print(f'Cleared {ipynb_path}')


if __name__ == '__main__':
    DRY_RUN = os.environ.get('DRY_RUN', 'true').lower() != 'false'
    DELETE = os.environ.get('DELETE', 'false').lower() == 'true'
    clear_code_cells('.', 'Lesson 0', dry_run=DRY_RUN, delete=DELETE)
    clear_code_cells('L10n/Chinese', '第0课', dry_run=DRY_RUN, delete=DELETE)
