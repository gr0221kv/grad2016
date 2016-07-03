#!/usr/bin/env python3
from jinja2 import Template

# [(name, in, ptm_time, prop_time, ptm_mem, prop_mem), ...]
data = [("C17", 5, 0.212, 0.000, 0.000, 0.003),
        ("decod", 5, 5.132, 0.000, 1.020, 0.007),
        ("xor5", 5, 3.589, 0.000, 0.227, 0.008),
        ("z4ml", 7, 3.849, 0.006, 1.004, 0.015),
        ("9symml", 9, 89.145, 0.035, 6.668, 0.025),
        ("x2", 10, 11.015, 0.006, 2.344, 0.008),
        ("cu", 14, 23.700, 0.195, 2.215, 0.013),
        ("parity", 16, 1.060, 0.309, 0.113, 0.015),
        ("pm1", 16, 72.384, 0.168, 3.734, 0.016),
        ("pcle", 19, 28.810, 4.411, 3.309, 0.014),
        ("cc", 21, 57.400, 18.326, 4.839, 0.019),
        ("mux", 21, 18.052, 22.765, 2.051, 0.017),
        ("c8", 28, 35559.500, 5538.100, 930.023, 0.041)]

class Row(object):
    def __init__(self, *cols, end=None):
        if end == None:
            self.set_end_hline()
        elif isinstance(end, tuple):
            self.set_end_cline(*end)
        else:
            self.end = end
        self.set_cols(cols)
    def set_cols(self, cols):
        self.cols = " & ".join(cols)
    def set_end_cline(self, b, e):
        self.end = "\\cline{%d-%d}" % (b, e)
    def set_end_hline(self):
        self.end = "\\hline"
    def set_end_noline(self):
        self.end = ""
    def __str__(self):
        result = self.cols + " \\\\"
        if self.end:
            result += " " + self.end
        return result

def multi(body, cols=2, align='c'):
    return "\\multicolumn{%d}{|%s|}{%s}" % (cols, align, body)

template = Template("""\\begin{table}[tbp]
  \\centering
  \\caption{caption}
  \\begin{tabular}{{ '{' }}{{ col_aligns }}{{ '}' }} \\Hline{% for row in rows %}
    {{ row }}{% endfor %}
  \\end{tabular}
  \\label{tb:{{ label }}}
\end{table}""")

def div_round(a, b):
    if b == 0.:
        b = 0.001
    return round(a / b, 1)

def gen_data_row(r):
    return (str(a) for a in (r[0], r[1], r[2], r[3], div_round(r[2], r[3]), r[4], r[5], div_round(r[4], r[5])))

print(template.render(
    col_aligns="l|r||r|r|r|r|r|r",
    label="compare",
    rows=[
        Row("", "", multi("Time (s)", 3), multi("Memory (MB)", 3), end=(3, 8)),
        Row(multi("回路名", 1), multi("入力", 1), multi("PTM", 1), multi("提案", 1), multi("比率", 1), multi("PTM", 1), multi("提案", 1), multi("比率", 1)),
    ] + [Row(*gen_data_row(r)) for r in data]
))
