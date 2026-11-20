/*
 * [문법] return — 반환값
 *
 * 실행: javac L23_Return.java && java L23_Return
 *
 * 메서드가 결과를 돌려줄 때 사용.
 * 반환 타입을 void 대신 int, String 등으로 적는다.
 */
public class L23_Return {

    public static void main(String[] args) {
        int sum = add(3, 5); // 반환값 8을 sum 에 저장
        System.out.println("합 = " + sum);

        System.out.println("두 배 = " + doubleOf(7));
    }

    // 반환 타입 int. return 으로 값을 돌려줌
    static int add(int a, int b) {
        return a + b;
    }

    static int doubleOf(int n) {
        return n * 2;
        // return 아래 코드는 실행되지 않음
    }
}
