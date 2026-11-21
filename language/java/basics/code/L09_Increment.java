/*
 * [문법] 증감 연산자 ++ / --
 *
 * 실행: javac L09_Increment.java && java L09_Increment
 *
 * x++  후위: 값을 쓴 뒤에 1 증가
 * ++x  전위: 먼저 1 증가한 뒤 사용
 */
public class L09_Increment {

    public static void main(String[] args) {
        int x = 5;

        System.out.println("x++ = " + (x++)); // 5 출력, 그다음 x=6
        System.out.println("지금 x = " + x);  // 6

        System.out.println("++x = " + (++x)); // 먼저 7로 만든 뒤 출력
        System.out.println("지금 x = " + x);  // 7

        x--; // 1 감소 → 6
        System.out.println("x-- 후 = " + x);
    }
}
