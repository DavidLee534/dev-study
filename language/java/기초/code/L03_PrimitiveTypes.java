/*
 * [문법] 원시 타입 (primitive)
 *
 * 실행: javac L03_PrimitiveTypes.java && java L03_PrimitiveTypes
 *
 * 자주 쓰는 것: int, long, double, boolean
 */
public class L03_PrimitiveTypes {

    public static void main(String[] args) {
        // 정수 — 기본은 int. 더 크면 long (끝에 L)
        byte small = 100;           // 1바이트
        short medium = 30000;       // 2바이트
        int count = 42;             // 4바이트 (정수 기본)
        long big = 3_000_000_000L;  // 8바이트. _ 는 가독용

        // 실수 — 기본은 double. float 은 끝에 f
        float ratio = 3.14f;        // 4바이트
        double height = 175.5;      // 8바이트 (실수 기본)

        // 논리
        boolean ok = true;          // true 또는 false 만

        System.out.println("byte=" + small + ", short=" + medium);
        System.out.println("int=" + count + ", long=" + big);
        System.out.println("float=" + ratio + ", double=" + height);
        System.out.println("boolean=" + ok);
    }
}
