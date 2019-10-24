package koreatech.cse.repository;


import koreatech.cse.domain.H2member;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

@Repository
public interface H2memberMapper {
    @Insert("INSERT INTO h2member (NAME, PHONE, AGE) VALUES (#{name}, #{phone}, #{age})")
    void insert(H2member h2member);
}
