/*
 * [문법] 비교 연산자 == != > >= < <=
 *
 * 실행: javac L10_Comparison.java && java L10_Comparison
 *
 * 결과는 항상 boolean (true / false)
 * == 는 비교, = 는 대입. 헷갈리지 말 것.
 */
public class L10_Comparison {

    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        System.out.println("a == b → " + (a == b)); // false
        System.out.println("a != b → " + (a != b)); // true
        System.out.println("a > b  → " + (a > b));  // true
        System.out.println("a >= 10 → " + (a >= 10)); // true
        System.out.println("a < b  → " + (a < b));  // false
        System.out.println("a <= 3 → " + (a <= 3)); // false
    }
}
