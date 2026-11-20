package demo;

import java.util.List;

/**
 * 학습용 예시: 연관 엔티티를 한 번에 조회하는 fetch join 스케치
 */
public class MenuService {

    // 실제 프로젝트에서는 EntityManager / Repository를 사용합니다.
    public List<Object> findMenusWithCategory() {
        String jpql = """
            select m
            from Menu m
            join fetch m.category
            where m.status = 'ACTIVE'
            """;
        // em.createQuery(jpql, Menu.class).getResultList();
        return List.of();
    }
}
