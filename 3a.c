#include <stdio.h>

void floyd(int d[10][10], int n) {
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (d[i][k] + d[k][j] < d[i][j])
                    d[i][j] = d[i][k] + d[k][j];
}

int main() {
    int n, cost[10][10];
    printf("Enter no. of Vertices: ");
    scanf("%d", &n);
    printf("Enter the cost matrix:\n");
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            scanf("%d", &cost[i][j]);

    floyd(cost, n);

    printf("All pair shortest path:\n");
    for (int i = 1; i <= n; i++, printf("\n"))
        for (int j = 1; j <= n; j++)
            printf("%d ", cost[i][j]);
}
