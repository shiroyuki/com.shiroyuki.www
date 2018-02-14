package com.shiroyuki.www.injector;

import java.util.Date;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

import com.shiroyuki.www.model.Page;

@Aspect
@Component
public class LastLoadedAtInjector {
    // NOTE https://www.mkyong.com/spring3/spring-aop-aspectj-annotation-example/
    @AfterReturning(
            pointcut = "execution(* com.shiroyuki.www.repository.PageRepository.get(..))",
            returning = "result"
    )
    public void inject(JoinPoint joinPoint, Object result) {
        Page page = (Page) result;
        page.setLastLoadedAt(new Date());
    }
}
