/*
 * [문법] 논리 연산자 && || !
 *
 * 실행: javac L11_Logical.java && java L11_Logical
 *
 * && AND : 둘 다 true 여야 true
 * || OR  : 하나라도 true 면 true
 * !  NOT : true↔false 뒤집기
 *
 * 단축 평가: 앞쪽에서 결과가 정해지면 뒤를 실행하지 않음
 */
public class L11_Logical {

    public static void main(String[] args) {
        boolean adult = true;
        boolean ticket = false;

        System.out.println("adult && ticket → " + (adult && ticket)); // false
        System.out.println("adult || ticket → " + (adult || ticket)); // true
        System.out.println("!ticket → " + (!ticket));                 // true

        // && 앞이 false 면 뒤(10/n)는 실행되지 않음 → 예외 없음
        int n = 0;
        boolean safe = (n != 0) && (10 / n > 1);
        System.out.println("단축 평가 safe → " + safe); // false
    }
}
