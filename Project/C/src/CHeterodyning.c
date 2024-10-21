#include "CHeterodyning.h"
#include <stdio.h>

extern float data[SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT];
alignas(8) float result[SAMPLE_COUNT];  // Align for better memory access

void heterodyne_optimized() {
    // Process 4 elements at a time
    const int unrollFactor = 4;
    const int limit = SAMPLE_COUNT - (SAMPLE_COUNT % unrollFactor);
    
    // Hint to the compiler about no pointer aliasing
    float* __restrict__ r = result;
    const float* __restrict__ d = data;
    const float* __restrict__ c = carrier;
    
    // Main loop with manual unrolling
    #pragma GCC unroll 4
    for (int i = 0; i < limit; i += unrollFactor) {
        // Prefetch next chunks of data
        __builtin_prefetch(&d[i + 32], 0, 3);
        __builtin_prefetch(&c[i + 32], 0, 3);
        
        // Unrolled multiplication
        r[i] = d[i] * c[i];
        r[i + 1] = d[i + 1] * c[i + 1];
        r[i + 2] = d[i + 2] * c[i + 2];
        r[i + 3] = d[i + 3] * c[i + 3];
    }
    
    // Handle remaining elements
    for (int i = limit; i < SAMPLE_COUNT; i++) {
        r[i] = d[i] * c[i];
    }
}

int main(int argc, char **argv) {
    printf("Running Optimized Test\n");
    printf("Precision sizeof %ld\n", sizeof(float));
    printf("Total amount of samples: %d\n", SAMPLE_COUNT);
    
    tic();
    heterodyne_optimized();
    double t = toc();
    
    printf("Time: %lf ms\n", t/1e-3);
    printf("End Optimized Test\n");
    return 0;
}
