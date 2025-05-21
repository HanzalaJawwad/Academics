#include <stdio.h>
#define INF 999
int n, cost[10][10], dist[10], visited[10];
void dijkstra(int src) {
    for (int i = 0; i < n; i++) dist[i] = cost[src][i], visited[i] = 0;
    dist[src] = 0; visited[src] = 1;

    for (int i = 1; i < n; i++) {
        int min = INF, u = -1;
        for (int j = 0; j < n; j++)
            if (!visited[j] && dist[j] < min) min = dist[j], u = j;
        if (u == -1) break;
        visited[u] = 1;
        for (int v = 0; v < n; v++)
            if (!visited[v] && cost[u][v] != INF && dist[u] + cost[u][v] < dist[v])
                dist[v] = dist[u] + cost[u][v];
    }
}
int main() {
    int src;
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter cost matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);

    printf("Enter source vertex: ");
    scanf("%d", &src);
    dijkstra(src);
    printf("Shortest distances from %d:\n", src);
    for (int i = 0; i < n; i++)
        printf("To %d: %d\n", i, dist[i]);
}