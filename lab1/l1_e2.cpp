#include <iostream>
#include <vector>
#include <fstream>
#include <random> // Required for Gaussian noise

using namespace std;

int main() {
    // Parameters
    const int time_steps = 50;
    double x_true = 0.0;     // Initial true state
    const double mean = 0.0;
    const double std_dev = 2.0;

    // Random number setup
    default_random_engine generator;
    normal_distribution<double> noise(mean, std_dev);

    // File setup
    ofstream data_file("noisy_state.csv");
    if (!data_file.is_open()) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    // Header: True State vs Noisy Measurement
    data_file << "t,True_State,Noisy_Measurement" << endl;

    for (int t = 0; t <= time_steps; ++t) {
        // Generate noise for this step
        double v_t = noise(generator);
        double z_t = x_true + v_t;

        // Log both values
        data_file << t << "," << x_true << "," << z_t << endl;

        // Evolution of true state: x(t+1) = x(t) + 1
        x_true = x_true + 1.0;
    }

    data_file.close();
    cout << "Simulation complete. Data saved to noisy_state.csv" << endl;

    return 0;
}