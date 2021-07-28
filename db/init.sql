CREATE DATABASE citiesData;
use citiesData;

/* CREATE TABLE */

CREATE TABLE IF NOT EXISTS tblCitiesImport (
    `id` int AUTO_INCREMENT,
    `fldMonth` VARCHAR(21) CHARACTER SET utf8,
    `fldAvg` NUMERIC(5,1),
    `fld2005` NUMERIC(5,1),
    `fld2006` NUMERIC(5,1),
    `fld2007` NUMERIC(5,1),
    `fld2008` NUMERIC(5,1),
    `fld2009` NUMERIC(5,1),
    `fld2010` NUMERIC(5,1),
    `fld2011` NUMERIC(5,1),
    `fld2012` NUMERIC(5,1),
    `fld2013` NUMERIC(5,1),
    `fld2014` NUMERIC(5,1),
    `fld2015` NUMERIC(5,1),
    PRIMARY KEY (`id`)
);
INSERT INTO tblCitiesImport (fldMonth,fldAvg,fld2005,fld2006,fld2007,fld2008,fld2009,fld2010,fld2011,fld2012,fld2013,fld2014,fld2015) VALUES
    ("May",0.1,0,0,1,1,0,0,0,2,0,0,0),
    ("Jun",0.5,2,1,1,0,0,1,1,2,2,0,1),
    ("Jul",0.7,5,1,1,2,0,1,3,0,2,2,1),
    ("Aug",2.3,6,3,2,4,4,4,7,8,2,2,3),
    ("Sep",3.5,6,4,7,4,2,8,5,2,5,2,5),
    ("Oct",2,8,0,1,3,2,5,1,5,2,3,0,1),
    ("Nov",0.5,3,0,0,1,1,0,1,0,1,0,1),
    ("Dec",0,1,0,1,0,0,0,0,0,0,0,1)






