/*
 * [문법] enum — 열거 타입
 *
 * 실행: javac L17_Enum.java && java L17_Enum
 *
 * 미리 정해 둔 상수 묶음. 오타 나는 문자열 대신 타입으로 제한한다.
 */
public class L17_Enum {

    public static void main(String[] args) {
        Day today = Day.WED;

        System.out.println("오늘 = " + today);
        System.out.println("이름 = " + today.name());
        System.out.println("순서 = " + today.ordinal()); // 0부터

        // switch 와 잘 맞음
        String label = switch (today) {
            case MON, TUE, WED, THU, FRI -> "평일";
            case SAT, SUN -> "주말";
        };
        System.out.println(label);
    }
}

enum Day {
    MON, TUE, WED, THU, FRI, SAT, SUN
}
