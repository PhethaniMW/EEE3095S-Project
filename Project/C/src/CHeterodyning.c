#include "CHeterodyning.h"

extern float data[SAMPLE_COUNT];
extern float carrier[SAMPLE_COUNT];
float result[SAMPLE_COUNT] __attribute__((aligned(16)));  // Align for better memory access

int main(int argc, char**argv) {
    printf("Running Unthreaded Test\n");
    printf("Precision sizeof %ld\n", sizeof(float));
    
    printf("Total amount of samples: %ld\n", sizeof(data) / sizeof(data[0]));
    
    tic(); // start the timer
    
    // Tell compiler the arrays don't overlap and loop can be vectorized
    #pragma GCC ivdep
    for (int i = 0; i < SAMPLE_COUNT; i++) {
        result[i] = data[i] * carrier[i];
    }
    
    double t = toc();
    printf("Time: %lf ms\n", t/1e-3);
    printf("End Unthreaded Test\n");
    return 0;
}
