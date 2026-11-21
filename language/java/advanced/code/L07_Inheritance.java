/*
 * [문법] 상속 (extends)
 *
 * 실행: javac L07_Inheritance.java && java L07_Inheritance
 *
 * 자식 클래스가 부모의 필드·메서드를 물려받는다.
 * 자바는 클래스 단일 상속만 가능 (부모 하나).
 */
public class L07_Inheritance {

    public static void main(String[] args) {
        Student s = new Student();
        s.name = "스키퍼";      // Person 에게서 물려받음
        s.grade = 3;          // Student 고유
        s.introduce();        // Person 메서드
        s.study();            // Student 메서드
    }
}

class PersonBase {
    String name;

    void introduce() {
        System.out.println("안녕하세요, " + name + "입니다");
    }
}

// extends = PersonBase 를 부모로
class Student extends PersonBase {
    int grade;

    void study() {
        System.out.println(name + " 학생이 공부합니다 (학년 " + grade + ")");
    }
}
