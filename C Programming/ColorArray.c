#include <stdio.h>
#include <stdlib.h>

int main() {
    system("color 0B");
    int rows = 3, cols = 3;
    int arr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    printf("\n--- Matrix with Colours ---\n");
    for (int i = 0; i < rows; i++) {
        printf("| ");
        for (int j = 0; j < cols; j++) {
            if (arr[i][j] % 2 == 0)
                printf("\033[1;34m%4d\033[0m ", arr[i][j]); // Blue for even
            else
                printf("\033[1;32m%4d\033[0m ", arr[i][j]); // Green for odd
        }
        printf("|\n");
    }

    return 0;
}
