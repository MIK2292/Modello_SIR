#include <iostream>
#include <fstream>
using namespace std;

void write_CSV(const string& filename, double** data, unsigned int len_data) {
	ofstream ofs("../data/" + filename);

	if (!ofs.is_open()) {
		cerr << "Failed to open file: " << filename << endl;
		return;
	}

	ofs << "S,I,R\n";

	// Write the data to the CSV file
	for (size_t i = 0; i < len_data; i++) {
		ofs << data[0][i] << "," << data[1][i] << "," << data[2][i];
		if (i < len_data - 1) {
			ofs << "\n"; // Add endl except for the last element
		}
	}

	ofs.close();
}


