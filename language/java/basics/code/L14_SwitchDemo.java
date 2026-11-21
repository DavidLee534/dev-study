/*
 * [문법] switch
 *
 * 실행: javac L14_SwitchDemo.java && java L14_SwitchDemo
 *
 * 값에 따라 분기. Java 14+ 화살표(->) 문법은 case 마다 break 불필요.
 */
public class L14_SwitchDemo {

    public static void main(String[] args) {
        int day = 3;

        // 문장 형태: 각 case 에서 동작 수행
        switch (day) {
            case 1 -> System.out.println("월요일");
            case 2 -> System.out.println("화요일");
            case 3 -> System.out.println("수요일");
            default -> System.out.println("그 외");
        }

        // 표현식 형태: switch 결과가 값이 됨
        String name = switch (day) {
            case 1 -> "월";
            case 2 -> "화";
            case 3 -> "수";
            default -> "기타";
        };
        System.out.println("약자: " + name);
    }
}
