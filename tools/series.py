#!/usr/bin/env python3
"""The canonical topic list, and prev/next navigation built from it.

docs/ has no shared stylesheet or partial: every article is a standalone file.
That means the "previous / next" links are duplicated across articles by hand,
and adding a topic silently leaves the one before it pointing nowhere. This
module keeps the ordering in one place and regenerates the nav from it.

    python3 tools/series.py list          # show the series and what exists
    python3 tools/series.py nav           # rewrite nav in every article
    python3 tools/series.py nav --check   # report drift, change nothing

`article=None` means the article has not been written yet: it is skipped when
linking, so no article ever links to a page that would 404 on the live site.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'

# num, short title used in nav links, notebook, article, template
SERIES = [
    (1,  'Introduction to Python',           '1. Introduction to Python.ipynb',            '1_introduction_to_python.html', 'A'),
    (2,  'Lists, Tuples and Strings',        '2. Lists, Tuples and Strings.ipynb',         '2_lists_tuples_strings.html',   'B'),
    (3,  'Sets and Dictionaries',            '3. Sets and Dictionaries.ipynb',             '3_sets_dictionaries.html',      'B'),
    (4,  'Operators',                        '4. Operators.ipynb',                         '4_operators.html',              'B'),
    (5,  'Conditional Statements and Loops', '5. Conditional Statements and Loops.ipynb',  '5_conditionals_loops.html',     'B'),
    (6,  'Functions in Python',              '6. Functions in Python.ipynb',               '6_Python_functions.html',       'B'),
    (7,  'Types of Functions in Python',     '7. Types of Functions in Python.ipynb',      '7_types_of_functions.html',     'A'),
    (8,  'Object-Oriented Programming',      '8. Object Oriented Programming(OOPs).ipynb', '8_OOPs_in_Python.html',         'B'),
    (9,  'Exception Handling',               '9. Exception_Handling.ipynb',                '9_Exception_Handling.html',     'B'),
    (10, 'File Handling',                    '10. File_Handling.ipynb',                    '10_File_Handling.html',         'B'),
    # Phase A in progress: notebooks land first, articles are backfilled.
    (11, 'Modules and Virtual Environments', '11. Modules and Virtual Environments.ipynb', None, 'B'),
    (12, 'Iterators and Generators',         '12. Iterators and Generators.ipynb', None, 'B'),
    (13, 'Closures and Decorators',          '13. Closures and Decorators.ipynb', None, 'B'),
    (14, 'Context Managers',                 '14. Context Managers.ipynb', None, 'B'),
    (15, 'The Standard Library Toolkit',     '15. The Standard Library Toolkit.ipynb', None, 'B'),
    (16, 'Regular Expressions',              '16. Regular Expressions.ipynb', None, 'B'),
    (17, 'Working with APIs',                None, None, 'B'),
    (18, 'Web Scraping',                     None, None, 'B'),
    (19, 'Writing Reliable Code',            None, None, 'B'),
    (20, 'Capstone Project',                 None, None, 'B'),
]

REPO_URL = 'https://github.com/shikharkumar13/Python-Programming-Code'
SITE_URL = 'https://shikharkumar13.github.io/Python-Programming-Code'


def published():
    """Only the topics whose article exists — the ones safe to link."""
    return [row for row in SERIES if row[3]]


def notebook_url(notebook):
    """A blob URL: .ipynb files are not served by GitHub Pages."""
    from urllib.parse import quote
    return f'{REPO_URL}/blob/main/{quote(notebook)}'


_WORDS = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'nineteen', 20: 'twenty'}


def _count(n):
    """The articles spell the count out ("All ten articles"); keep that."""
    return _WORDS.get(n, str(n))


def build_nav(i, indent):
    """Nav block for published()[i]. Links only to articles that exist."""
    rows = published()
    parts = []
    if i > 0:
        _, title, _, article, _ = rows[i - 1]
        parts.append(f'<a class="prev" href="{article}">'
                     f'<span class="dir">← Previous</span>'
                     f'<span class="name">{title}</span></a>')
    if i < len(rows) - 1:
        _, title, _, article, _ = rows[i + 1]
        parts.append(f'<a class="next" href="{article}">'
                     f'<span class="dir">Next →</span>'
                     f'<span class="name">{title}</span></a>')
    parts.append(f'<a class="all" href="index.html">All {_count(len(rows))} articles</a>')
    pad = ' ' * indent
    inner = ('\n' + pad + '  ').join(parts)
    return f'{pad}<nav class="series-nav">\n{pad}  {inner}\n{pad}</nav>'


NAV_RE = re.compile(r'^[ \t]*<nav class="series-nav">.*?</nav>', re.S | re.M)


def update_nav(check_only=False):
    rows, changed = published(), []
    for i, (num, title, _, article, tpl) in enumerate(rows):
        path = DOCS / article
        text = path.read_text()
        indent = 6 if tpl == 'B' else 2
        nav = build_nav(i, indent)
        if not NAV_RE.search(text):
            print(f'  !! no nav block in {article} — insert one first')
            continue
        new = NAV_RE.sub(lambda m: nav, text, count=1)
        if new != text:
            changed.append(article)
            if not check_only:
                path.write_text(new)
    verb = 'would change' if check_only else 'updated'
    print(f'{verb}: {len(changed)} article(s)' + (': ' + ', '.join(changed) if changed else ''))
    return changed


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'list'
    if cmd == 'list':
        for num, title, nb, article, tpl in SERIES:
            nb_ok = '✓' if nb and (ROOT / nb).exists() else '·'
            ar_ok = '✓' if article and (DOCS / article).exists() else '·'
            print(f'{num:>3}. [nb {nb_ok}] [article {ar_ok}]  {title}')
    elif cmd == 'nav':
        update_nav(check_only='--check' in sys.argv)
    else:
        sys.exit(__doc__)
