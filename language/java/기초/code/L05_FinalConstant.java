/*
 * [문법] final — 상수
 *
 * 실행: javac L05_FinalConstant.java && java L05_FinalConstant
 *
 * final 변수는 한 번 대입하면 다시 바꿀 수 없다.
 * 이름은 보통 대문자_스네이크 (관례)
 */
public class L05_FinalConstant {

    public static void main(String[] args) {
        final int MAX_SCORE = 100;

        // MAX_SCORE = 90;  // 주석 해제하면 컴파일 에러

        System.out.println("MAX_SCORE = " + MAX_SCORE);
    }
}
