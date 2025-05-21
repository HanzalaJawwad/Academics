#include <stdio.h>
int n, cost[10][10], colsum[10], select[10] = {0};
void cal_colsum() {
    for (int j = 0; j < n; j++) {
        colsum[j] = 0;
        for (int i = 0; i < n; i++)
            colsum[j] += cost[i][j];
    }
}
void source_removal() {
    printf("Topological ordering: ");
    for (int i = 0; i < n; i++) {
        cal_colsum();
        for (int j = 0; j < n; j++) {
            if (!select[j] && colsum[j] == 0) {
                printf("%d ", j);
                select[j] = 1;
                for (int k = 0; k < n; k++)
                    cost[j][k] = 0;
                break;
            }
        }
    }
}
int main() {
    printf("Enter no. of vertices: ");
    scanf("%d", &n);
    printf("Enter the cost matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);
    source_removal();
}