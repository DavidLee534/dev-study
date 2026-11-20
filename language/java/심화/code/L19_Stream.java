/*
 * [문법] Stream API
 *
 * 실행: javac L19_Stream.java && java L19_Stream
 *
 * 컬렉션을 파이프라인으로 가공한다.
 * filter(걸러내기) → map(변환) → forEach/toList(결과 모으기)
 */
import java.util.List;

public class L19_Stream {

    public static void main(String[] args) {
        List<Integer> nums = List.of(1, 2, 3, 4, 5, 6);

        // 짝수만 골라서 *10 한 뒤 리스트로
        List<Integer> result = nums.stream()
                .filter(n -> n % 2 == 0) // 2, 4, 6
                .map(n -> n * 10)        // 20, 40, 60
                .toList();

        System.out.println(result);

        // 출력만 할 때
        nums.stream()
                .filter(n -> n > 3)
                .forEach(n -> System.out.println("n=" + n));
    }
}
