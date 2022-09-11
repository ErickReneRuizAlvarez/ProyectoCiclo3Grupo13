use hpspg12_db;
insert into usuario values("pedrop","12345","enfermero","pedro","perez","2454523");
insert into usuario values("carlosg","67890","medico","carlos","gomez","7454523");
insert into usuario values("pedrogonz","67893","paciente","pedro","gonzalez","7854523");
insert into usuario values("rosarod","67894","paciente","rosa","rodriguez","6754523");
insert into usuario values("erickruiz","17894","familiar","erick","ruiz","6554523");
insert into usuario values("anaalv","97894","familiar","ana","alvar","6564523");

insert into personalsalud values("101","medico","cardiologia","carlosg");
insert into personalsalud values("102","enfermero","urologia","pedrop");

insert into paciente values(201, "Cr 7 12 23","bogota","1990-07-23",101,"pedrogonz");
insert into paciente values(202, "Cr 10 45 23","bogota","1997-07-30",101,"rosarod");

insert into familiar values(301, "hermano", "erickruiz@gmail.com","erickruiz",201);
insert into familiar values(302, "primo", "anaalv@gmail.com","anaalv",202);

insert into historiaclinica values(401, "hacer ejerc", "tension","entorno","2022-04-01","descrip",201);
insert into historiaclinica values(402, "hacer terap", "muscular","entorno2","2022-05-01","descrip2",202);

insert into signosvitales values(501,15,60,32,70,"120/80","2022-09-01",201);
insert into signosvitales values(502,17,65,30,75,"130/85","2022-09-02",202);

select * from usuario;
select * from personalsalud;
select * from paciente;
select * from familiar;
select * from historiaclinica;
select * from signosvitales;
