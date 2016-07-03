TARGET = thesis

TEX = platex
BIBTEX = pbibtex
DVIPDF = dvipdfmx
PDFLATEX = pdflatex
FONTMAP = ipa.map

.SUFFIXES: .pdf .dvi .tex .bbl .bib
.PHONY: all clean

all: $(TARGET).pdf

.dvi.pdf:
	$(DVIPDF) -f $(FONTMAP) $<

$(TARGET).dvi: $(wildcard *.tex) $(TARGET).bbl NGC.sty
	$(TEX) $(TARGET).tex && $(TEX) $(TARGET).tex

$(TARGET).bbl: references.bib
	cd img; make
	$(TEX) $(TARGET).tex && $(BIBTEX) $(TARGET)

clean:
	-rm -f $(TARGET).aux $(TARGET).bbl $(TARGET).dvi $(TARGET).log $(TARGET).pdf $(TARGET).toc $(TARGET).lof $(TARGET).lot $(TARGET).blg
	cd img; make clean

