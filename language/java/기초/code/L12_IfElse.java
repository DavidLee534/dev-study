/*
 * [문법] if / else if / else
 *
 * 실행: javac L12_IfElse.java && java L12_IfElse
 *
 * 조건이 true 인 블록만 실행된다.
 */
public class L12_IfElse {

    public static void main(String[] args) {
        int score = 75;

        if (score >= 90) {
            System.out.println("등급: A");
        } else if (score >= 80) {
            System.out.println("등급: B");
        } else if (score >= 60) {
            System.out.println("등급: C"); // ← score=75 이라 여기
        } else {
            System.out.println("등급: F");
        }
    }
}
