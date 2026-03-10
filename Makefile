# specifying the compiler
CXX = clang++

# O3 is optimization to make code faster, wall enables the warnigs, std=c++17 tells c++ version , shared means make a library , 
# fpic is so that library can be loaded anywhere in the memory
CXXFLAGS =-O3 -Wall -std=c++17 -shared -fPIC

#variables
srcdir = src_cpp
buildir = build
target = $(buildir)/libriskengine.so

source = $(srcdir)/simulation.cpp
header = $(srcdir)/simulation.h


# this runs when "make" is executed

all :$(target)

$(target) : $(source) $(header)
	@mkdir -p $(buildir)
	@echo "Compiling Risk Engine..."
	$(CXX) $(CXXFLAGS) $(source) -o $(target)
	@echo "Compilation Successful"

clean :
	rm -f $(buildir)/*.so
	

