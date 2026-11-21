/*
 * [문법] 추상 클래스 (abstract class)
 *
 * 실행: javac L09_Abstract.java && java L09_Abstract
 *
 * abstract 클래스: new 로 직접 만들 수 없다. 자식이 상속해서 쓴다.
 * abstract 메서드: 몸통({}) 없이 선언만. 자식이 반드시 구현한다.
 */
public class L09_Abstract {

    public static void main(String[] args) {
        // Shape s = new Shape(); // 추상 클래스라 컴파일 에러
        Shape c = new Circle(2);
        Shape r = new Rect(3, 4);

        System.out.println("원 넓이 = " + c.area());
        System.out.println("사각형 넓이 = " + r.area());
    }
}

abstract class Shape {
    // 공통 메서드는 일반 메서드로 둘 수 있다
    void info() {
        System.out.println("도형입니다");
    }

    // 자식마다 달라지는 부분 → abstract
    abstract double area();
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return 3.14 * radius * radius;
    }
}

class Rect extends Shape {
    double w, h;

    Rect(double w, double h) {
        this.w = w;
        this.h = h;
    }

    @Override
    double area() {
        return w * h;
    }
}
