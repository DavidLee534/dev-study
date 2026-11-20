/*
 * [문법] 인터페이스 (interface)
 *
 * 실행: javac L10_Interface.java && java L10_Interface
 *
 * 구현해야 할 메서드 규약. 클래스는 implements 로 여러 개 구현 가능.
 * (상속 extends 는 부모 하나, 인터페이스는 여러 개)
 */
public class L10_Interface {

    public static void main(String[] args) {
        Printable doc = new Document("회의록");
        doc.print();

        // 여러 인터페이스를 구현한 객체
        SmartPhone phone = new SmartPhone();
        phone.play();
        phone.shoot();
    }
}

interface Printable {
    void print(); // public abstract 가 생략된 형태
}

class Document implements Printable {
    String title;

    Document(String title) {
        this.title = title;
    }

    @Override
    public void print() {
        System.out.println("인쇄: " + title);
    }
}

interface Playable {
    void play();
}

interface Camera {
    void shoot();
}

// 인터페이스는 콤마로 여러 개 implements 가능
class SmartPhone implements Playable, Camera {
    @Override
    public void play() {
        System.out.println("음악 재생");
    }

    @Override
    public void shoot() {
        System.out.println("사진 촬영");
    }
}
