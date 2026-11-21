/*
 * [문법] while 반복문
 *
 * 실행: javac L16_WhileLoop.java && java L16_WhileLoop
 *
 * while (조건) { ... }
 * 조건이 true 인 동안 반복. 조건을 false 로 바꾸는 코드가 필요.
 */
public class L16_WhileLoop {

    public static void main(String[] args) {
        int count = 3;

        while (count > 0) {
            System.out.println("count = " + count);
            count--; // 안 줄이면 무한 루프
        }
        // 출력: 3 2 1
    }
}
