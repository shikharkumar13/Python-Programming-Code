#!/usr/bin/env python3
"""Re-execute a notebook and report cells whose committed output is wrong.

Outputs are committed to this repo, so a stale or invented output ships to
readers as if it were real. This runs the notebook in a fresh kernel and
compares, without touching the file on disk.

    python3 tools/verify_outputs.py "11. Modules and Virtual Environments.ipynb"
    python3 tools/verify_outputs.py --all

Cells tagged `skip-verify` in their metadata are reported as skipped rather
than compared — for the handful that make live network calls.
"""
import copy
import pathlib
import sys

import nbformat
from nbclient import NotebookClient

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _text(outputs):
    """Flatten a cell's outputs to comparable plain text."""
    parts = []
    for o in outputs:
        if o.get('output_type') == 'stream':
            parts.append(''.join(o.get('text', [])))
        elif o.get('output_type') in ('execute_result', 'display_data'):
            parts.append(''.join(o.get('data', {}).get('text/plain', [])))
        elif o.get('output_type') == 'error':
            parts.append(o.get('ename', '') + ': ' + o.get('evalue', ''))
    return ''.join(parts).strip()


def verify(name):
    nb = nbformat.read(ROOT / name, as_version=4)
    fresh = copy.deepcopy(nb)
    NotebookClient(fresh, timeout=120, kernel_name='python3',
                   resources={'metadata': {'path': str(ROOT)}}).execute()

    problems, skipped, checked = [], 0, 0
    for i, (before, after) in enumerate(zip(nb.cells, fresh.cells)):
        if before.cell_type != 'code' or not ''.join(before.source).strip():
            continue
        if 'skip-verify' in before.get('metadata', {}).get('tags', []):
            skipped += 1
            continue
        checked += 1
        want, got = _text(before.outputs), _text(after.outputs)
        if want != got:
            problems.append((i, ''.join(before.source).strip().split('\n')[0], want, got))

    print(f'{name}: {checked} cells checked, {skipped} skipped, {len(problems)} mismatched')
    for i, first_line, want, got in problems:
        print(f'  cell {i}: {first_line[:60]}')
        print(f'    committed: {want[:200]!r}')
        print(f'    actual:    {got[:200]!r}')
    return not problems


if __name__ == '__main__':
    if sys.argv[1:] == ['--all']:
        names = sorted((p.name for p in ROOT.glob('*.ipynb')),
                       key=lambda n: int(n.split('.')[0]))
    else:
        names = sys.argv[1:]
    sys.exit(0 if all([verify(n) for n in names]) else 1)
