/*
 * [문법] 매개변수 (parameter)
 *
 * 실행: javac L22_Parameters.java && java L22_Parameters
 *
 * 호출할 때 넘겨 주는 입력값.
 * 정의쪽 이름 = 매개변수, 호출때 넣는 값 = 인자(argument)
 */
public class L22_Parameters {

    public static void main(String[] args) {
        introduce("스키퍼", 25); // "스키퍼", 25 가 인자
        introduce("코왈스키", 30);
    }

    // name, age 가 매개변수
    static void introduce(String name, int age) {
        System.out.println(name + " / " + age + "세");
    }
}
