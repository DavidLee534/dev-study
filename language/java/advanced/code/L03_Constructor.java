/*
 * [문법] 생성자 (constructor)
 *
 * 실행: javac L03_Constructor.java && java L03_Constructor
 *
 * new 할 때 호출되는 특수 메서드. 이름을 클래스와 같게 쓰고 반환 타입이 없다.
 * 객체를 만들자마자 필드를 초기화할 때 쓴다.
 */
public class L03_Constructor {

    public static void main(String[] args) {
        // new Book(...) 할 때 생성자가 실행됨
        Book b = new Book("자바 기초", 15000);
        System.out.println(b.title + " / " + b.price + "원");
    }
}

class Book {
    String title;
    int price;

    // 생성자: 클래스 이름과 동일, 반환 타입 없음
    Book(String t, int p) {
        title = t;
        price = p;
    }
}
