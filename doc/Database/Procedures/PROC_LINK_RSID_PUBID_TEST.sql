insert into public.gt_file
values('123', '2022-01-01'),
('124', '2022-01-01')

insert into public.gt_file_data
values('123', 1, 'aa', 69, 'lo'),
('124', 2, 'aa', 69, 'lo')

insert into public.article
values(1, 123, 'aa', 69, 'lo', 2017, 'kut', 'leipe score'),
(2, 123, 'aa', 69, 'lo', 2017, 'kut', 'leipe score')

insert into public.id_search
values(1, '2022-01-01'),
(2, '2022-01-01')


select * from gt_file
select * from gt_file_data

delete from gt_file_data



call PROC_LINK_RSID_PUBID('{1, 2}', '{1, 2}')



DROP PROCEDURE proc_link_rsid_pubid(text[],text[])