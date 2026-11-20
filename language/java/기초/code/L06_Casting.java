/*
 * [문법] 형변환 (casting)
 *
 * 실행: javac L06_Casting.java && java L06_Casting
 *
 * 작은 → 큰 : 자동 (안전)
 * 큰 → 작은 : (타입) 강제. 값이 잘릴 수 있음
 */
public class L06_Casting {

    public static void main(String[] args) {
        int n = 10;
        long wide = n;              // int → long 자동

        double raw = 9.8;
        int truncated = (int) raw;  // 강제. 9 (소수점 버림, 반올림 아님)

        System.out.println("wide = " + wide);
        System.out.println("truncated = " + truncated);
    }
}
