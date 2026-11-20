/*
 * [문법] throws / throw
 *
 * 실행: javac L16_Throws.java && java L16_Throws
 *
 * throw  : 예외를 직접 발생시킴
 * throws : 이 메서드가 예외를 밖으로 던질 수 있다고 표시
 *          → 호출한 쪽에서 try/catch 하거나 다시 throws
 */
public class L16_Throws {

    public static void main(String[] args) {
        try {
            int age = parseAge("abc"); // 숫자 아님 → 예외
            System.out.println(age);
        } catch (IllegalArgumentException e) {
            System.out.println("잡음: " + e.getMessage());
        }
    }

    // 이 메서드는 IllegalArgumentException 을 던질 수 있음
    static int parseAge(String text) throws IllegalArgumentException {
        try {
            return Integer.parseInt(text);
        } catch (NumberFormatException e) {
            // 새 예외로 바꿔서 던짐
            throw new IllegalArgumentException("나이가 숫자가 아님: " + text);
        }
    }
}
