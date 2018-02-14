FROM java:8-jdk-alpine

ENV APP_USER app
ENV APP_PATH /opt/app
ENV STATIC_PAGE_DATA_PATH /opt/data/static/pages/en

# As root
RUN adduser -h ${APP_PATH} -s nologin -D -H ${APP_USER}
ADD . ${APP_PATH}
WORKDIR ${APP_PATH}
RUN chown -Rf ${APP_USER} .

# As non-privileged user
USER ${APP_USER}
RUN ./mvnw package

CMD ./mvnw spring-boot:run
