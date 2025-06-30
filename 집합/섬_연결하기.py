# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[rb] = ra
        return True
    
    costs.sort(key=lambda x: x[2])
    
    total, picked = 0, 0
    
    # 크루스칼
    for a, b, c in costs:
        if union(a, b):
            total += c
            picked += 1
            if picked == n - 1:
                break
    
    return total



'''
•	모든 섬이 하나의 네트워크가 돼야 함(최소 신장 트리, MST)
    
1.	그래프 모델링
섬을 정점, 해저케이블을 간선(가중치 = 건설비)으로 보는 무향 가중 그래프.
2.	최소 신장 트리(MST)
트리 간선 수 = n - 1; 총 가중치가 최소인 스패닝 트리를 구해야 한다.
대표 알고리즘 ⇒ Kruskal(크루스칼) 또는 Prim(프림).
3.	Kruskal 선택 (간선 리스트가 이미 주어짐)
	1.	간선을 가중치 오름차순으로 정렬
	2.	사이클이 생기지 않는 선에서 차례로 채택—Disjoint-Set(Union-Find) 로 사이클 검사
	3.	간선 n-1개 고르면 종료
4.	복잡도
	•	정렬 O(E log E) ≈ 10 000 log 10 000
	•	Union-Find α(E)
	•	n ≤ 100이므로 충분히 빠름.


1.	간선 정렬
costs.sort(key=lambda x: x[2]) → 가장 싼 케이블부터 검토.
2.	Union-Find
  •	find(x) : 루트 정점 찾기(경로압축)
  •	union(a,b) : 두 집합 합치고, 이미 같으면 False 반환(사이클 발생)
3.	간선 채택
정렬된 리스트를 순회하며 union() 성공한 경우만 total += c.
4.	얼리 스톱
picked == n-1 이면 신장 트리 완성 → 루프 종료.


'''