#include <iostream>
#include <chrono>
#include "custom_io.hpp"
using namespace std;

void one_step_evolution(double Sn, double In, double Rn, 
		double& Snp1, double& Inp1, double& Rnp1,
		double gamma, double mu, double delta)
{
	//it should be \pm mu * (Sn * In)/N, ma abbiamo imposto N = 1
	Snp1 = Sn - mu * (Sn * In) + delta * In;
	Inp1 = In + mu * (Sn * In) - gamma * In;
	Rnp1 = Rn + gamma * In - delta * In;

	/*
	if ((Snp1 > 1) or (Rnp1 < 0)) 
	{
		Snp1 = Sn - mu * (Sn * In);
		Rnp1 = Rn + gamma * In;
	}
	*/ 
}

void evolve_system(double** SIR, unsigned int N_steps,
		double gamma, double mu, double delta)
{	
	for (int n = 0; n < N_steps-1; n++) 
		one_step_evolution(SIR[0][n],   SIR[1][n],   SIR[2][n],
				   SIR[0][n+1], SIR[1][n+1], SIR[2][n+1],
				   gamma, mu, delta);
}



int main(int argc, char* argv[]){

	// INITIALIZATION
	
	// Start time measurement
	auto start = chrono::high_resolution_clock::now();

	// Check if the user provided a command-line argument
	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " <float_value>" << endl;
		return 1;
	}

	// Convert the arguments to doubles and int
	double S0 = atof(argv[1]);
	double I0 = atof(argv[2]);
	double R0 = atof(argv[3]);
	double gamma = atof(argv[4]);
	double mu = atof(argv[5]);
	double delta = atof(argv[6]);
	unsigned int N_steps = atoi(argv[7]);
	
	// Generate dynamic array
	double** SIR = new double*[3];
	for (int i = 0; i < 3; i++)
		SIR[i] = new double[N_steps];
		
	double N = S0 + I0 + R0; 
	SIR[0][0] = S0/N;
	SIR[1][0] = I0/N;
	SIR[2][0] = R0/N;
	
	
	// CORE
	
	evolve_system(SIR, N_steps, gamma, mu, delta);
	
	write_CSV("SIR_" + to_string(gamma) + "_" + to_string(mu) + "_" + to_string(delta) + ".csv", SIR, N_steps);
	
	
	// END PROCEDURES
	
	cout << "Data written\n";
	
	// End time measurement
	auto end = std::chrono::high_resolution_clock::now();
	chrono::duration<double> elapsed = end - start;
	
	// Display the elapsed time in seconds
	cout << "Time elapsed: " << elapsed.count() << " seconds" << std::endl;
	
	return 0;
}
































