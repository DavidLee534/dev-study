/*
 * [문법] record (Java 16+)
 *
 * 실행: javac L18_Record.java && java L18_Record
 *
 * 데이터만 담는 불변 객체를 짧게 만드는 문법.
 * 생성자, getter, equals, hashCode, toString 을 자동 생성한다.
 */
public class L18_Record {

    public static void main(String[] args) {
        Point p = new Point(3, 4);

        System.out.println(p);          // Point[x=3, y=4]
        System.out.println("x = " + p.x()); // getter 이름 = 필드명()
        System.out.println("y = " + p.y());

        Point same = new Point(3, 4);
        System.out.println("equals? " + p.equals(same)); // true
    }
}

// record 이름(필드...) { }
record Point(int x, int y) {
    // 필요하면 메서드 추가 가능
    double distanceFromOrigin() {
        return Math.sqrt(x * x + y * y);
    }
}
