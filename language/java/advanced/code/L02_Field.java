/*
 * [문법] 필드 (field)
 *
 * 실행: javac L02_Field.java && java L02_Field
 *
 * 클래스가 가지는 변수. 객체마다 값이 따로 저장된다.
 * 숫자를 안 넣으면 0, boolean 은 false, 참조는 null.
 */
public class L02_Field {

    public static void main(String[] args) {
        Dog d = new Dog();

        System.out.println("기본 age = " + d.age);     // 0
        System.out.println("기본 name = " + d.name);   // null

        d.name = "리코";
        d.age = 3;

        System.out.println(d.name + " / " + d.age + "살");
    }
}

class Dog {
    String name; // 참조 타입 기본값: null
    int age;     // 정수 기본값: 0
}
