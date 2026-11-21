/*
 * [문법] for 반복문
 *
 * 실행: javac L15_ForLoop.java && java L15_ForLoop
 *
 * for (초기화; 조건; 증감) { ... }
 * 횟수가 정해져 있을 때 적합.
 */
public class L15_ForLoop {

    public static void main(String[] args) {
        // i=0 으로 시작 → i<5 인 동안 → 끝날 때마다 i++
        for (int i = 0; i < 5; i++) {
            System.out.println("i = " + i);
        }
        // 출력: 0 1 2 3 4
    }
}
