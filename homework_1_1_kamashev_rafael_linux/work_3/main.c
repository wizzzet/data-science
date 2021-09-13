//
// Created by wizzzet on 10.09.2021.
//
#include <stdio.h>
#include <unistd.h>

int main () {
    FILE *fp;
    fp = fopen("result/example.txt", "w");
    fprintf(fp, "First line.\n");
    // fflush(fp);

    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
        fprintf(fp, "Сhild line.\n");
    } else if (pid > 0) {
        printf("Parent pid=%i\n", pid);
        fprintf(fp, "Parent line.\n");
    } else {
        printf("Error in fork\n");
    }
    printf("Hello, World! I'm pid=%i\n", pid);

    fclose(fp);
    return 0;
}
