/*
 * [문법] Set — 중복 없는 집합
 *
 * 실행: javac L15_Set.java && java L15_Set
 *
 * 같은 값은 한 번만 들어간다. 순서는 보장하지 않는다 (HashSet).
 */
import java.util.HashSet;
import java.util.Set;

public class L15_Set {

    public static void main(String[] args) {
        Set<String> tags = new HashSet<>();

        tags.add("java");
        tags.add("spring");
        tags.add("java"); // 중복 → 무시됨

        System.out.println("크기 = " + tags.size()); // 2
        System.out.println("포함? " + tags.contains("spring"));

        for (String tag : tags) {
            System.out.println(tag);
        }
    }
}
