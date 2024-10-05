#!/bin/bash

# Measure runtime of a command
start_time=$(date +%s)

work(){
	cd cpp

	echo "Compiling..."
	g++ -o CORE SIR.cpp

	echo "Running..."
	./CORE 59999999 1 0 $gamma $mu $delta 150

	cd ../python
	echo "Generating plots..."
	python3 generate_plots.py $gamma $mu $delta

	cd ..
}

#choose parameters
gamma=0.25
mu=0.7
delta=0.0
work

gamma=0.25
mu=0.7
delta=0.125
work

gamma=0.25
mu=0.7
delta=0.225
work

gamma=0.25
mu=0.7
delta=0.25
work

end_time=$(date +%s)
runtime=$((end_time - start_time))

echo "Done in ${runtime} seconds"

