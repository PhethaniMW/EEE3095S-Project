.RECIPEPREFIX +=
CC = arm-linux-gnueabihf-g++
OPTFLAGS = -march=armv6 -mfpu=vfp -mfloat-abi=hard -ffast-math -mfp16-format=ieee -O2
CFLAGS = $(OPTFLAGS) -lm -lrt
INCLUDE = -ITools
PROG = bin/*
OBJS = obj/*

default: standard threaded

standard:
    mkdir -p bin obj
    $(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning.c -o obj/CHeterodyning.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/CHeterodyning obj/CHeterodyning.o obj/Timer.o $(CFLAGS)

threaded:
    mkdir -p bin obj
    $(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning_threaded.c -o obj/CHeterodyning_threaded.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/CHeterodyning_threaded obj/CHeterodyning_threaded.o obj/Timer.o $(CFLAGS) -pthread

run:
    bin/CHeterodyning

run_threaded:
    bin/CHeterodyning_threaded
    
clean: 
    rm -rf $(PROG) $(OBJS)
