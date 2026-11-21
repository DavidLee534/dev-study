/*
 * [문법] 산술 연산자 + - * / %
 *
 * 실행: javac L08_Arithmetic.java && java L08_Arithmetic
 *
 * 정수 / 정수 → 소수점 버림. 실수 결과가 필요하면 double 로 나눈다.
 */
public class L08_Arithmetic {

    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        System.out.println("a + b = " + (a + b)); // 13
        System.out.println("a - b = " + (a - b)); // 7
        System.out.println("a * b = " + (a * b)); // 30
        System.out.println("a / b = " + (a / b)); // 3  ← 정수 나눗셈
        System.out.println("a % b = " + (a % b)); // 1  ← 나머지

        System.out.println("실수 나눗셈 = " + ((double) a / b)); // 3.333...

        // 대입과 연산을 합친 형태
        int score = 80;
        score += 10; // score = score + 10
        System.out.println("score = " + score); // 90
    }
}
