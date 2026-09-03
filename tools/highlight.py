#!/usr/bin/env python3
"""Generate the Pygments token spans that article code blocks need.

Articles in docs/ ship pre-highlighted: each article inlines its own
`.code-card .k{...}` colour rules and the markup carries `<span class="k">`
tokens. Code pasted in as plain text renders unstyled, so every new sample has
to be run through here first.

    python3 tools/highlight.py snippet.py          # -> highlighted markup
    echo 'x = 1' | python3 tools/highlight.py      # -> reads stdin

Or from Python:
    from highlight import code_card
    print(code_card(source, output='42'))
"""
import html
import sys

from pygments import highlight as _highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

_FORMATTER = HtmlFormatter(nowrap=True)


def spans(source):
    """Python source -> the same source wrapped in Pygments token spans."""
    return _highlight(source, PythonLexer(), _FORMATTER).rstrip('\n')


COPY_ICON = ('<svg class="icon"><use href="#icon-copy"></use></svg>')


def code_card(source, lang='python'):
    """A full .code-card block, matching the structure used across docs/."""
    return (
        '<div class="code-card"><div class="code-head">'
        '<div class="dots"><span></span><span></span><span></span></div>'
        f'<span class="lang">{lang}</span>'
        f'<button class="copy-btn" type="button">{COPY_ICON}Copy</button>'
        f'</div><pre><code>{spans(source)}\n</code></pre></div>'
    )


def output_card(text):
    """An .output-card block. Output is escaped, never highlighted."""
    return f'<div class="output-card"><pre><code>{html.escape(text)}\n</code></pre></div>'


if __name__ == '__main__':
    src = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    print(spans(src.rstrip('\n')))
