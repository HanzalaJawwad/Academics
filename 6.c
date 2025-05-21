#include <stdio.h>
int n, m, p[10], w[10], V[10][10];
int max(int a, int b) { return a > b ? a : b; }
void knapsack() {
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            V[i][j] = (i == 0 || j == 0) ? 0 :
                      (w[i] > j ? V[i-1][j] : max(V[i-1][j], p[i] + V[i-1][j - w[i]]));
    for (int i = 0; i <= n; i++, printf("\n"))
        for (int j = 0; j <= m; j++)
            printf("%d ", V[i][j]);
    printf("Items included: ");
    for (int i = n, j = m; i > 0; i--)
        if (V[i][j] != V[i-1][j]) {
            printf("%d ", i);
            j -= w[i];
        }
}
int main() {
    printf("Enter no. of items: ");
    scanf("%d", &n);
    printf("Enter weights: ");
    for (int i = 1; i <= n; i++) scanf("%d", &w[i]);
    printf("Enter prices: ");
    for (int i = 1; i <= n; i++) scanf("%d", &p[i]);
    printf("Enter knapsack capacity: ");
    scanf("%d", &m);
    knapsack();
}