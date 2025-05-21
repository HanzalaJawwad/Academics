#include <stdio.h>

void warshall(int a[10][10], int n) {
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                a[i][j] |= a[i][k] && a[k][j];
}

int main() {
    int n, a[10][10];
    printf("Enter no. of Vertices: ");
    scanf("%d", &n);
    printf("Enter the adjacency matrix:\n");
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            scanf("%d", &a[i][j]);

    warshall(a, n);

    printf("Transitive closure:\n");
    for (int i = 1; i <= n; i++, printf("\n"))
        for (int j = 1; j <= n; j++)
            printf("%d ", a[i][j]);
}
