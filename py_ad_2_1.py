"""
Section 2
Parallelism with Multiprocessing - Process vs Thread, Parallelism

Keyword - Process, Thread, 병렬성

"""
"""

(1).Parallelism
    - 완전히 동일한 타이밍(시점)에 태스크 실행
    - 다양한 파트(부분)으로 나눠서 실행(합 나눠서 구하고 취합)
    - 멀티프로세싱에서 CPU가 1Core 인 경우 만족하지 않음
    - 딥러닝, 비트코인 채굴 등

(2).Process vs Thread(차이 비교(중요))
    - 독립된 메모리(프로세스), 공유메모리(스레드)
    - 많은 메모리 필요(프로세스), 적은 메모리(스레드)
    - 좀비(데드)프로세스 생성 가능성, 좀비(데드) 스레드 생성 쉽지 않음
    - 오버헤드 큼(프로세스), 오버헤드 작음(스레드)
    - 생성/소멸 다소 느림(프로세스), 생성/소멸 빠름(스레드)
    - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드작성 어려움/디버깅 어려움(스레드)

"""