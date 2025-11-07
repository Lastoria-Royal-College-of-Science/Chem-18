import os
from pathlib import Path
import shutil


def delete_unfinished_lessons(home: str, dry_run: bool = True):
    for unfinished_placeholder in Path(home).glob('**/*.unfinished'):
        print(f'Found {unfinished_placeholder.parent}')

        if dry_run:
            continue

        shutil.rmtree(unfinished_placeholder.parent)
        print(f'Deleted {unfinished_placeholder.parent}')


if __name__ == '__main__':
    DRY_RUN = os.environ.get('DRY_RUN', 'true').lower() != 'false'
    delete_unfinished_lessons('.', dry_run=DRY_RUN)
