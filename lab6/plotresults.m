% 1. Define the data points from your screenshots
% Assuming standard gradual steps (e.g., 0.5m, 1m, 1.5m, 2m)
distances = [0.5, 1.0, 1.5, 2.0]; 
rms_values = [0.0070, 0.0065, 0.0034, 0.0020]; 

% 2. Create the plot
figure;
plot(distances, rms_values, '-ok', 'LineWidth', 2, 'MarkerFaceColor', 'r');
grid on;

% 3. Add labels and title
xlabel('Distance from Microphone (meters)');
ylabel('Original Signal Strength (RMS)');
title('Signal Decay over Distance');

% 4. Add annotations to show the data trend
text(distances, rms_values, string(rms_values), 'VerticalAlignment','bottom','HorizontalAlignment','right');

% 5. Logic check: Inverse Square Law
% Sound pressure typically follows an inverse relationship with distance.