/*
 * [문법] 메서드 — 정의와 호출
 *
 * 실행: javac L21_Method.java && java L21_Method
 *
 * 반복되는 코드를 묶어 이름 붙인 것.
 * 형태: 반환타입 이름(매개변수) { ... }
 */
public class L21_Method {

    public static void main(String[] args) {
        // 메서드 호출
        greet();
        greet();
    }

    // void = 반환값 없음
    // static = main 처럼 객체 없이 호출 (지금은 이 형태만 사용)
    static void greet() {
        System.out.println("안녕하세요");
    }
}
