def solution(info, n, m):
    MAX = 120 + 12  # 최대 흔적 값 설정

    # DP 테이블 초기화 (A, B 흔적 가능 여부 저장)
    dp = [[False] * MAX for _ in range(MAX)]
    dp[0][0] = True  # 초기 상태 (아무것도 훔치지 않음)

    item_count = len(info)

    # 모든 물건에 대해 DP 갱신
    for traceA, traceB in info:
        next_dp = [[False] * MAX for _ in range(MAX)]

        for a in range(n):  # A 흔적 제한
            for b in range(m):  # B 흔적 제한
                if not dp[a][b]:
                    continue

                # A 도둑이 가져가는 경우
                if a + traceA < n:
                    next_dp[a + traceA][b] = True

                # B 도둑이 가져가는 경우
                if b + traceB < m:
                    next_dp[a][b + traceB] = True

        # DP 테이블 업데이트
        dp = [row[:] for row in next_dp]

    # 최소 A 도둑 흔적 찾기
    for a in range(n):
        for b in range(m):
            if dp[a][b]:  # 가능한 경우 발견
                return a

    return -1  # 불가능한 경우
