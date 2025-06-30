# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    
    
    def dfs(sheeps, wolves):
        if sheeps > wolves:
            answer.append(sheeps)
        else:
            return
        
        for p, c in edges:
            # 부모는 방문하였지만 자식은 방문 안한 경우만 진행
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheeps + 1, wolves)
                else:
                    dfs(sheeps, wolves + 1)
                # 만약 다른 곳을 들렸다 방문 시 조건에 충족할 수 있어 false 처리
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
    
    return max(answer)