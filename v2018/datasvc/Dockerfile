FROM java:8-jdk-alpine

ADD . /opt
WORKDIR /opt
RUN ./mvnw package

CMD ./mvnw spring-boot:run
