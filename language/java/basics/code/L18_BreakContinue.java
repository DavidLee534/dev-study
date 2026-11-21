/*
 * [문법] break / continue
 *
 * 실행: javac L18_BreakContinue.java && java L18_BreakContinue
 *
 * break    : 반복 전체를 즉시 종료
 * continue : 이번 회차만 건너뛰고 다음으로
 */
public class L18_BreakContinue {

    public static void main(String[] args) {
        System.out.print("결과: ");

        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                break; // 5에서 반복 종료 → 이후 숫자 출력 안 함
            }
            if (i % 2 == 0) {
                continue; // 짝수는 건너뜀
            }
            System.out.print(i + " "); // 1 3
        }

        System.out.println();
    }
}
