/*
 * [문법] 컬렉션 List
 *
 * 실행: javac L12_List.java && java L12_List
 *
 * 배열과 비슷하지만 크기가 가변이다.
 * ArrayList 를 가장 많이 쓴다. (java.util 패키지)
 */
import java.util.ArrayList;
import java.util.List;

public class L12_List {

    public static void main(String[] args) {
        // <String> = 이 리스트에는 String 만 (제네릭, L13 에서 더 자세히)
        List<String> names = new ArrayList<>();

        names.add("스키퍼");
        names.add("코왈스키");
        names.add("프라이빗");

        System.out.println("크기 = " + names.size());
        System.out.println("0번 = " + names.get(0));

        names.remove("코왈스키");

        // for-each 로 순회
        for (String name : names) {
            System.out.println(name);
        }
    }
}
