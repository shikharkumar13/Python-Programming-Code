# Python Programming Series

A complete, runnable Python course in 20 chapters, taking a reader from their first
literal to a tested, packaged data pipeline. Built as the language prerequisite for
data science, machine learning and AI engineering work.

<p>
  <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white">
  <img alt="20 notebooks" src="https://img.shields.io/badge/notebooks-20-F37626?logo=jupyter&logoColor=white">
  <img alt="882 runnable code cells" src="https://img.shields.io/badge/code%20cells-882-success">
  <img alt="outputs verified" src="https://img.shields.io/badge/outputs-reproducible-brightgreen">
</p>

**Read the companion articles:** <https://shikharkumar13.github.io/Python-Programming-Code/index.html>

---

## Contents

- [What this is](#what-this-is)
- [Getting started](#getting-started)
- [Curriculum](#curriculum)
- [Repository layout](#repository-layout)
- [Reproducible outputs](#reproducible-outputs)
- [Authoring tools](#authoring-tools)
- [Where to go next](#where-to-go-next)

---

## What this is

20 Jupyter notebooks, 1,626 cells, 882 of them executable, with every
output committed and verified. Chapters 1 to 10 also have a long-form written article
published as a static site.

The material is designed around three principles:

**Nothing is asserted without being demonstrated.** Where a chapter warns you about
something, a cell shows it happening. The regex that silently matches a commented-out
HTML element, the `assert` that vanishes under `python -O`, the `@contextmanager`
whose cleanup never runs, the price parser that returns `None` and explodes three
frames later: each is executed, not described.

**Every chapter is unlocked by the one before it.** Decorators open on the timer
written by hand in chapter 7. Generators open on the file read line by line in
chapter 10. The capstone in chapter 20 uses essentially all nineteen.

**The examples are real.** Branded, concrete scenarios rather than `foo` and `bar`,
and from chapter 17 onward, real HTTP requests against a live API.

### Who it is for

Anyone who wants a solid Python foundation before moving into data work. Chapters 1 to 10
assume no programming background. Chapters 11 to 20 assume you have finished them.

### What you need

Python 3.10 or newer, and Jupyter. Chapters 1 to 16 use the standard library only;
chapters 17 and 18 add two packages, and chapter 19 introduces two development tools.

---

## Getting started

```bash
git clone https://github.com/shikharkumar13/Python-Programming-Code.git
cd Python-Programming-Code

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt    # only needed from chapter 17
pip install jupyterlab

jupyter lab "1. Introduction to Python.ipynb"
```

Chapters 1 to 16 need nothing installed beyond Jupyter itself. If you would rather read
than run, chapters 1 to 10 are published as articles at the link above.

### Dependencies

| Package | Needed by | Why |
|---------|-----------|-----|
| `requests` | 17, 18 | HTTP requests |
| `beautifulsoup4` | 18 | HTML parsing |
| `pytest` | 19 | Running the tests that chapter writes |
| `mypy` | 19 | Checking the type hints that chapter writes |

Installing them is itself the worked example in chapter 11, which covers virtual
environments and `requirements.txt` before anything depends on them.

---

## Curriculum

### Part I: The language (chapters 1 to 10)

From literals to file I/O. No third-party packages, no installation.

| # | Chapter | Cells | Notebook | Article |
|--:|---------|------:|----------|---------|
| 1 | **Introduction to Python**<br><sub>Literals, variables, naming, memory model, interpreted vs compiled</sub> | 64 | [open](./1.%20Introduction%20to%20Python.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/1_introduction_to_python.html) |
| 2 | **Lists, Tuples and Strings**<br><sub>Sequence types, slicing, mutability, string methods, formatting</sub> | 171 | [open](./2.%20Lists%2C%20Tuples%20and%20Strings.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/2_lists_tuples_strings.html) |
| 3 | **Sets and Dictionaries**<br><sub>Hashing, set algebra, dictionary methods, comprehensions</sub> | 73 | [open](./3.%20Sets%20and%20Dictionaries.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/3_sets_dictionaries.html) |
| 4 | **Operators**<br><sub>Arithmetic, comparison, logical, bitwise, identity, precedence</sub> | 100 | [open](./4.%20Operators.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/4_operators.html) |
| 5 | **Conditional Statements and Loops**<br><sub>`if`/`elif`/`else`, `for`, `while`, `break`, `continue`, nesting</sub> | 102 | [open](./5.%20Conditional%20Statements%20and%20Loops.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/5_conditionals_loops.html) |
| 6 | **Functions in Python**<br><sub>Definition, arguments, defaults, `*args`, `**kwargs`, scope, `return`</sub> | 53 | [open](./6.%20Functions%20in%20Python.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/6_Python_functions.html) |
| 7 | **Types of Functions in Python**<br><sub>`enumerate`, `zip`, `map`/`filter`/`reduce`, `lambda`, recursion</sub> | 54 | [open](./7.%20Types%20of%20Functions%20in%20Python.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/7_types_of_functions.html) |
| 8 | **Object-Oriented Programming**<br><sub>Classes, four pillars, five inheritance types, MRO, duck typing</sub> | 74 | [open](./8.%20Object%20Oriented%20Programming%28OOPs%29.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/8_OOPs_in_Python.html) |
| 9 | **Exception Handling**<br><sub>Hierarchy, `try`/`except`/`else`/`finally`, chaining, `assert`, logging</sub> | 54 | [open](./9.%20Exception_Handling.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/9_Exception_Handling.html) |
| 10 | **File Handling**<br><sub>Modes, `seek`/`tell`, `os`, `pathlib`, CSV, JSON, `shutil`</sub> | 67 | [open](./10.%20File_Handling.ipynb) | [read](https://shikharkumar13.github.io/Python-Programming-Code/10_File_Handling.html) |

### Part II: How Python is actually written (chapters 11 to 16)

The constructs you meet the moment you read real code, and the tooling around them.

| # | Chapter | Cells | Notebook | Article |
|--:|---------|------:|----------|---------|
| 11 | **Modules and Virtual Environments**<br><sub>`import` machinery, writing modules, packages, pip, venv, layout</sub> | 81 | [open](./11.%20Modules%20and%20Virtual%20Environments.ipynb) | _in progress_ |
| 12 | **Iterators and Generators**<br><sub>Iterator protocol, `yield`, laziness, generator expressions</sub> | 105 | [open](./12.%20Iterators%20and%20Generators.ipynb) | _in progress_ |
| 13 | **Closures and Decorators**<br><sub>First-class functions, closures, `@`, `functools`, decorator factories</sub> | 93 | [open](./13.%20Closures%20and%20Decorators.ipynb) | _in progress_ |
| 14 | **Context Managers**<br><sub>`__enter__`/`__exit__`, `@contextmanager`, `suppress`, `ExitStack`</sub> | 92 | [open](./14.%20Context%20Managers.ipynb) | _in progress_ |
| 15 | **The Standard Library Toolkit**<br><sub>`collections`, `itertools`, `functools`, `datetime`</sub> | 125 | [open](./15.%20The%20Standard%20Library%20Toolkit.ipynb) | _in progress_ |
| 16 | **Regular Expressions**<br><sub>Raw strings, character classes, groups, greedy vs lazy, `re.escape`</sub> | 91 | [open](./16.%20Regular%20Expressions.ipynb) | _in progress_ |

### Part III: Working with real data (chapters 17 to 20)

Getting data from the network, and shipping code that survives contact with it.

| # | Chapter | Cells | Notebook | Article |
|--:|---------|------:|----------|---------|
| 17 | **Working with APIs**<br><sub>HTTP verbs, status codes, timeouts, retries, keys, pagination</sub> | 64 | [open](./17.%20Working%20with%20APIs.ipynb) | _in progress_ |
| 18 | **Web Scraping**<br><sub>`robots.txt`, BeautifulSoup, selectors, tables, encoding, ethics</sub> | 61 | [open](./18.%20Web%20Scraping.ipynb) | _in progress_ |
| 19 | **Writing Reliable Code**<br><sub>Type hints, `mypy`, docstrings, `logging`, `pytest`, tracebacks</sub> | 58 | [open](./19.%20Writing%20Reliable%20Code.ipynb) | _in progress_ |
| 20 | **Capstone Project**<br><sub>End-to-end pipeline: package, tests, validation, CSV and JSON output</sub> | 44 | [open](./20.%20Capstone%20Project.ipynb) | _in progress_ |

---

## Repository layout

```
.
├── 1. Introduction to Python.ipynb     the 20 chapters, in order
├── ...
├── 20. Capstone Project.ipynb
│
├── docs/                               the published site (GitHub Pages)
│   ├── index.html                      series index
│   └── N_topic.html                    one self-contained article per chapter
│
├── sample_data/                        frozen fixtures, committed on purpose
│   ├── github_repo.json                real API responses, trimmed (ch. 17)
│   ├── issues_page_*.json              paginated responses (ch. 17)
│   └── shop_page_*.html                hand-written pages to parse (ch. 18)
│
├── tools/                              authoring helpers, not a build step
│   ├── nb_edit.py                      byte-identical notebook round-trip
│   ├── series.py                       the canonical chapter list and nav
│   ├── verify_outputs.py               re-execute and diff committed outputs
│   └── highlight.py                    Pygments spans for article code blocks
│
└── requirements.txt
```

Each article in `docs/` is a single self-contained HTML file: inline stylesheet, inline
SVG icon sprite, inline script, and code blocks pre-highlighted with Pygments. The only
external dependency is Google Fonts. Nothing is generated from the notebooks; the
articles are hand-written expansions of the same material.

---

## Reproducible outputs

Notebook outputs are committed, which means a wrong one reaches a reader looking exactly
like a right one. Every committed output in this repository has been executed and
checked:

```bash
python3 tools/verify_outputs.py --all              # re-run all 20, diff every output
python3 tools/verify_outputs.py "4. Operators.ipynb"
```

The script executes each notebook in a fresh kernel and compares the result against what
is on disk. It reports mismatches without touching the file. All 20 chapters pass from
a clean checkout and pass again on a repeat run, which is the check that catches the
outputs that are only correct the second time you run them.

**Run it twice.** Python randomises string hashing per process, so anything printing a
set's iteration order passes one run and fails the next. The same applies to `id()`,
memory addresses in a default `repr`, and timings. None of them belong in a committed
output, and two runs is what finds them.

49 cells carry a `skip-verify` tag because their output legitimately differs every
run: live network calls, timestamps, memory addresses, interactive `input()`, and set
iteration order. They still execute; only the comparison is skipped, and the reason is
recorded per cell.

### Offline by default

The network chapters read committed fixtures from `sample_data/`, so chapters 17 and 18
produce the same output every time and work with no internet. A small number of clearly
marked cells make a real request, and the notebooks say so up front.

---

## Authoring tools

`tools/` holds four helpers used to write and maintain the material. They are not a build
step: `docs/` is hand-authored and nothing in it is generated from the notebooks.

| Tool | Purpose |
|------|---------|
| `nb_edit.py` | Loads and saves notebooks byte-identically (`indent=1`, `ensure_ascii=False`), so a two-line change produces a two-line diff instead of rewriting every line of the file. |
| `series.py` | The single ordered list of chapters. Regenerates the prev/next navigation across every article, and skips chapters whose article does not exist yet so no page ever links to a 404. |
| `verify_outputs.py` | Executes a notebook in a fresh kernel and reports outputs that no longer reproduce. |
| `highlight.py` | Emits the Pygments token spans that the article code blocks require. |

```bash
python3 tools/series.py list         # chapter list, and what exists so far
python3 tools/series.py nav --check  # report prev/next drift across articles
python3 tools/series.py nav          # rewrite the nav blocks
```

---

## Where to go next

This repository ends where the data work begins. Chapter 20 produces a clean, tidy CSV
and hands it over deliberately:

1. **This repository.** The Python language, and getting data in.
2. **NumPy, pandas and exploratory analysis.** The dataset from chapter 20 is the file
   you walk in with.
3. **Machine learning, MLOps and AI engineering.** Everything that needs a trained model
   or a deployed service.

---

## Notes

- Chapters are self-contained enough to read out of order, but each one builds on the
  vocabulary of the last, and later chapters reference earlier ones by number.
- The demo directories that chapters write while running (`file_handling_demo/`,
  `module_demo/`, `api_demo/` and others) are gitignored. `sample_data/` is the
  exception and is committed on purpose.
- Articles for chapters 11 to 20 are in progress. The notebooks are complete.
