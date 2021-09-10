//
// Created by wizzzet on 10.09.2021.
//
#include <stdio.h>
#include <unistd.h>

const int ITERATIONS = 5;

int main () {
    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
        for (int i = 0; i < ITERATIONS; i++) {
            fork();
            printf("Created a child %i\n", i);
            sleep(5);
        }
    } else if (pid > 0) {
        printf("Parent %i\n", pid);
    } else {
        printf("Error in fork\n");
    }
    printf("Hello, World! I'm %i\n", pid);
    return 0;
}
