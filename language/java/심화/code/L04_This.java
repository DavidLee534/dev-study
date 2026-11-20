/*
 * [문법] this
 *
 * 실행: javac L04_This.java && java L04_This
 *
 * this = "이 객체 자신".
 * 매개변수 이름과 필드 이름이 같을 때 구분하려고 자주 쓴다.
 */
public class L04_This {

    public static void main(String[] args) {
        Member m = new Member("스키퍼");
        m.print();
    }
}

class Member {
    String name; // 필드

    Member(String name) { // 매개변수 name
        // this.name → 필드
        // name      → 매개변수
        this.name = name;
    }

    void print() {
        // 메서드 안에서도 this 로 자기 필드에 접근 가능
        System.out.println("이름: " + this.name);
    }
}
