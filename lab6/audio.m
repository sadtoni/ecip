%% Sound Clarification Task: 2-Machine Voice Enhancement
fs = 44100;         % Sampling frequency
duration = 5;       % Duration in seconds
threshold = 0.03;   % Noise gate threshold (adjust based on room noise)
alpha = 0.95;       % Pre-emphasis coefficient for clarity

% 1. CAPTURE: Initialize and record from Machine 2 microphone
recObj = audiorecorder(fs, 16, 1);
fprintf('Recording for %d seconds... Speak now on Machine 1.\n', duration);
recordblocking(recObj, duration);
fprintf('Recording complete. Processing...\n');
y = getaudiodata(recObj);

% 2. AMPLIFY: RMS Normalization
% Brings the distant voice to a standard volume level
targetRMS = 0.2;
currentRMS = sqrt(mean(y.^2));
if currentRMS > 0
    y_proc = y * (targetRMS / currentRMS);
else
    y_proc = y;
end

% 3. ENHANCE: Noise Gating & Pre-Emphasis
% We use a single loop to apply a high-pass filter (for crispness) 
% and a gate (to silence background noise)
y_final = zeros(size(y_proc));
for n = 2:length(y_proc)
    % High-pass filter (Pre-emphasis) to make speech less muffled
    y_final(n) = y_proc(n) - alpha * y_proc(n-1);

    % Noise Gate: If the signal is too quiet, assume it's background noise
    if abs(y_final(n)) < threshold
        y_final(n) = 0;
    end
end

% 4. SMOOTH: Simple 3-point Moving Average
% Reduces the "tinny" digital hiss created by the high-pass filter
y_smooth = y_final;
for n = 2:length(y_final)-1
    y_smooth(n) = (y_final(n-1) + y_final(n) + y_final(n+1)) / 3;
end

% 5. OUTPUT: Compare Original vs. Processed
disp('Playing Original Recording...');
sound(y, fs);
pause(duration + 1);

disp('Playing Enhanced Voice...');
sound(y_smooth, fs);

% Visual Comparison
subplot(2,1,1); plot(y); title('Original Signal (Machine 2 Input)');
subplot(2,1,2); plot(y_smooth); title('Enhanced Signal (Amplified & Clarified)');