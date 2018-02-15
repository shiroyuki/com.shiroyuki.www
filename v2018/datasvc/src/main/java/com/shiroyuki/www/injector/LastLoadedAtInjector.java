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
    @AfterReturning(
            pointcut = "execution(* com.shiroyuki.www.repository.PageRepository.getEnglish(..))",
            returning = "result"
    )
    public void interceptEnglishPage(JoinPoint joinPoint, Object result) {
        Page page = (Page) result;
        page.setLastLoadedAt(new Date());
    }

    @AfterReturning(
            pointcut = "execution(* com.shiroyuki.www.repository.PageRepository.getJapanese(..))",
            returning = "result"
    )
    public void interceptJapanesePage(JoinPoint joinPoint, Object result) {
        Page page = (Page) result;
        page.setLastLoadedAt(new Date());
    }
}
