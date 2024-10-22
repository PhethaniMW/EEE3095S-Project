#include "CHeterodyning.h"
#include <stdio.h>
#include <stdlib.h>
#include <omp.h> // Include OpenMP for multi-threading

// Define these variables elsewhere or include a header
extern float data[SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT];
float result[SAMPLE_COUNT];

int main(int argc, char** argv) {
    printf("Running Optimized Test with Multi-Threading\n");
    printf("Precision sizeof %zu\n", sizeof(float));
    printf("Total amount of samples: %zu\n", SAMPLE_COUNT);

    // Set the number of threads - adjust based on your system
    int num_threads = 4;  // Adjust based on the number of cores on your machine
    omp_set_num_threads(num_threads);

    // Start the timer
    tic();

    // Efficiently parallelize the loop using OpenMP
    #pragma omp parallel for schedule(static)
    for (int i = 0; i < SAMPLE_COUNT; i++) {
        result[i] = data[i] * carrier[i];
    }

    // Stop the timer
    double t = toc();
    printf("Time: %lf ms\n", t);
    printf("End Optimized Test\n");

    return 0;
}
