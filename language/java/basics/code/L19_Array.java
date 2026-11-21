/*
 * [문법] 배열 — 선언, 생성, 인덱스, length
 *
 * 실행: javac L19_Array.java && java L19_Array
 *
 * 같은 타입 값을 한 줄로 담는 자료구조.
 * 인덱스는 0부터 시작한다.
 */
public class L19_Array {

    public static void main(String[] args) {
        // 선언 + 크기만큼 생성 (값은 숫자면 0으로 채워짐)
        int[] scores = new int[3];
        scores[0] = 90;
        scores[1] = 80;
        scores[2] = 70;

        // 선언과 동시에 값 넣기
        String[] names = {"스키퍼", "코왈스키", "프라이빗"};

        System.out.println("scores[0] = " + scores[0]);
        System.out.println("names[1] = " + names[1]);
        System.out.println("길이 length = " + names.length); // 3
        // names[3] 은 범위 밖 → ArrayIndexOutOfBoundsException
    }
}
