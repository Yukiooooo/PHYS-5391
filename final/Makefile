# This is the makefile that used for compiling 
# both the Fortran and LaTex source code

# Rules for compiling Fortran
FLAGS = -fdefault-real-8
OPT   = -O4
DFLAG =
COMPILER = gfortran $(FLAGS) $(OPT) $(DFLAG)

DEPEND =	\
	read_ampfac.o	\
	print_matrix.o

j.exe: $(DEPEND)
	$(COMPILER) $^ -o $@

%.o: %.f90
	$(COMPILER) -c $<

# Rules for compiling LaTex
DOC=final
TEX=pdflatex
BIB=final.bib

pdf: $(DOC).tex $(DOC).bbl
	$(TEX) $<
	$(TEX) $<

$(DOC).bbl: $(BIB) $(DOC).tex
	$(TEX) $(DOC).tex
	bibtex $(DOC)

help:	
	@echo "This makefile compiles both Fortran and LaTex"
	@echo "make: compile Fortran: read AMPERE FAC"	
	@echo "make pdf: compile LaTex: create the pdf file"
	@echo "make clean: remove results and all compile files"

clean:
	rm -rf *~ *.o *.mod $(MODULE)  *.aux *.blg *.dvi *.log *.bbl *~ *.toc $(DOC).pdf


