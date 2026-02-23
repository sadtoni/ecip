#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    // Parameters
    const int time_steps = 50;
    double x = 0.0; // Initial state x(0)
    
    // Create and open a CSV file for plotting
    ofstream data_file("state_data.csv");
    
    if (!data_file.is_open()) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    // Write CSV Header
    data_file << "t,x_t" << endl;

    // Simulation loop
    for (int t = 0; t <= time_steps; ++t) {
        // Log current state to file
        data_file << t << "," << x << endl;
        
        // State transition: x(t+1) = x(t) + 1
        x = x + 1.0;
    }

    data_file.close();
    cout << "Success! Data for 50 steps saved to state_data.csv" << endl;

    return 0;
}