TARGETS = $(basename $(notdir $(wildcard org/*.pdf)))
XBB = $(addsuffix .xbb,$(TARGETS))
PDF = $(addsuffix .pdf,$(TARGETS))

.SUFFIXES: .pdf .xbb
.PHONY: all clean

all: $(XBB) $(PDF)

.pdf.xbb:
	extractbb $<

%.pdf: org/%.pdf
	pdfcrop --pdftexcmd pdflatex --clip $< $@

clean:
	-rm -rf *.pdf *.xbb
