/*
 * [문법] 접근 제어자 (access modifier)
 *
 * 실행: javac L05_AccessModifier.java && java L05_AccessModifier
 *
 * public    : 어디서든 접근 가능
 * private   : 같은 클래스 안에서만
 * (생략)    : 같은 패키지 (default)
 * protected : 같은 패키지 + 자식 클래스 (상속 때 다시)
 *
 * 필드는 보통 private 으로 숨기고, 메서드로 읽고 쓴다.
 */
public class L05_AccessModifier {

    public static void main(String[] args) {
        BankAccount acc = new BankAccount();
        acc.deposit(1000);
        // acc.balance = 99999; // private 이라 밖에서 직접 수정 불가 (컴파일 에러)
        System.out.println("잔액 = " + acc.getBalance());
    }
}

class BankAccount {
    private int balance; // 외부에서 직접 못 건드림

    public void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public int getBalance() {
        return balance;
    }
}
