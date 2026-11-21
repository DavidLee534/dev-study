/*
 * [문법] 오버라이딩 (overriding)
 *
 * 실행: javac L08_Override.java && java L08_Override
 *
 * 부모 메서드를 자식이 같은 시그니처로 다시 정의하는 것.
 * @Override 를 붙이면 시그니처 실수를 컴파일러가 잡아 준다.
 *
 * 오버로딩(기초 L24): 같은 이름, 다른 매개변수
 * 오버라이딩(여기):   같은 이름+매개변수, 자식이 내용을 바꿈
 */
public class L08_Override {

    public static void main(String[] args) {
        Animal animal = new Animal();
        Animal dog = new DogAnimal(); // 부모 타입으로 담을 수 있음

        animal.sound(); // 동물이 소리를 낸다
        dog.sound();    // 멍멍!  ← 실제 객체(Dog)의 메서드가 호출됨
    }
}

class Animal {
    void sound() {
        System.out.println("동물이 소리를 낸다");
    }
}

class DogAnimal extends Animal {
    @Override
    void sound() {
        System.out.println("멍멍!");
    }
}
