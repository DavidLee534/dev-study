/*
 * [문법] do-while 반복문
 *
 * 실행: javac L17_DoWhile.java && java L17_DoWhile
 *
 * do { ... } while (조건);
 * 조건을 나중에 검사하므로 블록은 최소 1번 실행된다.
 */
public class L17_DoWhile {

    public static void main(String[] args) {
        int n = 0;

        do {
            System.out.println("최소 1번은 실행 (n=" + n + ")");
            n++;
        } while (n < 0); // 처음부터 false 여도 위 블록은 이미 실행됨
    }
}
