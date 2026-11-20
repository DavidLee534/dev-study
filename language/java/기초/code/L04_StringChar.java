/*
 * [문법] char / String
 *
 * 실행: javac L04_StringChar.java && java L04_StringChar
 *
 * char   → 글자 하나, 작은따옴표 'A'
 * String → 문자열,   큰따옴표 "안녕"
 */
public class L04_StringChar {

    public static void main(String[] args) {
        char grade = 'A';           // 반드시 작은따옴표, 글자 하나
        // char wrong = "A";        // 컴파일 에러 (String 리터럴)

        String name = "스키퍼";       // 큰따옴표. String 은 클래스(참조 타입)
        String empty = "";          // 빈 문자열도 가능

        System.out.println("grade = " + grade);
        System.out.println("name = " + name);
        System.out.println("empty 길이 = " + empty.length());
    }
}
