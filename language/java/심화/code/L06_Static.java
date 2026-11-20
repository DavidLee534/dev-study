/*
 * [문법] static
 *
 * 실행: javac L06_Static.java && java L06_Static
 *
 * static 멤버는 객체가 아니라 클래스에 속한다.
 * 객체 없이 클래스이름.멤버 로 접근한다.
 * 모든 객체가 값을 공유한다.
 */
public class L06_Static {

    public static void main(String[] args) {
        // static 메서드: 객체 없이 호출
        System.out.println(MathUtil.square(5)); // 25

        Counter a = new Counter();
        Counter b = new Counter();
        // count 는 static → a, b 가 하나를 공유
        System.out.println("생성된 수 = " + Counter.count); // 2
    }
}

class MathUtil {
    // 객체 상태와 무관한 기능 → static
    static int square(int n) {
        return n * n;
    }
}

class Counter {
    static int count = 0; // 클래스 공유 변수

    Counter() {
        count++; // 객체가 만들어질 때마다 증가
    }
}
