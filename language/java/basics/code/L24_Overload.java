/*
 * [문법] 메서드 오버로딩 (overloading)
 *
 * 실행: javac L24_Overload.java && java L24_Overload
 *
 * 같은 이름이지만 매개변수 개수/타입이 다르면 여러 개 정의 가능.
 * 반환 타입만 다른 것은 오버로딩이 아니다.
 */
public class L24_Overload {

    public static void main(String[] args) {
        System.out.println(add(1, 2));       // int, int
        System.out.println(add(1, 2, 3));    // int, int, int
        System.out.println(add(1.5, 2.5));   // double, double
    }

    static int add(int a, int b) {
        return a + b;
    }

    static int add(int a, int b, int c) {
        return a + b + c;
    }

    static double add(double a, double b) {
        return a + b;
    }
}
