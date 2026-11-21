/*
 * [문법] Map — 키와 값
 *
 * 실행: javac L14_Map.java && java L14_Map
 *
 * 키(key)로 값(value)을 찾는다. 같은 키는 하나만.
 * HashMap 을 가장 많이 쓴다.
 */
import java.util.HashMap;
import java.util.Map;

public class L14_Map {

    public static void main(String[] args) {
        Map<String, Integer> ages = new HashMap<>();

        ages.put("스키퍼", 25);
        ages.put("코왈스키", 30);
        ages.put("스키퍼", 26); // 같은 키 → 값이 덮어써짐

        System.out.println("스키퍼 = " + ages.get("스키퍼")); // 26
        System.out.println("있음? " + ages.containsKey("코왈스키"));

        // 키 목록으로 순회
        for (String name : ages.keySet()) {
            System.out.println(name + " → " + ages.get(name));
        }
    }
}
