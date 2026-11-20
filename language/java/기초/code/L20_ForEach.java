/*
 * [문법] 향상된 for (for-each) — 배열 전체 순회
 *
 * 실행: javac L20_ForEach.java && java L20_ForEach
 *
 * for (타입 변수 : 배열) { ... }
 * 인덱스가 필요 없을 때 쓴다. 인덱스가 필요하면 일반 for.
 */
public class L20_ForEach {

    public static void main(String[] args) {
        int[] nums = {10, 20, 30};

        // for-each: 각 원소를 n 에 담아 반복
        for (int n : nums) {
            System.out.println(n);
        }

        // 인덱스가 필요하면 일반 for
        for (int i = 0; i < nums.length; i++) {
            System.out.println("nums[" + i + "] = " + nums[i]);
        }
    }
}
