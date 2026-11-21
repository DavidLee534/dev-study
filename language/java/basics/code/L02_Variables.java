/*
 * [문법] 변수 — 값을 담는 이름
 *
 * 실행: javac L02_Variables.java && java L02_Variables
 *
 * 형태: 타입 이름 = 값;
 */
public class L02_Variables {

    public static void main(String[] args) {
        // 선언과 동시에 대입
        int age = 25;

        // 선언만 하고 나중에 대입
        int score;
        score = 90;

        // 같은 타입을 한 줄에
        int a = 1, b = 2;

        // 변수 값은 다시 바꿀 수 있다 (= 대입)
        age = 26;

        System.out.println("age = " + age);
        System.out.println("score = " + score);
        System.out.println("a = " + a + ", b = " + b);
    }
}
