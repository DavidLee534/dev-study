/*
 * [문법] 콘솔 출력
 *
 * 실행: javac L07_Output.java && java L07_Output
 *
 * println : 출력 후 줄바꿈
 * print   : 줄바꿈 없음
 * printf  : 포맷 문자열 (%s %d %.1f %n)
 */
public class L07_Output {

    public static void main(String[] args) {
        System.out.println("줄바꿈 있는 출력");

        System.out.print("이어");
        System.out.print("쓰기");
        System.out.println(); // 줄바꿈만

        String name = "스키퍼";
        int age = 25;
        // %s 문자열, %d 정수, %.1f 소수 1자리, %n 줄바꿈
        System.out.printf("이름=%s, 나이=%d%n", name, age);
    }
}
