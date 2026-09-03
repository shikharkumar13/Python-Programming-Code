#!/usr/bin/env python3
"""Helpers for editing the course notebooks without reformatting them.

Jupyter writes .ipynb files as JSON with `indent=1` and unescaped unicode.
Loading a notebook with plain `json.load` and dumping it back with different
settings rewrites every line, which turns a two-line change into a diff of
several thousand lines. `load`/`save` here round-trip byte-identically, so a
diff shows only what actually changed.

Usage:
    from nb_edit import load, save, md, code, insert_before_trailing_blank

    nb = load('4. Operators.ipynb')
    insert_before_trailing_blank(nb, [md('# New Section'), code('1 + 1', 5, '2')])
    save('4. Operators.ipynb', nb)
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def save(name, nb):
    (ROOT / name).write_text(
        json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


def src(text):
    """Turn a text block into an ipynb source list.

    Every line keeps its newline except the last, which is how Jupyter stores
    cell source. An empty final line is dropped rather than stored as ''.
    """
    lines = text.split('\n')
    return [l + '\n' for l in lines[:-1]] + ([lines[-1]] if lines[-1] else [])


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": src(text)}


def code(text, count=None, result=None, stdout=None):
    """A code cell.

    `result` is the repr Jupyter echoes for a trailing expression; `stdout` is
    anything the cell prints. Pass the values the cell really produces — run
    the code first. See verify_outputs.py, which re-executes every cell and
    compares.
    """
    outputs = []
    if stdout is not None:
        outputs.append({"name": "stdout", "output_type": "stream",
                        "text": src(stdout)})
    if result is not None:
        outputs.append({"data": {"text/plain": src(result)},
                        "execution_count": count,
                        "metadata": {},
                        "output_type": "execute_result"})
    return {"cell_type": "code", "execution_count": count,
            "metadata": {}, "outputs": outputs, "source": src(text)}


def insert_before_trailing_blank(nb, cells):
    """Insert cells just before a trailing empty code cell, if there is one.

    Most notebooks here end with an empty cell; appending after it would leave
    the blank stranded in the middle of the notebook.
    """
    i = len(nb['cells'])
    if nb['cells'] and nb['cells'][-1]['cell_type'] == 'code' \
            and not ''.join(nb['cells'][-1]['source']).strip():
        i -= 1
    nb['cells'][i:i] = cells
    return nb


def max_execution_count(nb):
    """Highest execution_count in use.

    New cells must be numbered above this. The notebooks were written by hand
    over many sessions, so counts are not monotonic and reusing one produces a
    duplicate that looks like a re-run.
    """
    return max((c.get('execution_count') or 0
                for c in nb['cells'] if c['cell_type'] == 'code'), default=0)


KERNELSPEC = {"display_name": "Python 3 (ipykernel)",
              "language": "python",
              "name": "python3"}


def new_notebook(cells):
    """A notebook shell matching the metadata the existing ten use."""
    return {"cells": cells,
            "metadata": {"kernelspec": KERNELSPEC,
                         "language_info": {
                             "codemirror_mode": {"name": "ipython", "version": 3},
                             "file_extension": ".py",
                             "mimetype": "text/x-python",
                             "name": "python",
                             "nbconvert_exporter": "python",
                             "pygments_lexer": "ipython3",
                             "version": "3.12.8"}},
            "nbformat": 4,
            "nbformat_minor": 5}
