# This is the makefile that used for compiling the
# modularized 'heat.exe' for Forward Difference solver 

FLAGS = -fdefault-real-8
OPT   = -O4
DFLAG = 
COMPILER = gfortran $(FLAGS) $(OPT) $(DFLAG)

DEPEND =            \
	write2d.o   \
	ModHeatEq.o \
	HeatEq.o

help:
	@echo "This makefile compiles the heat equation program"
	@echo "make heat.exe: compile the heat equation program"
	@echo "make clean: remove results and all compile files"
	@echo "make debug: clean and compile with debug flags turned on"
	@echo "make viz: update the code, run it and plot results"

heat.exe: $(DEPEND)
	$(COMPILER) $^ -o $@

%.o: %.f90
	$(COMPILER) -c $<	

clean: 
	rm -f *.o *.exe *.mod *~ results.txt

viz: heat.exe
	./$^
	./viz_results.py results.txt