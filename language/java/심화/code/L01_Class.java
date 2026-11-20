/*
 * [문법] 클래스와 객체
 *
 * 실행: javac L01_Class.java && java L01_Class
 *
 * 클래스 = 설계도
 * 객체   = new 로 만든 실체 (인스턴스)
 */
public class L01_Class {

    public static void main(String[] args) {
        // new Person() → Person 설계도로 객체 생성
        Person p1 = new Person();
        Person p2 = new Person();

        // 객체마다 따로 존재한다
        p1.name = "스키퍼";
        p2.name = "코왈스키";

        System.out.println(p1.name); // 스키퍼
        System.out.println(p2.name); // 코왈스키
    }
}

// 같은 파일에 public 이 아닌 클래스를 추가로 둘 수 있다
class Person {
    String name; // 필드 (객체가 가지는 데이터)
}
