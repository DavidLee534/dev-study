/*
 * [문법] 예외 처리 try / catch / finally
 *
 * 실행: javac L11_Exception.java && java L11_Exception
 *
 * 예외가 나면 프로그램이 죽을 수 있다.
 * try 에서 시도 → catch 에서 잡음 → finally 는 항상 실행.
 */
public class L11_Exception {

    public static void main(String[] args) {
        // 1) 배열 범위 초과
        try {
            int[] nums = {1, 2, 3};
            System.out.println(nums[10]); // 예외 발생
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("인덱스 오류: " + e.getMessage());
        }

        // 2) 0 으로 나누기
        try {
            int result = 10 / 0;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("연산 오류: 0으로 나눌 수 없음");
        } finally {
            System.out.println("finally: 예외 여부와 관계없이 실행");
        }

        System.out.println("프로그램 계속 진행");
    }
}
