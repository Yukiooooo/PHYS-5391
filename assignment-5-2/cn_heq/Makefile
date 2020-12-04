# This is the makefile that used for 
# compiling 'heat.exe' for C-N method

default: heat.exe

# variables:
FLAGS = -fdefault-real-8
OPT = -O3
LIBS = -mkl
DFLAG = 
LIB_MKL=/opt/intel/mkl/lib
COMPILER = ifort $(FLAGS) $(DFLAG) $(OPT) -L$(LIB_MKL) $(LIBS)
DEPEND = \
	ModWrite2d.o   \
	ModHeatCN.o \
	nmum_e10_4.o

help:
	@echo "This makefile compiles the heat equation program"
	@echo "make heat.exe: compile the heat equation program"
	@echo "make clean: remove results and all compile files"
	@echo "make debug: clean and compile with debug flags turned on"
	@echo "make viz: update the code, run it and plot results"

debug: 
	make clean
	make DFLAG='-g -fbacktrace -fbounds-check' 

heat.exe: $(DEPEND)
	$(COMPILER) $^ -o $@

%.o: %.f90
	$(COMPILER) -c $<	

clean: 
	rm -f *.o *.exe *.mod *~ results.txt

viz: heat.exe
	./$^
	./viz_results.py results.txt
