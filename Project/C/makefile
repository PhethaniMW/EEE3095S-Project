RECIPEPREFIX += 

CC = arm-linux-gnueabihf-g++
CFLAGS = -O2 -lm -lrt
CFLAGS += -mfp16-format=ieee
CFLAGS += -ftree-vectorize
CFLAGS += -ffast-math
CFLAGS += -march=native
CFLAGS += -funroll-loops
INCLUDE = -ITools

PROG = bin/*
OBJS = obj/*

default:
	mkdir -p bin obj
	$(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning.c -o obj/CHeterodyning.o
	$(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
	$(CC) -o bin/CHeterodyning obj/CHeterodyning.o obj/Timer.o $(CFLAGS)

threaded:
	mkdir -p bin obj
	$(CC) $(INCLUDE) $(CFLAGS) -c src/CHeterodyning_threaded.c -o obj/CHeterodyning_threaded.o
	$(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
	$(CC) -o bin/CHeterodyning_threaded obj/CHeterodyning_threaded.o obj/Timer.o $(CFLAGS)

run:
	bin/CHeterodyning; \

run_threaded:
	bin/CHeterodyning_threaded; \

clean:
	rm -rf $(PROG) $(OBJS)
