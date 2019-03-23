drop database if exists airplane;
create database airplane default charset utf8;
use airplane;
create table data(
    id int auto_increment primary key,
    FlightNo varchar(16),
    FlightCompany varchar(16),
    FlightDeptimePlanDate varchar(32),
    FlightArrtimePlanDate varchar(32),
    CheckinTable varchar(32),
    BaggageID varchar(16),
    FlightDep varchar(16),
    FlightArr varchar(16),
    FlightDepAirport varchar(16),
    FlightArrAirport varchar(16),
    generic varchar(32),
    DepWeather varchar(32),
    ArrWeather varchar(32),
    distance int
);
alter table data add constraint pk_data_id primary key (id);