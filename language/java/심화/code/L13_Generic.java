/*
 * [문법] 제네릭 (generic)
 *
 * 실행: javac L13_Generic.java && java L13_Generic
 *
 * 타입을 파라미터처럼 넘긴다. <T> 자리에 실제 타입을 넣어 쓴다.
 * 잘못된 타입을 컴파일 단계에서 막을 수 있다.
 */
public class L13_Generic {

    public static void main(String[] args) {
        Box<String> sBox = new Box<>();
        sBox.set("안녕");
        System.out.println(sBox.get());

        Box<Integer> iBox = new Box<>();
        iBox.set(42);
        System.out.println(iBox.get());

        // iBox.set("문자"); // Integer 박스에 String → 컴파일 에러
    }
}

// T = 타입 파라미터 (Type 의 T 관례)
class Box<T> {
    private T value;

    void set(T value) {
        this.value = value;
    }

    T get() {
        return value;
    }
}
