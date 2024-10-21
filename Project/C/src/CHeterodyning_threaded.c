#include "CHeterodyning.h"
#include <stdio.h>
#include <stdlib.h>
#include <omp.h> // Include OpenMP for multi-threading

extern float data[SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT];
float result[SAMPLE_COUNT];

int main(int argc, char** argv) {
    printf("Running Optimized Test with Multi-Threading\n");
    printf("Precision sizeof %ld\n", sizeof(float));
    printf("Total amount of samples: %ld\n", sizeof(data) / sizeof(data[0]));

    tic(); // Start the timer

    // Parallelize the loop using OpenMP for multi-threading
    #pragma omp parallel for
    for (int i = 0; i < SAMPLE_COUNT; i++) {
        result[i] = data[i] * carrier[i];
    }

    double t = toc(); // Stop the timer
    printf("Time: %lf ms\n", t / 1e-3);
    printf("End Optimized Test\n");

    return 0;
}
