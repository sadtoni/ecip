#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <numeric> // For accumulate

using namespace std;

int main() {
    const int time_steps = 50;
    const int window_size = 5;
    double x_true = 0.0;
    
    // Random setup for AWGN (mean 0, std dev 2)
    default_random_engine generator;
    normal_distribution<double> dist(0.0, 2.0);

    vector<double> observations;
    ofstream data_file("filter_results.csv");

    if (!data_file.is_open()) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    // CSV Header
    data_file << "t,True_State,Noisy_Observation,Estimated_State" << endl;

    for (int t = 0; t <= time_steps; ++t) {
        // 1. Generate True State and Noisy Observation
        double z_t = x_true + dist(generator);
        observations.push_back(z_t);

        // 2. Compute Moving Average Estimate
        double x_est = 0.0;
        if (observations.size() < window_size) {
            // If we don't have enough data yet, average what we have
            x_est = accumulate(observations.begin(), observations.end(), 0.0) / observations.size();
        } else {
            // Average the last 'window_size' elements
            x_est = accumulate(observations.end() - window_size, observations.end(), 0.0) / window_size;
        }

        // 3. Log data
        data_file << t << "," << x_true << "," << z_t << "," << x_est << endl;

        // 4. Update state for next step
        x_true += 1.0;
    }

    data_file.close();
    cout << "Success! Results saved to filter_results.csv" << endl;

    return 0;
}