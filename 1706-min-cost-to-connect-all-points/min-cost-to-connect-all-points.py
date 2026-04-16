class Solution:
    def minCostConnectPoints(self, points):
        # Количество точек
        n = len(points)

        # Если точка одна, стоимость соединения равна 0
        if n <= 1:
            return 0

        # in_mst[i] = True, если точка уже включена в остов
        in_mst = [False] * n

        # min_dist[i] — минимальная стоимость подключения точки i к остову
        min_dist = [float('inf')] * n
        min_dist[0] = 0

        total_cost = 0

        for _ in range(n):
            # Ищем точку с минимальной стоимостью подключения
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            # Добавляем точку в остов
            in_mst[u] = True
            total_cost += min_dist[u]

            # Обновляем стоимости для оставшихся точек
            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return total_cost
