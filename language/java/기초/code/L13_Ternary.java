/*
 * [문법] 삼항 연산자 ? :
 *
 * 실행: javac L13_Ternary.java && java L13_Ternary
 *
 * 형태: 조건 ? 참일때값 : 거짓일때값
 * if/else 를 값 하나로 줄일 때 쓴다.
 */
public class L13_Ternary {

    public static void main(String[] args) {
        int score = 75;

        String result = score >= 60 ? "합격" : "불합격";
        System.out.println(result); // 합격
    }
}
