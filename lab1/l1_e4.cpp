#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <numeric>

using namespace std;

int main() {
    // 1. Setup Parameters
    const int time_steps = 50;
    const int window_size = 10; // Affects smoothing and lag
    double x_true = 0.0;        // Initial true state x(0)
    
    // 2. Random Number Generation for AWGN (Mean 0, Std Dev 2)
    default_random_engine generator;
    normal_distribution<double> noise_dist(0.0, 2.0);

    // 3. Data Storage
    vector<double> observations;
    ofstream data_file("analysis_results.csv");

    if (!data_file.is_open()) {
        cerr << "Error: Could not create data file." << endl;
        return 1;
    }

    // Write CSV Header for plotting
    data_file << "t,True_State,Observation,MA_Estimate" << endl;

    // 4. Simulation Loop
    for (int t = 0; t <= time_steps; ++t) {
        // Generate Noisy Observation: z(t) = x(t) + v(t)
        double z_t = x_true + noise_dist(generator);
        observations.push_back(z_t);

        // Compute Moving Average Estimate
        double x_est = 0.0;
        int current_size = observations.size();
        int start_idx = max(0, current_size - window_size);
        int count = current_size - start_idx;

        double sum = 0.0;
        for (int i = start_idx; i < current_size; ++i) {
            sum += observations[i];
        }
        x_est = sum / count;

        // Log Data: Time, True, Observation, Estimate
        data_file << t << "," << x_true << "," << z_t << "," << x_est << endl;

        // State Evolution: x(t+1) = x(t) + 1
        x_true += 1.0;
    }

    data_file.close();
    cout << "Simulation Finished. File 'analysis_results.csv' generated." << endl;

    return 0;
}