/*
 * [문법] main 메서드 — 프로그램 시작점
 *
 * 실행: javac L01_MainMethod.java && java L01_MainMethod
 *
 * 규칙:
 * - 파일명과 public class 이름이 같아야 한다 (L01_MainMethod.java)
 * - JVM은 public static void main(String[] args) 를 찾아 실행한다
 */
public class L01_MainMethod {

    // public  : JVM이 클래스 밖에서 호출할 수 있어야 함
    // static  : 객체 생성 없이 호출 가능
    // void    : 반환값 없음
    // args    : 실행 인자 (java L01_MainMethod a b → ["a","b"])
    public static void main(String[] args) {
        System.out.println("main 에서 시작됩니다");
        System.out.println("인자 개수: " + args.length);
    }
}
