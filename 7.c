#include <stdio.h>
int n, m, p[10], w[10];
void greedy_knapsack() {
    float profit = 0, ratio[10];
    int used[10] = {0};
    for (int i = 0; i < n; i++)
        ratio[i] = (float)p[i] / w[i];
    printf("Items included: ");
    while (m > 0) {
        int max = -1;
        for (int i = 0; i < n; i++)
            if (!used[i] && (max == -1 || ratio[i] > ratio[max]))
                max = i;
        if (w[max] <= m) {
            printf("%d ", max);
            m -= w[max];
            profit += p[max];
            used[max] = 1;
        } else {
            float frac = (float)m / w[max];
            profit += frac * p[max];
            printf("\nFraction of item %d taken: %.2f", max, frac);
            break;
        }
    }
    printf("\nTotal Profit = %.2f\n", profit);
}
int main() {
    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("Enter weights: ");
    for (int i = 0; i < n; i++) scanf("%d", &w[i]);
    printf("Enter prices: ");
    for (int i = 0; i < n; i++) scanf("%d", &p[i]);
    printf("Enter knapsack capacity: ");
    scanf("%d", &m);
    greedy_knapsack();
}