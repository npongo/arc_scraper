USE master
GO

IF DB_ID('Indonesia_menlhk') IS NULL CREATE DATABASE Indonesia_menlhk
GO
USE [Indonesia_menlhk]
GO

IF SCHEMA_ID('Hosted') IS NULL EXEC('CREATE SCHEMA [Hosted]')
GO

IF SCHEMA_ID('KLHK') IS NULL EXEC('CREATE SCHEMA [KLHK]')
GO

IF SCHEMA_ID('KLHK_EN') IS NULL EXEC('CREATE SCHEMA [KLHK_EN]')
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKRE_kode_prov]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKRE_kode_prov]
GO

CREATE TABLE [KLHK_EN].[IUPHHKRE_kode_prov] (
[Code] int NOT NULL PRIMARY KEY,
[Name] nvarchar(23) NOT NULL
)
GO

INSERT INTO[KLHK_EN].[IUPHHKRE_kode_prov]([Code], [Name])VALUES
('0', 'Belum Terdevinisi'),
('11', 'Nangroe Aceh Darussalam'),
('12', 'Sumatera Utara'),
('13', 'Sumatera Barat'),
('14', 'Riau'),
('15', 'Jambi'),
('16', 'Sumatera Selatan'),
('17', 'Bengkulu'),
('18', 'Lampung'),
('19', 'Kep. Bangka Belitung'),
('20', 'Kep. Riau'),
('31', 'DKI Jakarta'),
('32', 'Jawa Barat'),
('33', 'Jawa Tengah'),
('34', 'DI Jogjakarta'),
('35', 'Jawa Timur'),
('36', 'Banten'),
('51', 'Bali'),
('52', 'Nusa Tenggara Barat'),
('53', 'Nusa Tenggara Timur'),
('61', 'Kalimantan Barat'),
('62', 'Kalimantan Tengah'),
('63', 'Kalimantan Selatan'),
('64', 'Kalimantan Timur'),
('71', 'Sulawesi Utara'),
('72', 'Sulawesi Tengah'),
('73', 'Sulawesi Selatan'),
('74', 'Sulawesi Tenggara'),
('75', 'Gorontalo'),
('76', 'Sulawesi Barat'),
('81', 'Maluku'),
('82', 'Maluku Utara'),
('91', 'Papua Barat'),
('92', 'Papua')
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKRE_stat_prshn]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKRE_stat_prshn]
GO

CREATE TABLE [KLHK_EN].[IUPHHKRE_stat_prshn] (
[Code] varchar(11) NOT NULL PRIMARY KEY,
[Name] nvarchar(11) NOT NULL
)
GO

INSERT INTO[KLHK_EN].[IUPHHKRE_stat_prshn]([Code], [Name])VALUES
('Aktif', 'Aktif'),
('Tidak Aktif', 'Tidak Aktif')
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKRE_stat_milik]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKRE_stat_milik]
GO

CREATE TABLE [KLHK_EN].[IUPHHKRE_stat_milik] (
[Code] varchar(16) NOT NULL PRIMARY KEY,
[Name] nvarchar(16) NOT NULL
)
GO

INSERT INTO[KLHK_EN].[IUPHHKRE_stat_milik]([Code], [Name])VALUES
('Swasta', 'Swasta'),
('Penyertaan Saham', 'Penyertaan Saham')
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKRE_sertifikasi_lpi]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKRE_sertifikasi_lpi]
GO

CREATE TABLE [KLHK_EN].[IUPHHKRE_sertifikasi_lpi] (
[Code] varchar(9) NOT NULL PRIMARY KEY,
[Name] nvarchar(9) NOT NULL
)
GO

INSERT INTO[KLHK_EN].[IUPHHKRE_sertifikasi_lpi]([Code], [Name])VALUES
('Ada', 'Ada'),
('Tidak Ada', 'Tidak Ada')
GO

IF SCHEMA_ID('Latihan') IS NULL EXEC('CREATE SCHEMA [Latihan]')
GO

IF SCHEMA_ID('Other') IS NULL EXEC('CREATE SCHEMA [Other]')
GO

IF SCHEMA_ID('Publik') IS NULL EXEC('CREATE SCHEMA [Publik]')
GO

IF SCHEMA_ID('SINAV') IS NULL EXEC('CREATE SCHEMA [SINAV]')
GO

IF SCHEMA_ID('test') IS NULL EXEC('CREATE SCHEMA [test]')
GO

IF SCHEMA_ID('Utilities') IS NULL EXEC('CREATE SCHEMA [Utilities]')
GO

IF OBJECT_ID('[KLHK].[ArahanPemanfaatanHutanProduksi]') IS NOT NULL
	DROP TABLE [KLHK].[ArahanPemanfaatanHutanProduksi]
GO
CREATE TABLE [KLHK].[ArahanPemanfaatanHutanProduksi] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[kodeprov] int NULL,
[arahan_19] varchar(62) NULL,
CONSTRAINT [pk_KLHK_ArahanPemanfaatanHutanProduksi_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_ArahanPemanfaatanHutanProduksi_Shape] ON [KLHK].[ArahanPemanfaatanHutanProduksi](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10612249.221323071,  ymin = -1214951.1736942562,  xmax = 15696446.784850607,  ymax = 618255.4499077563));
GO

IF OBJECT_ID('[KLHK].[BatasDas]') IS NOT NULL
	DROP TABLE [KLHK].[BatasDas]
GO
CREATE TABLE [KLHK].[BatasDas] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[kode_prov] int NULL,
[nama_das] varchar(62) NULL,
[luas_ha] float NULL,
[kel_m] float NULL,
[prioritas_] smallint NULL,
[kd_tematik] varchar(3) NULL,
[kd_region] smallint NULL,
[kd_lintas] smallint NULL,
[kd_das] varchar(11) NULL,
[wil_kerja] varchar(62) NULL,
[kd_urutdas] smallint NULL,
[globalid] varchar(47) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_BatasDas_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BatasDas_shape] ON [KLHK].[BatasDas](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15696049.900475679,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK].[BURN_AREA_2015]') IS NOT NULL
	DROP TABLE [KLHK].[BURN_AREA_2015]
GO
CREATE TABLE [KLHK].[BURN_AREA_2015] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[Luas] float NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_BURN_AREA_2015_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BURN_AREA_2015_Shape] ON [KLHK].[BURN_AREA_2015](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10673556.241654037,  ymin = -1207615.7131777396,  xmax = 15772137.449682387,  ymax = 495324.9246791944));
GO

IF OBJECT_ID('[KLHK].[BurnAreaIndonesia2016]') IS NOT NULL
	DROP TABLE [KLHK].[BurnAreaIndonesia2016]
GO
CREATE TABLE [KLHK].[BurnAreaIndonesia2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[luas] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_BurnAreaIndonesia2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BurnAreaIndonesia2016_shape] ON [KLHK].[BurnAreaIndonesia2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10630295.891224591,  ymin = -1141059.6178268855,  xmax = 15690764.487899574,  ymax = 580624.0963193306));
GO

IF OBJECT_ID('[KLHK].[BurnAreaIndonesia2017]') IS NOT NULL
	DROP TABLE [KLHK].[BurnAreaIndonesia2017]
GO
CREATE TABLE [KLHK].[BurnAreaIndonesia2017] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[luas] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_BurnAreaIndonesia2017_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BurnAreaIndonesia2017_shape] ON [KLHK].[BurnAreaIndonesia2017](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10606623.881100839,  ymin = -1212988.825200088,  xmax = 15695579.044410475,  ymax = 610672.6902352808));
GO

IF OBJECT_ID('[KLHK].[BurnArea]') IS NOT NULL
	DROP TABLE [KLHK].[BurnArea]
GO
CREATE TABLE [KLHK].[BurnArea] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Luas] float NULL,
[Periode] varchar(37) NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_BurnArea_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BurnArea_Shape] ON [KLHK].[BurnArea](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10632668.518691039,  ymin = -1149200.5400683028,  xmax = 15694342.749591034,  ymax = 546591.293526884));
GO

IF OBJECT_ID('[KLHK].[BurnArea2019]') IS NOT NULL
	DROP TABLE [KLHK].[BurnArea2019]
GO
CREATE TABLE [KLHK].[BurnArea2019] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[Periode] varchar(18) NULL,
[Luas] float NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_BurnArea2019_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_BurnArea2019_Shape] ON [KLHK].[BurnArea2019](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.41910666400008,  ymin = -10.829716807999944,  xmax = 141.01792734600008,  ymax = 5.534889735000036));
GO

IF OBJECT_ID('[KLHK].[Deforestation20032006]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20032006]
GO
CREATE TABLE [KLHK].[Deforestation20032006] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2003_2006_area] float NULL,
[landuse2003] varchar(62) NULL,
[landuse2006] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20032006_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20032006_shape] ON [KLHK].[Deforestation20032006](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10599069.185973221,  ymin = -1220240.7862468746,  xmax = 15696048.201851575,  ymax = 654384.5322049214));
GO

IF OBJECT_ID('[KLHK].[Deforestation20062009]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20062009]
GO
CREATE TABLE [KLHK].[Deforestation20062009] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2006_2009_area] float NULL,
[landuse2006] varchar(62) NULL,
[landuse2009] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20062009_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20062009_shape] ON [KLHK].[Deforestation20062009](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10622254.442050006,  ymin = -1010615.2674040551,  xmax = 15695182.33102231,  ymax = 622761.7466963774));
GO

IF OBJECT_ID('[KLHK].[Deforestation20092011]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20092011]
GO
CREATE TABLE [KLHK].[Deforestation20092011] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2009_2011_area] float NULL,
[landuse2009] varchar(62) NULL,
[landuse2011] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20092011_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20092011_shape] ON [KLHK].[Deforestation20092011](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10611204.591874374,  ymin = -1215834.1841169756,  xmax = 15692517.270611644,  ymax = 614836.3179790565));
GO

IF OBJECT_ID('[KLHK].[Deforestation20112012]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20112012]
GO
CREATE TABLE [KLHK].[Deforestation20112012] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[k_prop] smallint NULL,
[pl11_id] int NULL,
[pl12_id] int NULL,
[kws] varchar(37) NULL,
[kode_prop] smallint NULL,
[luas_ha] float NULL,
[kode_p09__] float NULL,
[kode_p09_1] varchar(317) NULL,
[kelas] varchar(317) NULL,
[kode_p09_2] varchar(317) NULL,
[kode_p09_3] float NULL,
[kode_p09_4] varchar(317) NULL,
[kelas_12] varchar(317) NULL,
[urut_v] float NULL,
[kode_p09_5] varchar(317) NULL,
[re_kws] varchar(18) NULL,
[urut_kws] smallint NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20112012_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20112012_shape] ON [KLHK].[Deforestation20112012](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10603921.048651112,  ymin = -1144272.1642380448,  xmax = 14940782.476672476,  ymax = 652115.9841073104));
GO

IF OBJECT_ID('[KLHK].[Deforestation20122013]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20122013]
GO
CREATE TABLE [KLHK].[Deforestation20122013] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[ket] varchar(12) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20122013_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20122013_shape] ON [KLHK].[Deforestation20122013](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10625729.48266791,  ymin = -1202140.448646454,  xmax = 15689784.973005908,  ymax = 616752.0106376818));
GO

IF OBJECT_ID('[KLHK].[Deforestation20132014]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestation20132014]
GO
CREATE TABLE [KLHK].[Deforestation20132014] (
[objectid] int NOT NULL,
[ket] varchar(12) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestation20132014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestation20132014_shape] ON [KLHK].[Deforestation20132014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10606634.38287028,  ymin = -1137567.688944834,  xmax = 15695791.71317319,  ymax = 611245.4593704295));
GO

IF OBJECT_ID('[KLHK].[Deforestasi2014_2015]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestasi2014_2015]
GO
CREATE TABLE [KLHK].[Deforestasi2014_2015] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[ket] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestasi2014_2015_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestasi2014_2015_shape] ON [KLHK].[Deforestasi2014_2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10619373.741202824,  ymin = -1225074.5933172652,  xmax = 15698209.60368267,  ymax = 555312.3234543385));
GO

IF OBJECT_ID('[KLHK].[DeforestasiTahun2015_2016]') IS NOT NULL
	DROP TABLE [KLHK].[DeforestasiTahun2015_2016]
GO
CREATE TABLE [KLHK].[DeforestasiTahun2015_2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[shape_leng] float NULL,
[ket] varchar(25) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_DeforestasiTahun2015_2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_DeforestasiTahun2015_2016_shape] ON [KLHK].[DeforestasiTahun2015_2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10603023.766467178,  ymin = -1014592.2303049477,  xmax = 15685818.701961666,  ymax = 653956.0471054983));
GO

IF OBJECT_ID('[KLHK].[Deforestasi2016_2017]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestasi2016_2017]
GO
CREATE TABLE [KLHK].[Deforestasi2016_2017] (
[objectid] int NOT NULL,
[ket_def] varchar(6) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestasi2016_2017_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestasi2016_2017_shape] ON [KLHK].[Deforestasi2016_2017](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10604363.588515913,  ymin = -1004932.383696676,  xmax = 15687979.848969275,  ymax = 591049.5038178021));
GO

IF OBJECT_ID('[KLHK].[Deforestasi2017_2018]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestasi2017_2018]
GO
CREATE TABLE [KLHK].[Deforestasi2017_2018] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[fid_kws_no] int NULL,
[label] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[fid_pl1718] int NULL,
[provinsi_1] varchar(62) NULL,
[pl17_id] int NULL,
[pl2018] int NULL,
[l] float NULL,
[pl17_id_1] float NULL,
[simbol_17] varchar(317) NULL,
[kelas_17] varchar(317) NULL,
[urut_v17] float NULL,
[ps_17] varchar(317) NULL,
[kel_def17] varchar(317) NULL,
[pl18_id] float NULL,
[simbol_18] varchar(317) NULL,
[kelas_18] varchar(317) NULL,
[urut_v18] float NULL,
[ps_18] varchar(317) NULL,
[kel_def18] varchar(317) NULL,
[shape_leng] float NULL,
[ket] varchar(25) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_Deforestasi2017_2018_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestasi2017_2018_shape] ON [KLHK].[Deforestasi2017_2018](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10589733.82004074,  ymin = -1232326.7786307938,  xmax = 15696268.365978235,  ymax = 624302.1184581473));
GO

IF OBJECT_ID('[KLHK].[Deforestasi2018_2019]') IS NOT NULL
	DROP TABLE [KLHK].[Deforestasi2018_2019]
GO
CREATE TABLE [KLHK].[Deforestasi2018_2019] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[KET] varchar(25) NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_Deforestasi2018_2019_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Deforestasi2018_2019_Shape] ON [KLHK].[Deforestasi2018_2019](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10623914.75321261,  ymin = -1147044.9699286856,  xmax = 15694962.836798271,  ymax = 617924.8330256091));
GO

IF OBJECT_ID('[KLHK].[EkoregionDarat]') IS NOT NULL
	DROP TABLE [KLHK].[EkoregionDarat]
GO
CREATE TABLE [KLHK].[EkoregionDarat] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[kode] varchar(3) NULL,
[nameko2017] varchar(317) NULL,
[kodeeko] int NULL,
[transparan] int NULL,
[kepulauan] varchar(125) NULL,
[bujur] varchar(317) NULL,
[lintang] varchar(317) NULL,
[luas] float NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EkoregionDarat_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EkoregionDarat_shape] ON [KLHK].[EkoregionDarat](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10572308.484441176,  ymin = -1232970.3876269285,  xmax = 15699380.711553814,  ymax = 677753.8042168831));
GO

IF OBJECT_ID('[KLHK].[EkoregionLaut]') IS NOT NULL
	DROP TABLE [KLHK].[EkoregionLaut]
GO
CREATE TABLE [KLHK].[EkoregionLaut] (
[objectid] int NOT NULL,
[id] int NULL,
[eko_id_br] smallint NULL,
[ek_laut_na] varchar(125) NULL,
[kode_00] varchar(12) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EkoregionLaut_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EkoregionLaut_shape] ON [KLHK].[EkoregionLaut](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10246051.961724585,  ymin = -1567579.1286850164,  xmax = 15740575.894864399,  ymax = 918364.5462628781));
GO

IF OBJECT_ID('[KLHK].[EkoregionDarat]') IS NOT NULL
	DROP TABLE [KLHK].[EkoregionDarat]
GO
CREATE TABLE [KLHK].[EkoregionDarat] (
[objectid] int NOT NULL,
[objectid_1] int NULL,
[nama] varchar(125) NULL,
[kode] varchar(3) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EkoregionDarat_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EkoregionDarat_shape] ON [KLHK].[EkoregionDarat](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10572308.484463252,  ymin = -1232970.387577215,  xmax = 15699380.711566368,  ymax = 677753.8042092284));
GO

IF OBJECT_ID('[KLHK].[FungsiEkologiGambut]') IS NOT NULL
	DROP TABLE [KLHK].[FungsiEkologiGambut]
GO
CREATE TABLE [KLHK].[FungsiEkologiGambut] (
[objectid] int NOT NULL,
[nama_khg] varchar(125) NULL,
[kode_khg] varchar(37) NULL,
[status_khg] varchar(37) NULL,
[kubah_gmbt] varchar(37) NULL,
[feg_kghltr] varchar(62) NULL,
[luas__ha] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_FungsiEkologiGambut_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_FungsiEkologiGambut_shape] ON [KLHK].[FungsiEkologiGambut](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621212.117360055,  ymin = -926516.7138912926,  xmax = 15692210.766642649,  ymax = 545217.2085017891));
GO

IF OBJECT_ID('[KLHK].[SebaranHotspotTahun2014]') IS NOT NULL
	DROP TABLE [KLHK].[SebaranHotspotTahun2014]
GO
CREATE TABLE [KLHK].[SebaranHotspotTahun2014] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long_] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date_] float NULL,
[source] varchar(317) NULL,
[provinsi] varchar(75) NULL,
[kab_kota] varchar(50) NULL,
[kec2006] varchar(87) NULL,
[desaa2006] varchar(87) NULL,
[nama_kaw] varchar(87) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_SebaranHotspotTahun2014_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_SebaranHotspotTahun2014_shape] ON [KLHK].[SebaranHotspotTahun2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10611530.459868802,  ymin = -967718.42022192,  xmax = 13934417.260048013,  ymax = 619910.064137754));
GO

IF OBJECT_ID('[KLHK].[SebaranHotspotTahun2015]') IS NOT NULL
	DROP TABLE [KLHK].[SebaranHotspotTahun2015]
GO
CREATE TABLE [KLHK].[SebaranHotspotTahun2015] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long_] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date_] float NULL,
[source] varchar(317) NULL,
[provinsi] varchar(75) NULL,
[kab_kota] varchar(50) NULL,
[kec2006] varchar(87) NULL,
[desaa2006] varchar(87) NULL,
[fungsi] varchar(18) NULL,
[pas_name] varchar(75) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_SebaranHotspotTahun2015_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_SebaranHotspotTahun2015_shape] ON [KLHK].[SebaranHotspotTahun2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10609860.667506903,  ymin = -958711.11478867,  xmax = 13929964.480416289,  ymax = 791277.1851438589));
GO

IF OBJECT_ID('[KLHK].[SebaranHotspotTahun2016]') IS NOT NULL
	DROP TABLE [KLHK].[SebaranHotspotTahun2016]
GO
CREATE TABLE [KLHK].[SebaranHotspotTahun2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date] int NULL,
[source] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kab_kota] varchar(317) NULL,
[kec2006] varchar(317) NULL,
[desaa2006] varchar(317) NULL,
[nama_kaw] varchar(317) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_SebaranHotspotTahun2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_SebaranHotspotTahun2016_shape] ON [KLHK].[SebaranHotspotTahun2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10631011.370757626,  ymin = -940702.1775890316,  xmax = 13887106.476460878,  ymax = 617673.188234664));
GO

IF OBJECT_ID('[KLHK].[SebaranHotspotTahun2017]') IS NOT NULL
	DROP TABLE [KLHK].[SebaranHotspotTahun2017]
GO
CREATE TABLE [KLHK].[SebaranHotspotTahun2017] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[join_count] int NULL,
[target_fid] int NULL,
[lat] float NULL,
[long] float NULL,
[satellite] varchar(317) NULL,
[conf__] int NULL,
[time_utc] varchar(317) NULL,
[date] varchar(317) NULL,
[source] varchar(317) NULL,
[provinsi] varchar(62) NULL,
[kabkot] varchar(62) NULL,
[kecamatan] varchar(62) NULL,
[desa] varchar(62) NULL,
[tahun] varchar(62) NULL,
CONSTRAINT [pk_KLHK_SebaranHotspotTahun2017_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_SebaranHotspotTahun2017_Shape] ON [KLHK].[SebaranHotspotTahun2017](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621629.150340144,  ymin = -1212437.1355538075,  xmax = 15696151.818033604,  ymax = 620212.2718943226));
GO

IF OBJECT_ID('[KLHK].[SebaranHotspotTahun2018]') IS NOT NULL
	DROP TABLE [KLHK].[SebaranHotspotTahun2018]
GO
CREATE TABLE [KLHK].[SebaranHotspotTahun2018] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[Lat] float NULL,
[Long] float NULL,
[Tgl_ddmmyy] bigint NULL, 
[Tgl_ddmmyy_Date] AS (dateadd(millisecond, Tgl_ddmmyy%(60000), dateadd(minute, Tgl_ddmmyy/(60000), '1970-01-01 00:00:00.000'))),
[Time_UTC] varchar(317) NULL,
[TK__] int NULL,
[Satelit] varchar(317) NULL,
[Kecamatan] varchar(317) NULL,
[Kabupaten] varchar(317) NULL,
[Provinsi] varchar(317) NULL,
CONSTRAINT [pk_KLHK_SebaranHotspotTahun2018_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_SebaranHotspotTahun2018_Shape] ON [KLHK].[SebaranHotspotTahun2018](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10618268.468346454,  ymin = -1215214.0015646734,  xmax = 15697829.313704265,  ymax = 624941.1819857573));
GO

IF OBJECT_ID('[KLHK].[Sebaran_Hotspot_Tahun_2019]') IS NOT NULL
	DROP TABLE [KLHK].[Sebaran_Hotspot_Tahun_2019]
GO
CREATE TABLE [KLHK].[Sebaran_Hotspot_Tahun_2019] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[Lat] float NULL,
[Long] float NULL,
[Tgl_ddmmyy] bigint NULL, 
[Tgl_ddmmyy_Date] AS (dateadd(millisecond, Tgl_ddmmyy%(60000), dateadd(minute, Tgl_ddmmyy/(60000), '1970-01-01 00:00:00.000'))),
[Time_UTC] varchar(317) NULL,
[TK__] int NULL,
[Satelit] varchar(317) NULL,
[Kecamatan] varchar(317) NULL,
[Kabupaten] varchar(317) NULL,
[Provinsi] varchar(317) NULL,
CONSTRAINT [pk_KLHK_Sebaran_Hotspot_Tahun_2019_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_Sebaran_Hotspot_Tahun_2019_Shape] ON [KLHK].[Sebaran_Hotspot_Tahun_2019](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10624741.835885447,  ymin = -1212923.629457321,  xmax = 15687855.855433673,  ymax = 616428.0381458461));
GO

IF OBJECT_ID('[KLHK].[HutanAdat]') IS NOT NULL
	DROP TABLE [KLHK].[HutanAdat]
GO
CREATE TABLE [KLHK].[HutanAdat] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[PROVINSI] varchar(62) NULL,
[KABUPATEN] varchar(62) NULL,
[KECAMATAN] varchar(62) NULL,
[DESA] varchar(187) NULL,
[NAMOBJ] varchar(312) NULL,
[NAMA_MHA] varchar(187) NULL,
[SK_MENLHK] varchar(187) NULL,
[TGL_PNTPN] bigint NULL, 
[TGL_PNTPN_Date] AS (dateadd(millisecond, TGL_PNTPN%(60000), dateadd(minute, TGL_PNTPN/(60000), '1970-01-01 00:00:00.000'))),
[FUNGSI_KWS] varchar(37) NULL,
[LUAS] float NULL,
[DSR_PNTPN] varchar(187) NULL,
[FCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[SRS_ID] varchar(62) NULL,
[KET_HUTAN] varchar(25) NULL,
[REMARK] varchar(312) NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_HutanAdat_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_HutanAdat_Shape] ON [KLHK].[HutanAdat](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11085270.2504782,  ymin = -953349.6115922667,  xmax = 13550012.440376652,  ymax = 140343.4245148389));
GO

IF OBJECT_ID('[KLHK].[HakPengelolaanHutanDesa]') IS NOT NULL
	DROP TABLE [KLHK].[HakPengelolaanHutanDesa]
GO
CREATE TABLE [KLHK].[HakPengelolaanHutanDesa] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HD_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(62) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_LPHD] varchar(62) NULL,
[NO_SK_HPHD] varchar(62) NULL,
[TGL_HPHD] bigint NULL, 
[TGL_HPHD_Date] AS (dateadd(millisecond, TGL_HPHD%(60000), dateadd(minute, TGL_HPHD/(60000), '1970-01-01 00:00:00.000'))),
[NO_SK_PAK] varchar(62) NULL,
[TGL_SK_PAK] bigint NULL, 
[TGL_SK_PAK_Date] AS (dateadd(millisecond, TGL_SK_PAK%(60000), dateadd(minute, TGL_SK_PAK/(60000), '1970-01-01 00:00:00.000'))),
[LUAS_HL] float NULL,
[LUAS_HP] float NULL,
[LUAS_HPT] float NULL,
[LUAS_HPK] float NULL,
[LUAS_HPHD] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_HakPengelolaanHutanDesa_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_HakPengelolaanHutanDesa_SHAPE] ON [KLHK].[HakPengelolaanHutanDesa](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10607320.807904901,  ymin = -944304.7913925685,  xmax = 15668880.98903507,  ymax = 611851.8175949687));
GO

IF OBJECT_ID('[KLHK].[IzinUsahaPemanfaatanHutanKemasyarakatan]') IS NOT NULL
	DROP TABLE [KLHK].[IzinUsahaPemanfaatanHutanKemasyarakatan]
GO
CREATE TABLE [KLHK].[IzinUsahaPemanfaatanHutanKemasyarakatan] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HKM_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(87) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_HKM] varchar(62) NULL,
[NO_IUPHKM] varchar(62) NULL,
[TGL_IUPHKM] bigint NULL, 
[TGL_IUPHKM_Date] AS (dateadd(millisecond, TGL_IUPHKM%(60000), dateadd(minute, TGL_IUPHKM/(60000), '1970-01-01 00:00:00.000'))),
[NO_SK_PAK] varchar(62) NULL,
[TGL_SK_PAK] bigint NULL, 
[TGL_SK_PAK_Date] AS (dateadd(millisecond, TGL_SK_PAK%(60000), dateadd(minute, TGL_SK_PAK/(60000), '1970-01-01 00:00:00.000'))),
[L_IUPHKM] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_IzinUsahaPemanfaatanHutanKemasyarakatan_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IzinUsahaPemanfaatanHutanKemasyarakatan_SHAPE] ON [KLHK].[IzinUsahaPemanfaatanHutanKemasyarakatan](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10606459.160314485,  ymin = -1142365.5686552636,  xmax = 15631907.558562323,  ymax = 583387.8212839274));
GO

IF OBJECT_ID('[KLHK].[MANGROVE_AR_50K]') IS NOT NULL
	DROP TABLE [KLHK].[MANGROVE_AR_50K]
GO
CREATE TABLE [KLHK].[MANGROVE_AR_50K] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[FCODE] varchar(62) NULL,
[LCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[NAMOBJ] varchar(62) NULL,
[SRSID] varchar(62) NULL,
[KRTJ] varchar(62) NULL,
[KRPH] varchar(62) NULL,
[SMBRDAT] varchar(187) NULL,
[THNBUAT] varchar(62) NULL,
[FGSFRF] varchar(62) NULL,
[INTS] varchar(62) NULL,
[REMARK] varchar(62) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
[LS_MGR] float NULL,
CONSTRAINT [pk_KLHK_MANGROVE_AR_50K_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_MANGROVE_AR_50K_SHAPE] ON [KLHK].[MANGROVE_AR_50K](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.15803553500007,  ymin = -5.901307390999932,  xmax = 109.12052236300008,  ymax = 5.8693109590000745));
GO

IF OBJECT_ID('[KLHK].[MANGROVE_AR_25K]') IS NOT NULL
	DROP TABLE [KLHK].[MANGROVE_AR_25K]
GO
CREATE TABLE [KLHK].[MANGROVE_AR_25K] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[FCODE] varchar(62) NULL,
[LCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[NAMOBJ] varchar(62) NULL,
[SRSID] varchar(62) NULL,
[KRTJ] varchar(62) NULL,
[KRPH] varchar(62) NULL,
[SMBRDAT] varchar(125) NULL,
[THNBUAT] varchar(62) NULL,
[FGSFRF] varchar(62) NULL,
[INTS] varchar(62) NULL,
[REMARK] varchar(62) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
[LS_MGR] float NULL,
CONSTRAINT [pk_KLHK_MANGROVE_AR_25K_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_MANGROVE_AR_25K_SHAPE] ON [KLHK].[MANGROVE_AR_25K](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 105.10015035100008,  ymin = -10.940138012999967,  xmax = 134.90598448600008,  ymax = 2.612264420000031));
GO

IF OBJECT_ID('[KLHK].[MANGROVE_AR_250K]') IS NOT NULL
	DROP TABLE [KLHK].[MANGROVE_AR_250K]
GO
CREATE TABLE [KLHK].[MANGROVE_AR_250K] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[FCODE] varchar(62) NULL,
[LCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[NAMOBJ] varchar(62) NULL,
[SRSID] varchar(62) NULL,
[SMBRDAT] varchar(125) NULL,
[THNBUAT] varchar(62) NULL,
[FGSFRF] varchar(62) NULL,
[INTS] varchar(62) NULL,
[REMARK] varchar(62) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
[LS_MGR] float NULL,
CONSTRAINT [pk_KLHK_MANGROVE_AR_250K_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_MANGROVE_AR_250K_SHAPE] ON [KLHK].[MANGROVE_AR_250K](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 105.64217376700009,  ymin = -9.118246041999953,  xmax = 140.99978499400004,  ymax = 4.722633839000025));
GO

IF OBJECT_ID('[KLHK].[IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat]') IS NOT NULL
	DROP TABLE [KLHK].[IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat]
GO
CREATE TABLE [KLHK].[IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HTR_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(62) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_HTR] varchar(62) NULL,
[NO_IUPHHK_HTR] varchar(62) NULL,
[TGL_IUPHHK_HTR] bigint NULL, 
[TGL_IUPHHK_HTR_Date] AS (dateadd(millisecond, TGL_IUPHHK_HTR%(60000), dateadd(minute, TGL_IUPHHK_HTR/(60000), '1970-01-01 00:00:00.000'))),
[L_IUPHHK_HTR] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat_SHAPE] ON [KLHK].[IzinUsahaPemanfaatanHasilHutanKayuHutanTanamanRakyat](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11027311.502452413,  ymin = -1127922.9687452575,  xmax = 15147917.804868942,  ymax = 468867.52909035474));
GO

IF OBJECT_ID('[KLHK].[IUPHHKHutanAlam]') IS NOT NULL
	DROP TABLE [KLHK].[IUPHHKHutanAlam]
GO
CREATE TABLE [KLHK].[IUPHHKHutanAlam] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[FCODE] varchar(62) NULL,
[NAMOBJ] varchar(312) NULL,
[REMARK] varchar(312) NULL,
[METADATA] varchar(62) NULL,
[SRS_ID] varchar(62) NULL,
[HA_ID] varchar(62) NULL,
[Kode_Prov] int NULL,
[No_SK] varchar(62) NULL,
[Tgl_SK] bigint NULL, 
[Tgl_SK_Date] AS (dateadd(millisecond, Tgl_SK%(60000), dateadd(minute, Tgl_SK/(60000), '1970-01-01 00:00:00.000'))),
[No_SK_Tap] varchar(62) NULL,
[Tgl_SK_Tap] bigint NULL, 
[Tgl_SK_Tap_Date] AS (dateadd(millisecond, Tgl_SK_Tap%(60000), dateadd(minute, Tgl_SK_Tap/(60000), '1970-01-01 00:00:00.000'))),
[LSSK] float NULL,
[SHAPE_Leng] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_IUPHHKHutanAlam_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IUPHHKHutanAlam_Shape] ON [KLHK].[IUPHHKHutanAlam](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10619903.695449868,  ymin = -933190.7179859309,  xmax = 15695411.45213785,  ymax = 573294.817074748));
GO

IF OBJECT_ID('[KLHK].[IUPHHKHutanTanaman]') IS NOT NULL
	DROP TABLE [KLHK].[IUPHHKHutanTanaman]
GO
CREATE TABLE [KLHK].[IUPHHKHutanTanaman] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[FCODE] varchar(62) NULL,
[NAMOBJ] varchar(312) NULL,
[REMARK] varchar(312) NULL,
[METADATA] varchar(62) NULL,
[SRS_ID] varchar(62) NULL,
[HT_ID] varchar(62) NULL,
[Kode_Prov] int NULL,
[No_SK] varchar(62) NULL,
[Tgl_SK] bigint NULL, 
[Tgl_SK_Date] AS (dateadd(millisecond, Tgl_SK%(60000), dateadd(minute, Tgl_SK/(60000), '1970-01-01 00:00:00.000'))),
[No_SK_Tap] varchar(62) NULL,
[Tgl_SK_Tap] bigint NULL, 
[Tgl_SK_Tap_Date] AS (dateadd(millisecond, Tgl_SK_Tap%(60000), dateadd(minute, Tgl_SK_Tap/(60000), '1970-01-01 00:00:00.000'))),
[LSSK] float NULL,
[SHAPE_Leng] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_IUPHHKHutanTanaman_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IUPHHKHutanTanaman_Shape] ON [KLHK].[IUPHHKHutanTanaman](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10622236.31545205,  ymin = -1121844.7922096045,  xmax = 15666376.791077217,  ymax = 627232.7970102817));
GO

IF OBJECT_ID('[KLHK].[IUPHHKRestorasiEkosistem]') IS NOT NULL
	DROP TABLE [KLHK].[IUPHHKRestorasiEkosistem]
GO
CREATE TABLE [KLHK].[IUPHHKRestorasiEkosistem] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[FCODE] varchar(62) NULL,
[NAMOBJ] varchar(312) NULL,
[REMARK] varchar(312) NULL,
[METADATA] varchar(62) NULL,
[SRS_ID] varchar(62) NULL,
[RE_ID] varchar(62) NULL,
[Kode_Prov] int NULL,
[No_SK] varchar(62) NULL,
[Tgl_SK] bigint NULL, 
[Tgl_SK_Date] AS (dateadd(millisecond, Tgl_SK%(60000), dateadd(minute, Tgl_SK/(60000), '1970-01-01 00:00:00.000'))),
[No_SK_Tap] varchar(62) NULL,
[Tgl_SK_Tap] bigint NULL, 
[Tgl_SK_Tap_Date] AS (dateadd(millisecond, Tgl_SK_Tap%(60000), dateadd(minute, Tgl_SK_Tap/(60000), '1970-01-01 00:00:00.000'))),
[LSSK] float NULL,
[SHAPE_Leng] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_IUPHHKRestorasiEkosistem_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IUPHHKRestorasiEkosistem_Shape] ON [KLHK].[IUPHHKRestorasiEkosistem](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11265929.343859954,  ymin = -376793.24774813635,  xmax = 12966607.122038255,  ymax = 177025.4556714707));
GO

IF OBJECT_ID('[KLHK].[KawasanHutandenganTujuanKhusus]') IS NOT NULL
	DROP TABLE [KLHK].[KawasanHutandenganTujuanKhusus]
GO
CREATE TABLE [KLHK].[KawasanHutandenganTujuanKhusus] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[khdtk_id] varchar(62) NULL,
[nameobj] varchar(312) NULL,
[jnskhdtk] varchar(62) NULL,
[nosk] varchar(62) NULL,
[tglsk] bigint NULL, 
[tglsk_Date] AS (dateadd(millisecond, tglsk%(60000), dateadd(minute, tglsk/(60000), '1970-01-01 00:00:00.000'))),
[lssk] float NULL,
[skdfn] varchar(62) NULL,
[remark] varchar(312) NULL,
[kodprv] int NULL,
[provinsi] varchar(317) NULL,
[fcode] varchar(62) NULL,
[lcode] varchar(62) NULL,
[metadata] varchar(62) NULL,
[srs_id] varchar(62) NULL,
[fngssk] varchar(62) NULL,
[infdtk] varchar(62) NULL,
[pnglol] varchar(62) NULL,
[jnslol] varchar(62) NULL,
[nskjuk] varchar(62) NULL,
[tskjuk] bigint NULL, 
[tskjuk_Date] AS (dateadd(millisecond, tskjuk%(60000), dateadd(minute, tskjuk/(60000), '1970-01-01 00:00:00.000'))),
[lskjuk] float NULL,
[nsktap] varchar(62) NULL,
[tsktap] bigint NULL, 
[tsktap_Date] AS (dateadd(millisecond, tsktap%(60000), dateadd(minute, tsktap/(60000), '1970-01-01 00:00:00.000'))),
[lsktap] float NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_KawasanHutandenganTujuanKhusus_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_KawasanHutandenganTujuanKhusus_Shape] ON [KLHK].[KawasanHutandenganTujuanKhusus](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11011857.166491052,  ymin = -1148407.3879900095,  xmax = 14915137.239407502,  ymax = 309669.1017309502));
GO

IF OBJECT_ID('[KLHK].[KawasanHutan]') IS NOT NULL
	DROP TABLE [KLHK].[KawasanHutan]
GO
CREATE TABLE [KLHK].[KawasanHutan] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[fgsfrf] int NULL,
[lskjuk] float NULL,
[nskjuk] varchar(125) NULL,
[tskjuk] bigint NULL, 
[tskjuk_Date] AS (dateadd(millisecond, tskjuk%(60000), dateadd(minute, tskjuk/(60000), '1970-01-01 00:00:00.000'))),
[fcode] varchar(62) NULL,
[metadata] varchar(62) NULL,
[namobj] varchar(312) NULL,
[remark] varchar(312) NULL,
[srs_id] varchar(62) NULL,
[lcode] varchar(62) NULL,
[kode_prov_] int NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_KawasanHutan_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_KawasanHutan_Shape] ON [KLHK].[KawasanHutan](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10572236.582291514,  ymin = -1232970.4198342145,  xmax = 15698279.243597636,  ymax = 677752.6509227199));
GO

IF OBJECT_ID('[KLHK].[dbklhk_sde_KHG]') IS NOT NULL
	DROP TABLE [KLHK].[dbklhk_sde_KHG]
GO
CREATE TABLE [KLHK].[dbklhk_sde_KHG] (
[objectid] int NOT NULL,
[kecamatan] varchar(33) NULL,
[kabupaten] varchar(40) NULL,
[provinsi] varchar(32) NULL,
[keterangan] varchar(62) NULL,
[ket_status] varchar(62) NULL,
[nama_khg] varchar(125) NULL,
[kode_khg_1] varchar(31) NULL,
[luas__m2] float NULL,
[luas__ha] float NULL,
[kode_khg] varchar(37) NULL,
[status_khg] varchar(62) NULL,
[ket__khg] varchar(62) NULL,
[kode__khg] varchar(37) NULL,
[ket_kg] varchar(62) NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_dbklhk_sde_KHG_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_dbklhk_sde_KHG_shape] ON [KLHK].[dbklhk_sde_KHG](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621212.117399294,  ymin = -929062.802051402,  xmax = 15693492.150112184,  ymax = 545217.2084622865));
GO

IF OBJECT_ID('[KLHK].[KPHK]') IS NOT NULL
	DROP TABLE [KLHK].[KPHK]
GO
CREATE TABLE [KLHK].[KPHK] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[provinsi] varchar(62) NULL,
[fungsi_kk] varchar(18) NULL,
[id_kph] int NULL,
[nama_kph] varchar(125) NULL,
[nomor_sk] varchar(62) NULL,
[tanggal] bigint NULL, 
[tanggal_Date] AS (dateadd(millisecond, tanggal%(60000), dateadd(minute, tanggal/(60000), '1970-01-01 00:00:00.000'))),
[luas] float NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_KPHK_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_KPHK_Shape] ON [KLHK].[KPHK](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.19616554200002,  ymin = -11.007615128999987,  xmax = 141.01944447999995,  ymax = 5.92952391));
GO

IF OBJECT_ID('[KLHK].[KPHP_KPHL]') IS NOT NULL
	DROP TABLE [KLHK].[KPHP_KPHL]
GO
CREATE TABLE [KLHK].[KPHP_KPHL] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[prov_unit] varchar(317) NULL,
[id_spasial] int NULL,
[nama_kph] varchar(317) NULL,
[nama_alias] varchar(317) NULL,
[id_jenis] int NULL,
[jenis_kph] varchar(317) NULL,
[organisasi] varchar(317) NULL,
[id_pecah] varchar(317) NULL,
[unit_angka] varchar(317) NULL,
[unit_kph] varchar(317) NULL,
[id_prov] int NULL,
[provinsi] varchar(317) NULL,
[wil_kab] varchar(317) NULL,
[id_penet] int NULL,
[penetapan] varchar(317) NULL,
[thn_real] float NULL,
[sk_penet] varchar(317) NULL,
[tgl_penet] bigint NULL, 
[tgl_penet_Date] AS (dateadd(millisecond, tgl_penet%(60000), dateadd(minute, tgl_penet/(60000), '1970-01-01 00:00:00.000'))),
[luas_penet] float NULL,
[sk_prov] varchar(317) NULL,
[tgl_prov] bigint NULL, 
[tgl_prov_Date] AS (dateadd(millisecond, tgl_prov%(60000), dateadd(minute, tgl_prov/(60000), '1970-01-01 00:00:00.000'))),
[sk_pergub] varchar(317) NULL,
[tgl_pergub] bigint NULL, 
[tgl_pergub_Date] AS (dateadd(millisecond, tgl_pergub%(60000), dateadd(minute, tgl_pergub/(60000), '1970-01-01 00:00:00.000'))),
[sk_rphjp] varchar(317) NULL,
[tgl_rphjp] bigint NULL, 
[tgl_rphjp_Date] AS (dateadd(millisecond, tgl_rphjp%(60000), dateadd(minute, tgl_rphjp/(60000), '1970-01-01 00:00:00.000'))),
[luas_rphjp] float NULL,
[thn_rphjp] varchar(317) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_KPHP_KPHL_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_KPHP_KPHL_Shape] ON [KLHK].[KPHP_KPHL](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01307203200003,  ymin = -10.919810521999977,  xmax = 141.00003603000005,  ymax = 5.882215488999975));
GO

IF OBJECT_ID('[KLHK].[LahanKritis]') IS NOT NULL
	DROP TABLE [KLHK].[LahanKritis]
GO
CREATE TABLE [KLHK].[LahanKritis] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[Kritis] varchar(62) NULL,
CONSTRAINT [pk_KLHK_LahanKritis_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_LahanKritis_Shape] ON [KLHK].[LahanKritis](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 94.97201709100004,  ymin = -11.007615377999928,  xmax = 141.00051037900008,  ymax = 6.07693003));
GO

IF OBJECT_ID('[KLHK].[PelepasanKawasanHutanuntukTransmigrasi]') IS NOT NULL
	DROP TABLE [KLHK].[PelepasanKawasanHutanuntukTransmigrasi]
GO
CREATE TABLE [KLHK].[PelepasanKawasanHutanuntukTransmigrasi] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODE_PROV] smallint NULL,
[NTRANS] varchar(125) NULL,
[WPPSKP] varchar(125) NULL,
[SKTRANS] varchar(125) NULL,
[TGLSKTRANS] bigint NULL, 
[TGLSKTRANS_Date] AS (dateadd(millisecond, TGLSKTRANS%(60000), dateadd(minute, TGLSKTRANS/(60000), '1970-01-01 00:00:00.000'))),
[LTRANS] float NULL,
[KETERANGAN] varchar(312) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_PelepasanKawasanHutanuntukTransmigrasi_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PelepasanKawasanHutanuntukTransmigrasi_SHAPE] ON [KLHK].[PelepasanKawasanHutanuntukTransmigrasi](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.45944831300005,  ymin = -9.516771080999945,  xmax = 140.80485058500005,  ymax = 5.3459593240000345));
GO

IF OBJECT_ID('[KLHK].[PelepasanKawasanHutan]') IS NOT NULL
	DROP TABLE [KLHK].[PelepasanKawasanHutan]
GO
CREATE TABLE [KLHK].[PelepasanKawasanHutan] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODEPROV] smallint NULL,
[NPLS] varchar(125) NULL,
[NOSKPLS] varchar(125) NULL,
[TGLSKPLS] bigint NULL, 
[TGLSKPLS_Date] AS (dateadd(millisecond, TGLSKPLS%(60000), dateadd(minute, TGLSKPLS/(60000), '1970-01-01 00:00:00.000'))),
[LSKPLS] float NULL,
[KOMODITAS] varchar(125) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_PelepasanKawasanHutan_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PelepasanKawasanHutan_SHAPE] ON [KLHK].[PelepasanKawasanHutan](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.28479692000008,  ymin = -8.745068937999974,  xmax = 140.98786337400009,  ymax = 5.364047928000048));
GO

IF OBJECT_ID('[KLHK].[PenutupanLahanTahun2014]') IS NOT NULL
	DROP TABLE [KLHK].[PenutupanLahanTahun2014]
GO
CREATE TABLE [KLHK].[PenutupanLahanTahun2014] (
[objectid] int NOT NULL,
[k_prop] smallint NULL,
[pl14_id] int NULL,
[luas] float NULL,
[shape_leng] float NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_PenutupanLahanTahun2014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PenutupanLahanTahun2014_shape] ON [KLHK].[PenutupanLahanTahun2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15717639.114466418,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK].[dbklhk_sde_PL_2015_Diss]') IS NOT NULL
	DROP TABLE [KLHK].[dbklhk_sde_PL_2015_Diss]
GO
CREATE TABLE [KLHK].[dbklhk_sde_PL_2015_Diss] (
[objectid] int NOT NULL,
[dbklhk_pantau_ipsdh_pl2015_k_pr] smallint NULL,
[dbklhk_sde_kode_pl_kode_veg] float NULL,
[dbklhk_sde_kode_pl_simbol] varchar(10) NULL,
[dbklhk_sde_kode_pl_kelas] varchar(36) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_dbklhk_sde_PL_2015_Diss_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_dbklhk_sde_PL_2015_Diss_shape] ON [KLHK].[dbklhk_sde_PL_2015_Diss](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.573618984,  ymin = -1233050.6363873458,  xmax = 15717639.114458114,  ymax = 658728.3137669326));
GO

IF OBJECT_ID('[KLHK].[PenutupanLahanTahun2016]') IS NOT NULL
	DROP TABLE [KLHK].[PenutupanLahanTahun2016]
GO
CREATE TABLE [KLHK].[PenutupanLahanTahun2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[pl16_id] int NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_PenutupanLahanTahun2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PenutupanLahanTahun2016_shape] ON [KLHK].[PenutupanLahanTahun2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15717639.114466418,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK].[PenutupanLahan]') IS NOT NULL
	DROP TABLE [KLHK].[PenutupanLahan]
GO
CREATE TABLE [KLHK].[PenutupanLahan] (
[objectid] int NOT NULL,
[k_prop] smallint NULL,
[pl17_id] int NULL,
[keterangan] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_PenutupanLahan_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PenutupanLahan_shape] ON [KLHK].[PenutupanLahan](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15717639.114466418,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK].[PenutupanLahan]') IS NOT NULL
	DROP TABLE [KLHK].[PenutupanLahan]
GO
CREATE TABLE [KLHK].[PenutupanLahan] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Provinsi_1] varchar(62) NULL,
[k_prop] int NULL,
[PL_18_ID] int NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_PenutupanLahan_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PenutupanLahan_Shape] ON [KLHK].[PenutupanLahan](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01255798400007,  ymin = -11.008322714999963,  xmax = 141.19395446800007,  ymax = 5.906965232000051));
GO

IF OBJECT_ID('[KLHK].[PenutupanLahan]') IS NOT NULL
	DROP TABLE [KLHK].[PenutupanLahan]
GO
CREATE TABLE [KLHK].[PenutupanLahan] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Provinsi] varchar(62) NULL,
[PL_19_R] int NULL,
[SHAPE_Leng] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_PenutupanLahan_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PenutupanLahan_Shape] ON [KLHK].[PenutupanLahan](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.573745267,  ymin = -1233050.6363851025,  xmax = 15696048.201962898,  ymax = 658728.3111434256));
GO

IF OBJECT_ID('[KLHK].[PIAPS4thRev]') IS NOT NULL
	DROP TABLE [KLHK].[PIAPS4thRev]
GO
CREATE TABLE [KLHK].[PIAPS4thRev] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[krit_tamba] varchar(62) NULL,
[kodeprov_1] int NULL,
[keterangan] varchar(62) NULL,
[luas_ha] float NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_PIAPS4thRev_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PIAPS4thRev_Shape] ON [KLHK].[PIAPS4thRev](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.260982189,  ymin = -10.818092017000026,  xmax = 141.00000190699996,  ymax = 5.849857601999986));
GO

IF OBJECT_ID('[KLHK].[PIAPS5thRev]') IS NOT NULL
	DROP TABLE [KLHK].[PIAPS5thRev]
GO
CREATE TABLE [KLHK].[PIAPS5thRev] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Krit_Tamba] varchar(62) NULL,
[Keterangan] varchar(62) NULL,
[KODEPROV_1] int NULL,
[Luas_Ha] float NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_PIAPS5thRev_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PIAPS5thRev_Shape] ON [KLHK].[PIAPS5thRev](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10604404.029635271,  ymin = -1211484.214877745,  xmax = 15696135.391840871,  ymax = 652337.5122025628));
GO

IF OBJECT_ID('[KLHK].[PinjamPakaiKawasanHutan]') IS NOT NULL
	DROP TABLE [KLHK].[PinjamPakaiKawasanHutan]
GO
CREATE TABLE [KLHK].[PinjamPakaiKawasanHutan] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[kode_prov] int NULL,
[id_ippkh] varchar(11) NULL,
[nama_ippkh] varchar(125) NULL,
[no_ippkh] varchar(62) NULL,
[tgl_ippkh] bigint NULL, 
[tgl_ippkh_Date] AS (dateadd(millisecond, tgl_ippkh%(60000), dateadd(minute, tgl_ippkh/(60000), '1970-01-01 00:00:00.000'))),
[luas_ippkh] float NULL,
[kode_guna] varchar(5) NULL,
[jenis_ippk] varchar(15) NULL,
[keterangan] varchar(62) NULL,
[tgl_berakh] bigint NULL, 
[tgl_berakh_Date] AS (dateadd(millisecond, tgl_berakh%(60000), dateadd(minute, tgl_berakh/(60000), '1970-01-01 00:00:00.000'))),
[kabupaten_] varchar(125) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_PinjamPakaiKawasanHutan_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PinjamPakaiKawasanHutan_Shape] ON [KLHK].[PinjamPakaiKawasanHutan](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10623392.930861318,  ymin = -1144756.642851397,  xmax = 15670975.495310597,  ymax = 594141.9930451924));
GO

IF OBJECT_ID('[KLHK].[IndikatifPenghentianPemberianIzinBaru]') IS NOT NULL
	DROP TABLE [KLHK].[IndikatifPenghentianPemberianIzinBaru]
GO
CREATE TABLE [KLHK].[IndikatifPenghentianPemberianIzinBaru] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[PIPPIB19_1] varchar(18) NULL,
CONSTRAINT [pk_KLHK_IndikatifPenghentianPemberianIzinBaru_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_IndikatifPenghentianPemberianIzinBaru_Shape] ON [KLHK].[IndikatifPenghentianPemberianIzinBaru](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01307203200012,  ymin = -11.007615089999964,  xmax = 141.0194444720001,  ymax = 5.907229826000188));
GO

IF OBJECT_ID('[KLHK].[PIPPIBTahun2020Periode1]') IS NOT NULL
	DROP TABLE [KLHK].[PIPPIBTahun2020Periode1]
GO
CREATE TABLE [KLHK].[PIPPIBTahun2020Periode1] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[objectid] int NULL,
[pippib20_1] varchar(25) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_PIPPIBTahun2020Periode1_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_PIPPIBTahun2020Periode1_Shape] ON [KLHK].[PIPPIBTahun2020Periode1](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576806.797306865,  ymin = -1232970.3872867082,  xmax = 15698212.750573361,  ymax = 658757.9227367552));
GO

IF OBJECT_ID('[KLHK].[RekalkulasiBatasKawasan]') IS NOT NULL
	DROP TABLE [KLHK].[RekalkulasiBatasKawasan]
GO
CREATE TABLE [KLHK].[RekalkulasiBatasKawasan] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[kodeprov] smallint NULL,
[nkws] varchar(312) NULL,
[ttbts] smallint NULL,
[blbf] varchar(3) NULL,
[babb] varchar(8) NULL,
[tbatb] bigint NULL, 
[tbatb_Date] AS (dateadd(millisecond, tbatb%(60000), dateadd(minute, tbatb/(60000), '1970-01-01 00:00:00.000'))),
[tsahbatb] bigint NULL, 
[tsahbatb_Date] AS (dateadd(millisecond, tsahbatb%(60000), dateadd(minute, tsahbatb/(60000), '1970-01-01 00:00:00.000'))),
[fungsibatb] varchar(18) NULL,
[pjbatb] float NULL,
[sumberbts] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_RekalkulasiBatasKawasan_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_RekalkulasiBatasKawasan_shape] ON [KLHK].[RekalkulasiBatasKawasan](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576806.797306865,  ymin = -1232970.4198342145,  xmax = 15698212.751463907,  ymax = 661252.988036878));
GO

IF OBJECT_ID('[KLHK].[RHL2014]') IS NOT NULL
	DROP TABLE [KLHK].[RHL2014]
GO
CREATE TABLE [KLHK].[RHL2014] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[satker] varchar(317) NULL,
[luas_ha] float NULL,
[keterangan] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[tipe_rhl] varchar(25) NULL,
[shape_leng] float NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_RHL2014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_RHL2014_shape] ON [KLHK].[RHL2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10521044.50795753,  ymin = -1218766.047358459,  xmax = 15684942.949189896,  ymax = 651051.8635198071));
GO

IF OBJECT_ID('[KLHK].[RehabilitasiHutandanLahanTahun2015]') IS NOT NULL
	DROP TABLE [KLHK].[RehabilitasiHutandanLahanTahun2015]
GO
CREATE TABLE [KLHK].[RehabilitasiHutandanLahanTahun2015] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[fungsi_kws] varchar(317) NULL,
[satker] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[luas_ha] float NULL,
[ket] varchar(317) NULL,
[lap_bibit] varchar(317) NULL,
[srt_pernya] varchar(317) NULL,
[foto] varchar(317) NULL,
[lab_bibit] varchar(317) NULL,
[id] int NULL,
[no_spks] varchar(317) NULL,
[kelompok] varchar(317) NULL,
[jenis] varchar(317) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_RehabilitasiHutandanLahanTahun2015_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_RehabilitasiHutandanLahanTahun2015_shape] ON [KLHK].[RehabilitasiHutandanLahanTahun2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10521044.54268921,  ymin = -1217348.7539144494,  xmax = 15689356.808855968,  ymax = 652776.5975172351));
GO

IF OBJECT_ID('[KLHK].[RehabilitasiHutandanLahanTahun2016]') IS NOT NULL
	DROP TABLE [KLHK].[RehabilitasiHutandanLahanTahun2016]
GO
CREATE TABLE [KLHK].[RehabilitasiHutandanLahanTahun2016] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[fungsi_kws] varchar(317) NULL,
[satker] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[luas_ha] float NULL,
[ket] varchar(317) NULL,
[jenis_rhl] varchar(317) NULL,
[kelompok] varchar(317) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_RehabilitasiHutandanLahanTahun2016_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_RehabilitasiHutandanLahanTahun2016_shape] ON [KLHK].[RehabilitasiHutandanLahanTahun2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 1643816.264294494,  ymin = -20683346.535252802,  xmax = 15675957.685727624,  ymax = 606324.4630364875));
GO

IF OBJECT_ID('[KLHK].[WilayahPengukuranKinerjaREDD]') IS NOT NULL
	DROP TABLE [KLHK].[WilayahPengukuranKinerjaREDD]
GO
CREATE TABLE [KLHK].[WilayahPengukuranKinerjaREDD] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[Gambut] varchar(10) NULL,
[REDD_Type] varchar(10) NULL,
[Luas] real NULL,
CONSTRAINT [pk_KLHK_WilayahPengukuranKinerjaREDD_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_WilayahPengukuranKinerjaREDD_Shape] ON [KLHK].[WilayahPengukuranKinerjaREDD](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10582026.276617289,  ymin = -1232326.77867644,  xmax = 15698209.603648797,  ymax = 658497.552264045));
IF OBJECT_ID('[KLHK_EN].[CommunityForest]') IS NOT NULL
	DROP TABLE [KLHK_EN].[CommunityForest]
GO
CREATE TABLE [KLHK_EN].[CommunityForest] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HTR_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(62) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_HTR] varchar(62) NULL,
[NO_IUPHHK_HTR] varchar(62) NULL,
[TGL_IUPHHK_HTR] bigint NULL, 
[TGL_IUPHHK_HTR_Date] AS (dateadd(millisecond, TGL_IUPHHK_HTR%(60000), dateadd(minute, TGL_IUPHHK_HTR/(60000), '1970-01-01 00:00:00.000'))),
[L_IUPHHK_HTR] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_CommunityForest_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_CommunityForest_SHAPE] ON [KLHK_EN].[CommunityForest](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11027311.502452413,  ymin = -1127922.9687452575,  xmax = 15147917.804868942,  ymax = 468867.52909035474));
GO

IF OBJECT_ID('[KLHK_EN].[CriticalLand]') IS NOT NULL
	DROP TABLE [KLHK_EN].[CriticalLand]
GO
CREATE TABLE [KLHK_EN].[CriticalLand] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[Kritis] varchar(62) NULL,
CONSTRAINT [pk_KLHK_EN_CriticalLand_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_CriticalLand_Shape] ON [KLHK_EN].[CriticalLand](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 94.97201709100004,  ymin = -11.007615377999928,  xmax = 141.00051037900008,  ymax = 6.07693003));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20032006]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20032006]
GO
CREATE TABLE [KLHK_EN].[Deforestation20032006] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2003_2006_area] float NULL,
[landuse2003] varchar(62) NULL,
[landuse2006] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20032006_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20032006_shape] ON [KLHK_EN].[Deforestation20032006](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10599069.185973221,  ymin = -1220240.7862468746,  xmax = 15696048.201851575,  ymax = 654384.5322049214));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20062009]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20062009]
GO
CREATE TABLE [KLHK_EN].[Deforestation20062009] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2006_2009_area] float NULL,
[landuse2006] varchar(62) NULL,
[landuse2009] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20062009_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20062009_shape] ON [KLHK_EN].[Deforestation20062009](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10622254.442050006,  ymin = -1010615.2674040551,  xmax = 15695182.33102231,  ymax = 622761.7466963774));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20092011]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20092011]
GO
CREATE TABLE [KLHK_EN].[Deforestation20092011] (
[objectid] int NOT NULL,
[name] varchar(62) NULL,
[dbklhk_sde_Deforestation_2009_2011_area] float NULL,
[landuse2009] varchar(62) NULL,
[landuse2011] varchar(62) NULL,
[province] varchar(62) NULL,
[years] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20092011_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20092011_shape] ON [KLHK_EN].[Deforestation20092011](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10611204.591874374,  ymin = -1215834.1841169756,  xmax = 15692517.270611644,  ymax = 614836.3179790565));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20112012]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20112012]
GO
CREATE TABLE [KLHK_EN].[Deforestation20112012] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[k_prop] smallint NULL,
[pl11_id] int NULL,
[pl12_id] int NULL,
[kws] varchar(37) NULL,
[kode_prop] smallint NULL,
[luas_ha] float NULL,
[kode_p09__] float NULL,
[kode_p09_1] varchar(317) NULL,
[kelas] varchar(317) NULL,
[kode_p09_2] varchar(317) NULL,
[kode_p09_3] float NULL,
[kode_p09_4] varchar(317) NULL,
[kelas_12] varchar(317) NULL,
[urut_v] float NULL,
[kode_p09_5] varchar(317) NULL,
[re_kws] varchar(18) NULL,
[urut_kws] smallint NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20112012_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20112012_shape] ON [KLHK_EN].[Deforestation20112012](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10603921.048651112,  ymin = -1144272.1642380448,  xmax = 14940782.476672476,  ymax = 652115.9841073104));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20122013]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20122013]
GO
CREATE TABLE [KLHK_EN].[Deforestation20122013] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[ket] varchar(12) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20122013_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20122013_shape] ON [KLHK_EN].[Deforestation20122013](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10625729.48266791,  ymin = -1202140.448646454,  xmax = 15689784.973005908,  ymax = 616752.0106376818));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation20132014]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation20132014]
GO
CREATE TABLE [KLHK_EN].[Deforestation20132014] (
[objectid] int NOT NULL,
[ket] varchar(12) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation20132014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation20132014_shape] ON [KLHK_EN].[Deforestation20132014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10606634.38287028,  ymin = -1137567.688944834,  xmax = 15695791.71317319,  ymax = 611245.4593704295));
GO

IF OBJECT_ID('[KLHK_EN].[Deforestation2014_2015]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Deforestation2014_2015]
GO
CREATE TABLE [KLHK_EN].[Deforestation2014_2015] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[ket] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Deforestation2014_2015_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Deforestation2014_2015_shape] ON [KLHK_EN].[Deforestation2014_2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10619373.741202824,  ymin = -1225074.5933172652,  xmax = 15698209.60368267,  ymax = 555312.3234543385));
GO

IF OBJECT_ID('[KLHK_EN].[DirectivesUtilizationofProductionForest]') IS NOT NULL
	DROP TABLE [KLHK_EN].[DirectivesUtilizationofProductionForest]
GO
CREATE TABLE [KLHK_EN].[DirectivesUtilizationofProductionForest] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[kodeprov] int NULL,
[arahan_19] varchar(62) NULL,
CONSTRAINT [pk_KLHK_EN_DirectivesUtilizationofProductionForest_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_DirectivesUtilizationofProductionForest_Shape] ON [KLHK_EN].[DirectivesUtilizationofProductionForest](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10612249.221323071,  ymin = -1214951.1736942562,  xmax = 15696446.784850607,  ymax = 618255.4499077563));
GO

IF OBJECT_ID('[KLHK_EN].[ForestAreaforSpecialPurpose]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ForestAreaforSpecialPurpose]
GO
CREATE TABLE [KLHK_EN].[ForestAreaforSpecialPurpose] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[khdtk_id] varchar(62) NULL,
[nameobj] varchar(312) NULL,
[jnskhdtk] varchar(62) NULL,
[nosk] varchar(62) NULL,
[tglsk] bigint NULL, 
[tglsk_Date] AS (dateadd(millisecond, tglsk%(60000), dateadd(minute, tglsk/(60000), '1970-01-01 00:00:00.000'))),
[lssk] float NULL,
[skdfn] varchar(62) NULL,
[remark] varchar(312) NULL,
[kodprv] int NULL,
[provinsi] varchar(317) NULL,
[fcode] varchar(62) NULL,
[lcode] varchar(62) NULL,
[metadata] varchar(62) NULL,
[srs_id] varchar(62) NULL,
[fngssk] varchar(62) NULL,
[infdtk] varchar(62) NULL,
[pnglol] varchar(62) NULL,
[jnslol] varchar(62) NULL,
[nskjuk] varchar(62) NULL,
[tskjuk] bigint NULL, 
[tskjuk_Date] AS (dateadd(millisecond, tskjuk%(60000), dateadd(minute, tskjuk/(60000), '1970-01-01 00:00:00.000'))),
[lskjuk] float NULL,
[nsktap] varchar(62) NULL,
[tsktap] bigint NULL, 
[tsktap_Date] AS (dateadd(millisecond, tsktap%(60000), dateadd(minute, tsktap/(60000), '1970-01-01 00:00:00.000'))),
[lsktap] float NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_EN_ForestAreaforSpecialPurpose_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ForestAreaforSpecialPurpose_Shape] ON [KLHK_EN].[ForestAreaforSpecialPurpose](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11011857.166491052,  ymin = -1148407.3879900095,  xmax = 14915137.239407502,  ymax = 309669.1017309502));
GO

IF OBJECT_ID('[KLHK_EN].[ForestArea]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ForestArea]
GO
CREATE TABLE [KLHK_EN].[ForestArea] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[FGSFRF] int NULL,
[LSKJUK] float NULL,
[NSKJUK] varchar(125) NULL,
[TSKJUK] bigint NULL, 
[TSKJUK_Date] AS (dateadd(millisecond, TSKJUK%(60000), dateadd(minute, TSKJUK/(60000), '1970-01-01 00:00:00.000'))),
[FCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[NAMOBJ] varchar(312) NULL,
[REMARK] varchar(312) NULL,
[SRS_ID] varchar(62) NULL,
[LCODE] varchar(62) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_ForestArea_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ForestArea_SHAPE] ON [KLHK_EN].[ForestArea](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 94.97201709200004,  ymin = -11.00761537699998,  xmax = 141.02004178900006,  ymax = 6.076930030000028));
GO

IF OBJECT_ID('[KLHK_EN].[ForestManagementUnitFMU]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ForestManagementUnitFMU]
GO
CREATE TABLE [KLHK_EN].[ForestManagementUnitFMU] (
[objectid] int NOT NULL,
[provinsi] varchar(317) NULL,
[kabupat] varchar(317) NULL,
[jenis_kph] varchar(25) NULL,
[unit_kph] varchar(62) NULL,
[nama_kph] varchar(317) NULL,
[cdkws] float NULL,
[fungsi_kws] varchar(12) NULL,
[kendali] varchar(62) NULL,
[luas_ha] float NULL,
[prior_mdl] int NULL,
[sk_mdl] varchar(62) NULL,
[tgl_sk_mdl] varchar(62) NULL,
[thn_sk_mdl] int NULL,
[luas_total] float NULL,
[legenda] varchar(62) NULL,
[unit_perub] varchar(62) NULL,
[prior_md] int NULL,
[total_luas] float NULL,
[status] varchar(62) NULL,
[rphjp_sah] varchar(62) NULL,
[sk_rphjp] varchar(62) NULL,
[tgl_rphjp] bigint NULL, 
[tgl_rphjp_Date] AS (dateadd(millisecond, tgl_rphjp%(60000), dateadd(minute, tgl_rphjp/(60000), '1970-01-01 00:00:00.000'))),
[wil_ttentu] varchar(62) NULL,
[l_wt] varchar(62) NULL,
[kodeprov] smallint NULL,
[shp_blok] varchar(62) NULL,
[sk] varchar(62) NULL,
[kode_kph] int NULL,
[ls_wt] float NULL,
[prog_fas] varchar(62) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_ForestManagementUnitFMU_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ForestManagementUnitFMU_shape] ON [KLHK_EN].[ForestManagementUnitFMU](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576800.74530403,  ymin = -1220615.2859689856,  xmax = 15699167.978218252,  ymax = 655958.5383277609));
GO

IF OBJECT_ID('[KLHK_EN].[HotspotDistribution2014]') IS NOT NULL
	DROP TABLE [KLHK_EN].[HotspotDistribution2014]
GO
CREATE TABLE [KLHK_EN].[HotspotDistribution2014] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long_] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date_] float NULL,
[source] varchar(317) NULL,
[provinsi] varchar(75) NULL,
[kab_kota] varchar(50) NULL,
[kec2006] varchar(87) NULL,
[desaa2006] varchar(87) NULL,
[nama_kaw] varchar(87) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_EN_HotspotDistribution2014_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_HotspotDistribution2014_shape] ON [KLHK_EN].[HotspotDistribution2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10611530.459868802,  ymin = -967718.42022192,  xmax = 13934417.260048013,  ymax = 619910.064137754));
GO

IF OBJECT_ID('[KLHK_EN].[HotspotDistribution2015]') IS NOT NULL
	DROP TABLE [KLHK_EN].[HotspotDistribution2015]
GO
CREATE TABLE [KLHK_EN].[HotspotDistribution2015] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long_] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date_] float NULL,
[source] varchar(317) NULL,
[provinsi] varchar(75) NULL,
[kab_kota] varchar(50) NULL,
[kec2006] varchar(87) NULL,
[desaa2006] varchar(87) NULL,
[fungsi] varchar(18) NULL,
[pas_name] varchar(75) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_EN_HotspotDistribution2015_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_HotspotDistribution2015_shape] ON [KLHK_EN].[HotspotDistribution2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10609860.667506903,  ymin = -958711.11478867,  xmax = 13929964.480416289,  ymax = 791277.1851438589));
GO

IF OBJECT_ID('[KLHK_EN].[HotspotDistribution2016]') IS NOT NULL
	DROP TABLE [KLHK_EN].[HotspotDistribution2016]
GO
CREATE TABLE [KLHK_EN].[HotspotDistribution2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[lat] float NULL,
[long] float NULL,
[satellite] varchar(317) NULL,
[time_utc] varchar(317) NULL,
[date] int NULL,
[source] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kab_kota] varchar(317) NULL,
[kec2006] varchar(317) NULL,
[desaa2006] varchar(317) NULL,
[nama_kaw] varchar(317) NULL,
[shape] geometry NULL,
CONSTRAINT [pk_KLHK_EN_HotspotDistribution2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_HotspotDistribution2016_shape] ON [KLHK_EN].[HotspotDistribution2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10631011.370757626,  ymin = -940702.1775890316,  xmax = 13887106.476460878,  ymax = 617673.188234664));
GO

IF OBJECT_ID('[KLHK_EN].[HotspotDistribution2017]') IS NOT NULL
	DROP TABLE [KLHK_EN].[HotspotDistribution2017]
GO
CREATE TABLE [KLHK_EN].[HotspotDistribution2017] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[join_count] int NULL,
[target_fid] int NULL,
[lat] float NULL,
[long] float NULL,
[satellite] varchar(317) NULL,
[conf__] int NULL,
[time_utc] varchar(317) NULL,
[date] varchar(317) NULL,
[source] varchar(317) NULL,
[provinsi] varchar(62) NULL,
[kabkot] varchar(62) NULL,
[kecamatan] varchar(62) NULL,
[desa] varchar(62) NULL,
[tahun] varchar(62) NULL,
CONSTRAINT [pk_KLHK_EN_HotspotDistribution2017_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_HotspotDistribution2017_Shape] ON [KLHK_EN].[HotspotDistribution2017](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621629.150340144,  ymin = -1212437.1355538075,  xmax = 15696151.818033604,  ymax = 620212.2718943226));
GO

IF OBJECT_ID('[KLHK_EN].[IndicativeTerminationMapPIPPIB]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IndicativeTerminationMapPIPPIB]
GO
CREATE TABLE [KLHK_EN].[IndicativeTerminationMapPIPPIB] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[PIPPIB19_1] varchar(18) NULL,
CONSTRAINT [pk_KLHK_EN_IndicativeTerminationMapPIPPIB_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_IndicativeTerminationMapPIPPIB_Shape] ON [KLHK_EN].[IndicativeTerminationMapPIPPIB](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01307203200012,  ymin = -11.007615089999964,  xmax = 141.0194444720001,  ymax = 5.907229826000188));
GO

IF OBJECT_ID('[KLHK_EN].[IndigenousForest]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IndigenousForest]
GO
CREATE TABLE [KLHK_EN].[IndigenousForest] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[PROVINSI] varchar(62) NULL,
[KABUPATEN] varchar(62) NULL,
[KECAMATAN] varchar(62) NULL,
[DESA] varchar(187) NULL,
[NAMOBJ] varchar(312) NULL,
[NAMA_MHA] varchar(187) NULL,
[SK_MENLHK] varchar(187) NULL,
[TGL_PNTPN] bigint NULL, 
[TGL_PNTPN_Date] AS (dateadd(millisecond, TGL_PNTPN%(60000), dateadd(minute, TGL_PNTPN/(60000), '1970-01-01 00:00:00.000'))),
[FUNGSI_KWS] varchar(37) NULL,
[LUAS] float NULL,
[DSR_PNTPN] varchar(187) NULL,
[FCODE] varchar(62) NULL,
[METADATA] varchar(62) NULL,
[SRS_ID] varchar(62) NULL,
[KET_HUTAN] varchar(25) NULL,
[REMARK] varchar(312) NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_IndigenousForest_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_IndigenousForest_Shape] ON [KLHK_EN].[IndigenousForest](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11085270.2504782,  ymin = -953349.6115922667,  xmax = 13550012.440376652,  ymax = 140343.4245148389));
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKHTI]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKHTI]
GO
CREATE TABLE [KLHK_EN].[IUPHHKHTI] (
[objectid_12] int NOT NULL,
[objectid_1] int NULL,
[objectid] int NULL,
[kode_prov] int NULL,
[nama_ht] varchar(62) NULL,
[no_sk_awal] varchar(25) NULL,
[tgl_sk_awa] bigint NULL, 
[tgl_sk_awa_Date] AS (dateadd(millisecond, tgl_sk_awa%(60000), dateadd(minute, tgl_sk_awa/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_akhi] varchar(25) NULL,
[tgl_sk_akh] bigint NULL, 
[tgl_sk_akh_Date] AS (dateadd(millisecond, tgl_sk_akh%(60000), dateadd(minute, tgl_sk_akh/(60000), '1970-01-01 00:00:00.000'))),
[luas_sk] float NULL,
[jenis_sk] varchar(17) NULL,
[pola_ht] varchar(12) NULL,
[jenis_ht] varchar(13) NULL,
[stat_prshn] varchar(13) NULL,
[stat_milik] varchar(20) NULL,
[ht_id] varchar(12) NULL,
[sumber] varchar(62) NULL,
[nosk_cabut] varchar(62) NULL,
[tglskcabut] bigint NULL, 
[tglskcabut_Date] AS (dateadd(millisecond, tglskcabut%(60000), dateadd(minute, tglskcabut/(60000), '1970-01-01 00:00:00.000'))),
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_IUPHHKHTI_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_IUPHHKHTI_shape] ON [KLHK_EN].[IUPHHKHTI](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621407.482843755,  ymin = -1121369.4962684335,  xmax = 15696048.201851575,  ymax = 629408.8882352764));
GO

IF OBJECT_ID('[KLHK_EN].[IUPHHKRE]') IS NOT NULL
	DROP TABLE [KLHK_EN].[IUPHHKRE]
GO
CREATE TABLE [KLHK_EN].[IUPHHKRE] (
[objectid] int NOT NULL,
[kode_prov] int NULL,
[nama_ha] varchar(62) NULL,
[no_sk_awal] varchar(25) NULL,
[tgl_sk_awal] bigint NULL, 
[tgl_sk_awal_Date] AS (dateadd(millisecond, tgl_sk_awal%(60000), dateadd(minute, tgl_sk_awal/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_akhir] varchar(62) NULL,
[tgl_sk_akhir] bigint NULL, 
[tgl_sk_akhir_Date] AS (dateadd(millisecond, tgl_sk_akhir%(60000), dateadd(minute, tgl_sk_akhir/(60000), '1970-01-01 00:00:00.000'))),
[luas_sk] float NULL,
[stat_prshn] varchar(11) NULL,
[stat_milik] varchar(16) NULL,
[sertifikasi_lpi] varchar(9) NULL,
[jenis_re] varchar(62) NULL,
[re_id] varchar(12) NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [CK_stat_prshn_code_domain] CHECK([stat_prshn] IN('Aktif','Tidak Aktif')),
CONSTRAINT [CK_kode_prov_code_domain] CHECK([kode_prov] IN(0,11,12,13,14,15,16,17,18,19,20,31,32,33,34,35,36,51,52,53,61,62,63,64,71,72,73,74,75,76,81,82,91,92)),
CONSTRAINT [CK_stat_milik_code_domain] CHECK([stat_milik] IN('Swasta','Penyertaan Saham')),
CONSTRAINT [CK_sertifikasi_lpi_code_domain] CHECK([sertifikasi_lpi] IN('Ada','Tidak Ada')),
CONSTRAINT [pk_KLHK_EN_IUPHHKRE_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_IUPHHKRE_shape] ON [KLHK_EN].[IUPHHKRE](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 11265929.343859946,  ymin = -376793.24774814164,  xmax = 12966581.708132457,  ymax = 177025.45567146243));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover2014]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover2014]
GO
CREATE TABLE [KLHK_EN].[LandCover2014] (
[objectid] int NOT NULL,
[k_prop] smallint NULL,
[pl14_id] int NULL,
[luas] float NULL,
[shape_leng] float NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover2014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover2014_shape] ON [KLHK_EN].[LandCover2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15717639.114466418,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover2015]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover2015]
GO
CREATE TABLE [KLHK_EN].[LandCover2015] (
[objectid] int NOT NULL,
[dbklhk_pantau_ipsdh_pl2015_k_pr] smallint NULL,
[dbklhk_sde_kode_pl_kode_veg] float NULL,
[dbklhk_sde_kode_pl_simbol] varchar(10) NULL,
[dbklhk_sde_kode_pl_kelas] varchar(36) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover2015_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover2015_shape] ON [KLHK_EN].[LandCover2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.573618984,  ymin = -1233050.6363873458,  xmax = 15717639.114458114,  ymax = 658728.3137669326));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover2016]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover2016]
GO
CREATE TABLE [KLHK_EN].[LandCover2016] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[pl16_id] int NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover2016_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover2016_shape] ON [KLHK_EN].[LandCover2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15717639.114466418,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover2017]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover2017]
GO
CREATE TABLE [KLHK_EN].[LandCover2017] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[PL17_ID_FI] int NULL,
[KELAS_2017] varchar(317) NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover2017_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover2017_Shape] ON [KLHK_EN].[LandCover2017](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10572236.5821802,  ymin = -1233050.6363851025,  xmax = 15717639.114466418,  ymax = 677753.8042168895));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover]
GO
CREATE TABLE [KLHK_EN].[LandCover] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Provinsi_1] varchar(62) NULL,
[k_prop] int NULL,
[PL_18_ID] int NULL,
[Shape_Leng] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover_Shape] ON [KLHK_EN].[LandCover](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01255798400007,  ymin = -11.008322714999963,  xmax = 141.19395446800007,  ymax = 5.906965232000051));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover2018]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover2018]
GO
CREATE TABLE [KLHK_EN].[LandCover2018] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[Provinsi_1] varchar(62) NULL,
[k_prop] smallint NULL,
[PL_18_ID] int NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover2018_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover2018_Shape] ON [KLHK_EN].[LandCover2018](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.573745267,  ymin = -1233050.636271698,  xmax = 15717639.114466418,  ymax = 658728.3110315118));
GO

IF OBJECT_ID('[KLHK_EN].[LandCover]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LandCover]
GO
CREATE TABLE [KLHK_EN].[LandCover] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[OBJECTID] int NULL,
[Provinsi] varchar(62) NULL,
[PL_19_R] int NULL,
[SHAPE_Leng] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_LandCover_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LandCover_Shape] ON [KLHK_EN].[LandCover](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.573745267,  ymin = -1233050.6363851025,  xmax = 15696048.201962898,  ymax = 658728.3111434256));
GO

IF OBJECT_ID('[KLHK_EN].[LeaseholdofForestArea]') IS NOT NULL
	DROP TABLE [KLHK_EN].[LeaseholdofForestArea]
GO
CREATE TABLE [KLHK_EN].[LeaseholdofForestArea] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[kode_prov] int NULL,
[id_ippkh] varchar(11) NULL,
[nama_ippkh] varchar(125) NULL,
[no_ippkh] varchar(62) NULL,
[tgl_ippkh] bigint NULL, 
[tgl_ippkh_Date] AS (dateadd(millisecond, tgl_ippkh%(60000), dateadd(minute, tgl_ippkh/(60000), '1970-01-01 00:00:00.000'))),
[luas_ippkh] float NULL,
[kode_guna] varchar(5) NULL,
[jenis_ippk] varchar(15) NULL,
[keterangan] varchar(62) NULL,
[tgl_berakh] bigint NULL, 
[tgl_berakh_Date] AS (dateadd(millisecond, tgl_berakh%(60000), dateadd(minute, tgl_berakh/(60000), '1970-01-01 00:00:00.000'))),
[kabupaten_] varchar(125) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_EN_LeaseholdofForestArea_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_LeaseholdofForestArea_Shape] ON [KLHK_EN].[LeaseholdofForestArea](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10623392.930861318,  ymin = -1144756.642851397,  xmax = 15670975.495310597,  ymax = 594141.9930451924));
GO

IF OBJECT_ID('[KLHK_EN].[Mangrove]') IS NOT NULL
	DROP TABLE [KLHK_EN].[Mangrove]
GO
CREATE TABLE [KLHK_EN].[Mangrove] (
[objectid] int NOT NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_Mangrove_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_Mangrove_shape] ON [KLHK_EN].[Mangrove](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10592944.060623627,  ymin = -964725.5304237846,  xmax = 14155528.69004006,  ymax = 654514.4243081689));
GO

IF OBJECT_ID('[KLHK_EN].[PeatEcologicalFunction]') IS NOT NULL
	DROP TABLE [KLHK_EN].[PeatEcologicalFunction]
GO
CREATE TABLE [KLHK_EN].[PeatEcologicalFunction] (
[objectid] int NOT NULL,
[nama_khg] varchar(125) NULL,
[kode_khg] varchar(37) NULL,
[status_khg] varchar(37) NULL,
[kubah_gmbt] varchar(37) NULL,
[feg_kghltr] varchar(62) NULL,
[luas__ha] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_PeatEcologicalFunction_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_PeatEcologicalFunction_shape] ON [KLHK_EN].[PeatEcologicalFunction](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621212.117360055,  ymin = -926516.7138912926,  xmax = 15692210.766642649,  ymax = 545217.2085017891));
GO

IF OBJECT_ID('[KLHK_EN].[PeatlandsHidrologicalUnit]') IS NOT NULL
	DROP TABLE [KLHK_EN].[PeatlandsHidrologicalUnit]
GO
CREATE TABLE [KLHK_EN].[PeatlandsHidrologicalUnit] (
[objectid] int NOT NULL,
[nama_khg] varchar(125) NULL,
[ket_status] varchar(62) NULL,
[ket_kg] varchar(62) NULL,
[keterangan] varchar(62) NULL,
[kecamatan] varchar(33) NULL,
[kabupaten] varchar(40) NULL,
[provinsi] varchar(32) NULL,
[kode_khg] varchar(25) NULL,
[luas__m2] float NULL,
[luas__ha] float NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_PeatlandsHidrologicalUnit_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_PeatlandsHidrologicalUnit_shape] ON [KLHK_EN].[PeatlandsHidrologicalUnit](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10621212.117360055,  ymin = -929062.8020683365,  xmax = 15693492.150161719,  ymax = 545217.2085017891));
GO

IF OBJECT_ID('[KLHK_EN].[PIPPIB20201stPeriod]') IS NOT NULL
	DROP TABLE [KLHK_EN].[PIPPIB20201stPeriod]
GO
CREATE TABLE [KLHK_EN].[PIPPIB20201stPeriod] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[objectid] int NULL,
[pippib20_1] varchar(25) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_KLHK_EN_PIPPIB20201stPeriod_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_PIPPIB20201stPeriod_Shape] ON [KLHK_EN].[PIPPIB20201stPeriod](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576806.797306865,  ymin = -1232970.3872867082,  xmax = 15698212.750573361,  ymax = 658757.9227367552));
GO

IF OBJECT_ID('[KLHK_EN].[RecalculatingForestAreaBoundaries]') IS NOT NULL
	DROP TABLE [KLHK_EN].[RecalculatingForestAreaBoundaries]
GO
CREATE TABLE [KLHK_EN].[RecalculatingForestAreaBoundaries] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[kodeprov] smallint NULL,
[nkws] varchar(312) NULL,
[ttbts] smallint NULL,
[blbf] varchar(3) NULL,
[babb] varchar(8) NULL,
[tbatb] bigint NULL, 
[tbatb_Date] AS (dateadd(millisecond, tbatb%(60000), dateadd(minute, tbatb/(60000), '1970-01-01 00:00:00.000'))),
[tsahbatb] bigint NULL, 
[tsahbatb_Date] AS (dateadd(millisecond, tsahbatb%(60000), dateadd(minute, tsahbatb/(60000), '1970-01-01 00:00:00.000'))),
[fungsibatb] varchar(18) NULL,
[pjbatb] float NULL,
[sumberbts] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_RecalculatingForestAreaBoundaries_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_RecalculatingForestAreaBoundaries_shape] ON [KLHK_EN].[RecalculatingForestAreaBoundaries](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576806.797306865,  ymin = -1232970.4198342145,  xmax = 15698212.751463907,  ymax = 661252.988036878));
GO

IF OBJECT_ID('[KLHK_EN].[ReleaseofForestAreaforTransmigration]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ReleaseofForestAreaforTransmigration]
GO
CREATE TABLE [KLHK_EN].[ReleaseofForestAreaforTransmigration] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODE_PROV] smallint NULL,
[NTRANS] varchar(125) NULL,
[WPPSKP] varchar(125) NULL,
[SKTRANS] varchar(125) NULL,
[TGLSKTRANS] bigint NULL, 
[TGLSKTRANS_Date] AS (dateadd(millisecond, TGLSKTRANS%(60000), dateadd(minute, TGLSKTRANS/(60000), '1970-01-01 00:00:00.000'))),
[LTRANS] float NULL,
[KETERANGAN] varchar(312) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_ReleaseofForestAreaforTransmigration_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ReleaseofForestAreaforTransmigration_SHAPE] ON [KLHK_EN].[ReleaseofForestAreaforTransmigration](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.45944831300005,  ymin = -9.516771080999945,  xmax = 140.80485058500005,  ymax = 5.3459593240000345));
GO

IF OBJECT_ID('[KLHK_EN].[ReleaseofForestArea]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ReleaseofForestArea]
GO
CREATE TABLE [KLHK_EN].[ReleaseofForestArea] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODEPROV] smallint NULL,
[NPLS] varchar(125) NULL,
[NOSKPLS] varchar(125) NULL,
[TGLSKPLS] bigint NULL, 
[TGLSKPLS_Date] AS (dateadd(millisecond, TGLSKPLS%(60000), dateadd(minute, TGLSKPLS/(60000), '1970-01-01 00:00:00.000'))),
[LSKPLS] float NULL,
[KOMODITAS] varchar(125) NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_ReleaseofForestArea_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ReleaseofForestArea_SHAPE] ON [KLHK_EN].[ReleaseofForestArea](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.28479692000008,  ymin = -8.745068937999974,  xmax = 140.98786337400009,  ymax = 5.364047928000048));
GO

IF OBJECT_ID('[KLHK_EN].[RHL2014]') IS NOT NULL
	DROP TABLE [KLHK_EN].[RHL2014]
GO
CREATE TABLE [KLHK_EN].[RHL2014] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[satker] varchar(317) NULL,
[luas_ha] float NULL,
[keterangan] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[tipe_rhl] varchar(25) NULL,
[shape_leng] float NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_RHL2014_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_RHL2014_shape] ON [KLHK_EN].[RHL2014](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10521044.50795753,  ymin = -1218766.047358459,  xmax = 15684942.949189896,  ymax = 651051.8635198071));
GO

IF OBJECT_ID('[KLHK_EN].[ForestandLandRehabilitation2015]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ForestandLandRehabilitation2015]
GO
CREATE TABLE [KLHK_EN].[ForestandLandRehabilitation2015] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[fungsi_kws] varchar(317) NULL,
[satker] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[luas_ha] float NULL,
[ket] varchar(317) NULL,
[lap_bibit] varchar(317) NULL,
[srt_pernya] varchar(317) NULL,
[foto] varchar(317) NULL,
[lab_bibit] varchar(317) NULL,
[id] int NULL,
[no_spks] varchar(317) NULL,
[kelompok] varchar(317) NULL,
[jenis] varchar(317) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_ForestandLandRehabilitation2015_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ForestandLandRehabilitation2015_shape] ON [KLHK_EN].[ForestandLandRehabilitation2015](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10521044.54268921,  ymin = -1217348.7539144494,  xmax = 15689356.808855968,  ymax = 652776.5975172351));
GO

IF OBJECT_ID('[KLHK_EN].[ForestandLandRehabilitation2016]') IS NOT NULL
	DROP TABLE [KLHK_EN].[ForestandLandRehabilitation2016]
GO
CREATE TABLE [KLHK_EN].[ForestandLandRehabilitation2016] (
[objectid] int NOT NULL,
[bpdas] varchar(317) NULL,
[provinsi] varchar(317) NULL,
[kabupaten] varchar(317) NULL,
[kecamatan] varchar(317) NULL,
[desa] varchar(317) NULL,
[fungsi_kws] varchar(317) NULL,
[satker] varchar(317) NULL,
[jenis_tana] varchar(317) NULL,
[batang] float NULL,
[luas_ha] float NULL,
[ket] varchar(317) NULL,
[jenis_rhl] varchar(317) NULL,
[kelompok] varchar(317) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_ForestandLandRehabilitation2016_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_ForestandLandRehabilitation2016_shape] ON [KLHK_EN].[ForestandLandRehabilitation2016](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 1643816.264294494,  ymin = -20683346.535252802,  xmax = 15675957.685727624,  ymax = 606324.4630364875));
GO

IF OBJECT_ID('[KLHK_EN].[RuralForest]') IS NOT NULL
	DROP TABLE [KLHK_EN].[RuralForest]
GO
CREATE TABLE [KLHK_EN].[RuralForest] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HD_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(62) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_LPHD] varchar(62) NULL,
[NO_SK_HPHD] varchar(62) NULL,
[TGL_HPHD] bigint NULL, 
[TGL_HPHD_Date] AS (dateadd(millisecond, TGL_HPHD%(60000), dateadd(minute, TGL_HPHD/(60000), '1970-01-01 00:00:00.000'))),
[NO_SK_PAK] varchar(62) NULL,
[TGL_SK_PAK] bigint NULL, 
[TGL_SK_PAK_Date] AS (dateadd(millisecond, TGL_SK_PAK%(60000), dateadd(minute, TGL_SK_PAK/(60000), '1970-01-01 00:00:00.000'))),
[LUAS_HL] float NULL,
[LUAS_HP] float NULL,
[LUAS_HPT] float NULL,
[LUAS_HPK] float NULL,
[LUAS_HPHD] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_RuralForest_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_RuralForest_SHAPE] ON [KLHK_EN].[RuralForest](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10607320.807904901,  ymin = -944304.7913925685,  xmax = 15668880.98903507,  ymax = 611851.8175949687));
GO

IF OBJECT_ID('[KLHK_EN].[SocialForest]') IS NOT NULL
	DROP TABLE [KLHK_EN].[SocialForest]
GO
CREATE TABLE [KLHK_EN].[SocialForest] (
[OBJECTID] int NOT NULL,
[SHAPE] geometry NULL,
[KODPRV] smallint NULL,
[KODKAB] smallint NULL,
[HKM_ID] int NULL,
[NAMA_PROV] varchar(62) NULL,
[NAMA_KAB] varchar(62) NULL,
[NAMA_KEC] varchar(87) NULL,
[NAMA_DESA] varchar(62) NULL,
[NAMA_HKM] varchar(62) NULL,
[NO_IUPHKM] varchar(62) NULL,
[TGL_IUPHKM] bigint NULL, 
[TGL_IUPHKM_Date] AS (dateadd(millisecond, TGL_IUPHKM%(60000), dateadd(minute, TGL_IUPHKM/(60000), '1970-01-01 00:00:00.000'))),
[NO_SK_PAK] varchar(62) NULL,
[TGL_SK_PAK] bigint NULL, 
[TGL_SK_PAK_Date] AS (dateadd(millisecond, TGL_SK_PAK%(60000), dateadd(minute, TGL_SK_PAK/(60000), '1970-01-01 00:00:00.000'))),
[L_IUPHKM] float NULL,
[LUAS_POLI] float NULL,
[SHAPE_Length] float NULL,
[SHAPE_Area] float NULL,
CONSTRAINT [pk_KLHK_EN_SocialForest_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_SocialForest_SHAPE] ON [KLHK_EN].[SocialForest](SHAPE) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10606459.160314485,  ymin = -1142365.5686552636,  xmax = 15631907.558562323,  ymax = 583387.8212839274));
GO

IF OBJECT_ID('[KLHK_EN].[WatershedBoundaries]') IS NOT NULL
	DROP TABLE [KLHK_EN].[WatershedBoundaries]
GO
CREATE TABLE [KLHK_EN].[WatershedBoundaries] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[kode_prov] int NULL,
[nama_das] varchar(62) NULL,
[luas_ha] float NULL,
[kel_m] float NULL,
[prioritas_] smallint NULL,
[kd_tematik] varchar(3) NULL,
[kd_region] smallint NULL,
[kd_lintas] smallint NULL,
[kd_das] varchar(11) NULL,
[wil_kerja] varchar(62) NULL,
[kd_urutdas] smallint NULL,
[globalid] varchar(47) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_WatershedBoundaries_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_WatershedBoundaries_shape] ON [KLHK_EN].[WatershedBoundaries](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10576749.57363394,  ymin = -1233050.6363851095,  xmax = 15696049.900475679,  ymax = 658728.3137174322));
GO

IF OBJECT_ID('[KLHK_EN].[AreaofPerformanceMeasurementREDD]') IS NOT NULL
	DROP TABLE [KLHK_EN].[AreaofPerformanceMeasurementREDD]
GO
CREATE TABLE [KLHK_EN].[AreaofPerformanceMeasurementREDD] (
[objectid] int NOT NULL,
[redd_hutan] varchar(3) NULL,
[redd_gambu] varchar(3) NULL,
[redd_type] varchar(10) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_KLHK_EN_AreaofPerformanceMeasurementREDD_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_KLHK_EN_AreaofPerformanceMeasurementREDD_shape] ON [KLHK_EN].[AreaofPerformanceMeasurementREDD](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10582026.276461776,  ymin = -1232326.7786307938,  xmax = 15698209.60368267,  ymax = 658497.5523141616));
IF OBJECT_ID('[Other].[Blok_KK]') IS NOT NULL
	DROP TABLE [Other].[Blok_KK]
GO
CREATE TABLE [Other].[Blok_KK] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[SHP_KK_4bz] varchar(25) NULL,
[SHP_KK_4_1] varchar(62) NULL,
[SHP_KK_4_2] varchar(37) NULL,
[SHP_KK_4_3] real NULL,
[SHP_KK_4_4] int NULL,
[SHP_KK_4_5] varchar(317) NULL,
[SHP_KK_4_6] float NULL,
[Sheet1__sk] varchar(317) NULL,
[Sheet1__lu] varchar(317) NULL,
[Zona_Blok] varchar(62) NULL,
[Status] varchar(62) NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_Other_Blok_KK_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_Other_Blok_KK_Shape] ON [Other].[Blok_KK](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.19618373500003,  ymin = -10.561689830999967,  xmax = 140.74300357900006,  ymax = 5.929023997000058));
GO

IF OBJECT_ID('[Other].[Profil_KK]') IS NOT NULL
	DROP TABLE [Other].[Profil_KK]
GO
CREATE TABLE [Other].[Profil_KK] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[SHP_KK_2_S] varchar(25) NULL,
[SHP_KK_2_1] varchar(62) NULL,
[SHP_KK_2_2] varchar(37) NULL,
[SHP_KK_2_3] real NULL,
[SHP_KK_2_4] int NULL,
[SHP_KK_2_5] varchar(317) NULL,
[SHP_KK_2_6] float NULL,
[SHP_KK_2_7] varchar(317) NULL,
[SHP_KK_2_8] float NULL,
[SHP_KK_2_9] varchar(317) NULL,
[SHP_KK__10] varchar(317) NULL,
[SHP_KK__11] varchar(317) NULL,
[SHP_KK__12] varchar(317) NULL,
[SHP_KK__13] varchar(317) NULL,
[SHP_KK__14] varchar(317) NULL,
[tbl_pengel] varchar(317) NULL,
[tbl_peng_1] varchar(317) NULL,
[tbl_peng_2] varchar(317) NULL,
[tbl_peng_3] varchar(317) NULL,
[tbl_peng_4] varchar(317) NULL,
[tbl_peng_5] varchar(317) NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_Other_Profil_KK_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_Other_Profil_KK_Shape] ON [Other].[Profil_KK](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10597188.673607623,  ymin = -1232970.4198342145,  xmax = 15698212.751463922,  ymax = 661252.9880368857));
GO

IF OBJECT_ID('[Other].[Zonasi_KK]') IS NOT NULL
	DROP TABLE [Other].[Zonasi_KK]
GO
CREATE TABLE [Other].[Zonasi_KK] (
[OBJECTID] int NOT NULL,
[Shape] geometry NULL,
[SHP_KK_4bz] varchar(25) NULL,
[SHP_KK_4_1] varchar(62) NULL,
[SHP_KK_4_2] varchar(37) NULL,
[SHP_KK_4_3] real NULL,
[SHP_KK_4_4] int NULL,
[SHP_KK_4_5] varchar(317) NULL,
[SHP_KK_4_6] float NULL,
[Sheet1__sk] varchar(317) NULL,
[Sheet1__lu] varchar(317) NULL,
[Zona_Blok] varchar(62) NULL,
[Status] varchar(62) NULL,
[Shape_Length] float NULL,
[Shape_Area] float NULL,
CONSTRAINT [pk_Other_Zonasi_KK_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO

CREATE SPATIAL INDEX [spidx_Other_Zonasi_KK_Shape] ON [Other].[Zonasi_KK](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10789302.05245228,  ymin = -1141257.298939973,  xmax = 15698212.751463922,  ymax = 489799.7919946897));
IF OBJECT_ID('[Publik].[Deforestasi2017_2018]') IS NOT NULL
	DROP TABLE [Publik].[Deforestasi2017_2018]
GO
CREATE TABLE [Publik].[Deforestasi2017_2018] (
[FID] int NOT NULL,
CONSTRAINT [pk_Publik_Deforestasi2017_2018_FID] PRIMARY KEY([FID])
)
GO
GO

IF OBJECT_ID('[Publik].[IUPHHKHutanAlam]') IS NOT NULL
	DROP TABLE [Publik].[IUPHHKHutanAlam]
GO
CREATE TABLE [Publik].[IUPHHKHutanAlam] (
[FID] int NOT NULL,
CONSTRAINT [pk_Publik_IUPHHKHutanAlam_FID] PRIMARY KEY([FID])
)
GO
GO

IF OBJECT_ID('[Publik].[IUPHHKHutanTanaman]') IS NOT NULL
	DROP TABLE [Publik].[IUPHHKHutanTanaman]
GO
CREATE TABLE [Publik].[IUPHHKHutanTanaman] (
[FID] int NOT NULL,
CONSTRAINT [pk_Publik_IUPHHKHutanTanaman_FID] PRIMARY KEY([FID])
)
GO
GO

IF OBJECT_ID('[Publik].[KawasanHutan]') IS NOT NULL
	DROP TABLE [Publik].[KawasanHutan]
GO
CREATE TABLE [Publik].[KawasanHutan] (
[OBJECTID] int NOT NULL,
[FGSFRF] int NULL,
[Ket_Fungsi] varchar(62) NULL,
CONSTRAINT [pk_Publik_KawasanHutan_OBJECTID] PRIMARY KEY([OBJECTID])
)
GO
GO

IF OBJECT_ID('[Publik].[IUPHHKRestorasiEkosistem]') IS NOT NULL
	DROP TABLE [Publik].[IUPHHKRestorasiEkosistem]
GO
CREATE TABLE [Publik].[IUPHHKRestorasiEkosistem] (
[FID] int NOT NULL,
CONSTRAINT [pk_Publik_IUPHHKRestorasiEkosistem_FID] PRIMARY KEY([FID])
)
GO
IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_hp_hd]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_hp_hd]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_hp_hd] (
[objectid] int NOT NULL,
[id_hphd] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_hphd] varchar(125) NULL,
[nama_desa_hphd] varchar(125) NULL,
[no_sk_hphd] varchar(250) NULL,
[tgl_sk_hphd] bigint NULL, 
[tgl_sk_hphd_Date] AS (dateadd(millisecond, tgl_sk_hphd%(60000), dateadd(minute, tgl_sk_hphd/(60000), '1970-01-01 00:00:00.000'))),
[luas_hl_hphd] float NULL,
[luas_hp_hphd] float NULL,
[luas_hpt_hphd] float NULL,
[luas_hpk_hphd] float NULL,
[luas_jml_hphd] float NULL,
[id_pak_hd] smallint NULL,
[nama_hd] varchar(125) NULL,
[id_konflik] varchar(62) NULL,
[hd_id] int NULL,
[tgl_input_hphd] bigint NULL, 
[tgl_input_hphd_Date] AS (dateadd(millisecond, tgl_input_hphd%(60000), dateadd(minute, tgl_input_hphd/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_hd] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_hp_hd_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_hp_hd_I3hd_id] ON [SINAV].[dbklhk_pkps_pskl_hp_hd](hd_id)
GO
GO

IF OBJECT_ID('[SINAV].[SPASIALHPHD]') IS NOT NULL
	DROP TABLE [SINAV].[SPASIALHPHD]
GO
CREATE TABLE [SINAV].[SPASIALHPHD] (
[objectid] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[hd_id] int NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(87) NULL,
[nama_hd] varchar(87) NULL,
[no_sk_hphd] varchar(62) NULL,
[tgl_sk_hphd] bigint NULL, 
[tgl_sk_hphd_Date] AS (dateadd(millisecond, tgl_sk_hphd%(60000), dateadd(minute, tgl_sk_hphd/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_pak_hd] varchar(62) NULL,
[tgl_sk_pak_hd] bigint NULL, 
[tgl_sk_pak_hd_Date] AS (dateadd(millisecond, tgl_sk_pak_hd%(60000), dateadd(minute, tgl_sk_pak_hd/(60000), '1970-01-01 00:00:00.000'))),
[wilayah] varchar(2) NULL,
[luas_hl] float NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_hpk] float NULL,
[luas_hphd] float NULL,
[luas_poli] float NULL,
[nama_lembaga] varchar(62) NULL,
[ketua_lembaga] varchar(62) NULL,
[kontak_lembaga] varchar(62) NULL,
[pendamping] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_SPASIALHPHD_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_SPASIALHPHD_I5hd_id] ON [SINAV].[SPASIALHPHD](hd_id)
GO

CREATE SPATIAL INDEX [spidx_SINAV_SPASIALHPHD_shape] ON [SINAV].[SPASIALHPHD](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 96.06893093900004,  ymin = -8.452012674999935,  xmax = 140.65752208800006,  ymax = 5.176126444000033));
GO

IF OBJECT_ID('[SINAV].[INDIKATIFHUTANADAT]') IS NOT NULL
	DROP TABLE [SINAV].[INDIKATIFHUTANADAT]
GO
CREATE TABLE [SINAV].[INDIKATIFHUTANADAT] (
[objectid_1] int NOT NULL,
[objectid] int NULL,
[wadmkk] varchar(62) NULL,
[wadmpr] varchar(62) NULL,
[wilayah_ad] varchar(62) NULL,
[orig_fid] int NULL,
[shape] geometry NULL,
CONSTRAINT [pk_SINAV_INDIKATIFHUTANADAT_objectid_1] PRIMARY KEY([objectid_1])
)
GO

CREATE SPATIAL INDEX [spidx_SINAV_INDIKATIFHUTANADAT_shape] ON [SINAV].[INDIKATIFHUTANADAT](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.76132162699997,  ymin = -7.1208207610000045,  xmax = 140.060539779,  ymax = 5.337364858000001));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_kemitraan_hut]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut] (
[objectid] int NOT NULL,
[id_kemitraan] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_kemitraan] varchar(125) NULL,
[nama_desa_kemitraan] varchar(125) NULL,
[id_jenis_pemegang_izin] smallint NULL,
[kegiatan_kemitraan] varchar(250) NULL,
[nama_pemegang_izin] varchar(187) NULL,
[no_kontak_pemegang_izin] varchar(62) NULL,
[no_nkk] varchar(125) NULL,
[tgl_nkk] bigint NULL, 
[tgl_nkk_Date] AS (dateadd(millisecond, tgl_nkk%(60000), dateadd(minute, tgl_nkk/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_iphps] varchar(312) NULL,
[tgl_sk_iphps] bigint NULL, 
[tgl_sk_iphps_Date] AS (dateadd(millisecond, tgl_sk_iphps%(60000), dateadd(minute, tgl_sk_iphps/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_kulinkk] varchar(312) NULL,
[tgl_sk_kulinkk] bigint NULL, 
[tgl_sk_kulinkk_Date] AS (dateadd(millisecond, tgl_sk_kulinkk%(60000), dateadd(minute, tgl_sk_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[nama_kontak_pemegang_izin] varchar(125) NULL,
[jenis_sk] varchar(62) NULL,
[luas_hl_kemitraan] float NULL,
[luas_hp_kemitraan] float NULL,
[luas_hpt_kemitraan] float NULL,
[luas_hpk_kemitraan] float NULL,
[id_konflik] varchar(62) NULL,
[luas_konservasi_kemitraan] float NULL,
[luas_kemitraan] float NULL,
[no_sk_konservasi] varchar(312) NULL,
[tgl_sk_konservasi] bigint NULL, 
[tgl_sk_konservasi_Date] AS (dateadd(millisecond, tgl_sk_konservasi%(60000), dateadd(minute, tgl_sk_konservasi/(60000), '1970-01-01 00:00:00.000'))),
[jml_kt_kemitraan] smallint NULL,
[jml_kth_kemitraan] smallint NULL,
[jml_gapoktan_kemitraan] smallint NULL,
[jml_koperasi_kemitraan] smallint NULL,
[kemitraan_id] int NULL,
[tgl_input_kemitraan] bigint NULL, 
[tgl_input_kemitraan_Date] AS (dateadd(millisecond, tgl_input_kemitraan%(60000), dateadd(minute, tgl_input_kemitraan/(60000), '1970-01-01 00:00:00.000'))),
[jml_lmdh_kemitraan] smallint NULL,
[id_usulan_kk] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_kemitraan_hut_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3kemitraan_id] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](kemitraan_id)
GO
GO

IF OBJECT_ID('[SINAV].[SPASIALIPHPS]') IS NOT NULL
	DROP TABLE [SINAV].[SPASIALIPHPS]
GO
CREATE TABLE [SINAV].[SPASIALIPHPS] (
[objectid_1] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[iphps_id] int NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(317) NULL,
[nama_iphps] varchar(317) NULL,
[no_sk_iphps] varchar(62) NULL,
[tgl_sk_iphps] bigint NULL, 
[tgl_sk_iphps_Date] AS (dateadd(millisecond, tgl_sk_iphps%(60000), dateadd(minute, tgl_sk_iphps/(60000), '1970-01-01 00:00:00.000'))),
[luas_hl] float NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_iphps] float NULL,
[luas_poli] float NULL,
[pendamping] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_SPASIALIPHPS_objectid_1] PRIMARY KEY([objectid_1])
)CREATE INDEX [SINAV_SPASIALIPHPS_I5iphps_id] ON [SINAV].[SPASIALIPHPS](iphps_id)
GO

CREATE SPATIAL INDEX [spidx_SINAV_SPASIALIPHPS_shape] ON [SINAV].[SPASIALIPHPS](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 106.59658314200004,  ymin = -8.44796055699993,  xmax = 113.41689899500011,  ymax = -5.946823265999967));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_iuphhkhtr]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_iuphhkhtr]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_iuphhkhtr] (
[objectid] int NOT NULL,
[id_iuphhkhtr] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_iuphhkhtr] varchar(125) NULL,
[nama_desa_iuphhkhtr] varchar(125) NULL,
[no_sk_iuphhkhtr] varchar(250) NULL,
[tgl_sk_iuphhkhtr] bigint NULL, 
[tgl_sk_iuphhkhtr_Date] AS (dateadd(millisecond, tgl_sk_iuphhkhtr%(60000), dateadd(minute, tgl_sk_iuphhkhtr/(60000), '1970-01-01 00:00:00.000'))),
[luas_hp_iuphhkhtr] float NULL,
[luas_hpt_iuphhkhtr] float NULL,
[luas_hpk_iuphhkhtr] float NULL,
[luas_jml_iuphhkhtr] float NULL,
[id_pencadangan_htr] smallint NULL,
[jml_kth_iuphhkhtr] smallint NULL,
[jml_gapoktan_iuphhkhtr] smallint NULL,
[jml_koperasi_iuphhkhtr] smallint NULL,
[jml_perorangan_iuphhkhtr] smallint NULL,
[nama_htr] varchar(125) NULL,
[id_konflik] varchar(62) NULL,
[jml_kt_iuphhkhtr] smallint NULL,
[htr_id] int NULL,
[tgl_input_iuphhkhtr] bigint NULL, 
[tgl_input_iuphhkhtr_Date] AS (dateadd(millisecond, tgl_input_iuphhkhtr%(60000), dateadd(minute, tgl_input_iuphhkhtr/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_htr] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_iuphhkhtr_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_iuphhkhtr_I3htr_id] ON [SINAV].[dbklhk_pkps_pskl_iuphhkhtr](htr_id)
GO
GO

IF OBJECT_ID('[SINAV].[SPASIALIUPHHKHTR]') IS NOT NULL
	DROP TABLE [SINAV].[SPASIALIUPHHKHTR]
GO
CREATE TABLE [SINAV].[SPASIALIUPHHKHTR] (
[objectid] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[htr_id] int NULL,
[nama_prov] varchar(87) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(87) NULL,
[nama_htr] varchar(87) NULL,
[no_sk_iuphhkhtr] varchar(62) NULL,
[tgl_sk_iuphhkhtr] bigint NULL, 
[tgl_sk_iuphhkhtr_Date] AS (dateadd(millisecond, tgl_sk_iuphhkhtr%(60000), dateadd(minute, tgl_sk_iuphhkhtr/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_pencadangan] varchar(62) NULL,
[tgl_sk_pencadangan] bigint NULL, 
[tgl_sk_pencadangan_Date] AS (dateadd(millisecond, tgl_sk_pencadangan%(60000), dateadd(minute, tgl_sk_pencadangan/(60000), '1970-01-01 00:00:00.000'))),
[wilayah] varchar(2) NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_hpk] float NULL,
[luas_iuphhkhtr] float NULL,
[luas_poli] float NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_SPASIALIUPHHKHTR_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_SPASIALIUPHHKHTR_I5htr_id] ON [SINAV].[SPASIALIUPHHKHTR](htr_id)
GO

CREATE SPATIAL INDEX [spidx_SINAV_SPASIALIUPHHKHTR_shape] ON [SINAV].[SPASIALIUPHHKHTR](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 99.25456498000005,  ymin = -9.835022331999937,  xmax = 136.07606086700002,  ymax = 4.208120291000057));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_iup_hkm]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_iup_hkm]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_iup_hkm] (
[objectid] int NOT NULL,
[id_iuphkm] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_iuphkm] varchar(125) NULL,
[nama_desa_iuphkm] varchar(125) NULL,
[no_sk_iuphkm] varchar(250) NULL,
[tgl_sk_iuphkm] bigint NULL, 
[tgl_sk_iuphkm_Date] AS (dateadd(millisecond, tgl_sk_iuphkm%(60000), dateadd(minute, tgl_sk_iuphkm/(60000), '1970-01-01 00:00:00.000'))),
[luas_hl_iuphkm] float NULL,
[luas_hp_iuphkm] float NULL,
[luas_hpt_iuphkm] float NULL,
[luas_hpk_iuphkm] float NULL,
[luas_jml_iuphkm] float NULL,
[id_pak_hkm] smallint NULL,
[jml_kth_iuphkm] smallint NULL,
[jml_gapoktan_iuphkm] smallint NULL,
[jml_koperasi_iuphkm] smallint NULL,
[nama_hkm] varchar(125) NULL,
[jml_kt_iuphkm] smallint NULL,
[id_konflik] varchar(62) NULL,
[hkm_id] int NULL,
[tgl_input_iuphkm] bigint NULL, 
[tgl_input_iuphkm_Date] AS (dateadd(millisecond, tgl_input_iuphkm%(60000), dateadd(minute, tgl_input_iuphkm/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_hkm] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_iup_hkm_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_iup_hkm_I3hkm_id] ON [SINAV].[dbklhk_pkps_pskl_iup_hkm](hkm_id)
GO
GO

IF OBJECT_ID('[SINAV].[SPASIALIUPHKM]') IS NOT NULL
	DROP TABLE [SINAV].[SPASIALIUPHKM]
GO
CREATE TABLE [SINAV].[SPASIALIUPHKM] (
[objectid] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[hkm_id] int NULL,
[nama_prov] varchar(75) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(87) NULL,
[nama_hkm] varchar(62) NULL,
[no_sk_iuphkm] varchar(62) NULL,
[tgl_sk_iuphkm] bigint NULL, 
[tgl_sk_iuphkm_Date] AS (dateadd(millisecond, tgl_sk_iuphkm%(60000), dateadd(minute, tgl_sk_iuphkm/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_pak_hkm] varchar(62) NULL,
[tgl_sk_pak_hkm] bigint NULL, 
[tgl_sk_pak_hkm_Date] AS (dateadd(millisecond, tgl_sk_pak_hkm%(60000), dateadd(minute, tgl_sk_pak_hkm/(60000), '1970-01-01 00:00:00.000'))),
[wilayah] varchar(2) NULL,
[luas_hl] float NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_hpk] float NULL,
[luas_iuphkm] float NULL,
[luas_poli] float NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_SPASIALIUPHKM_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_SPASIALIUPHKM_I5hkm_id] ON [SINAV].[SPASIALIUPHKM](hkm_id)
GO

CREATE SPATIAL INDEX [spidx_SINAV_SPASIALIUPHKM_shape] ON [SINAV].[SPASIALIUPHKM](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 97.37793938100003,  ymin = -10.151481675999946,  xmax = 131.35209884100004,  ymax = 4.11504547800007));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_kemitraan_hut]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut] (
[objectid] int NOT NULL,
[id_kemitraan] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_kemitraan] varchar(125) NULL,
[nama_desa_kemitraan] varchar(125) NULL,
[id_jenis_pemegang_izin] smallint NULL,
[kegiatan_kemitraan] varchar(250) NULL,
[nama_pemegang_izin] varchar(187) NULL,
[no_kontak_pemegang_izin] varchar(62) NULL,
[no_nkk] varchar(125) NULL,
[tgl_nkk] bigint NULL, 
[tgl_nkk_Date] AS (dateadd(millisecond, tgl_nkk%(60000), dateadd(minute, tgl_nkk/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_iphps] varchar(312) NULL,
[tgl_sk_iphps] bigint NULL, 
[tgl_sk_iphps_Date] AS (dateadd(millisecond, tgl_sk_iphps%(60000), dateadd(minute, tgl_sk_iphps/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_kulinkk] varchar(312) NULL,
[tgl_sk_kulinkk] bigint NULL, 
[tgl_sk_kulinkk_Date] AS (dateadd(millisecond, tgl_sk_kulinkk%(60000), dateadd(minute, tgl_sk_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[nama_kontak_pemegang_izin] varchar(125) NULL,
[jenis_sk] varchar(62) NULL,
[luas_hl_kemitraan] float NULL,
[luas_hp_kemitraan] float NULL,
[luas_hpt_kemitraan] float NULL,
[luas_hpk_kemitraan] float NULL,
[id_konflik] varchar(62) NULL,
[luas_konservasi_kemitraan] float NULL,
[luas_kemitraan] float NULL,
[no_sk_konservasi] varchar(312) NULL,
[tgl_sk_konservasi] bigint NULL, 
[tgl_sk_konservasi_Date] AS (dateadd(millisecond, tgl_sk_konservasi%(60000), dateadd(minute, tgl_sk_konservasi/(60000), '1970-01-01 00:00:00.000'))),
[jml_kt_kemitraan] smallint NULL,
[jml_kth_kemitraan] smallint NULL,
[jml_gapoktan_kemitraan] smallint NULL,
[jml_koperasi_kemitraan] smallint NULL,
[kemitraan_id] int NULL,
[tgl_input_kemitraan] bigint NULL, 
[tgl_input_kemitraan_Date] AS (dateadd(millisecond, tgl_input_kemitraan%(60000), dateadd(minute, tgl_input_kemitraan/(60000), '1970-01-01 00:00:00.000'))),
[jml_lmdh_kemitraan] smallint NULL,
[id_usulan_kk] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_kemitraan_hut_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3kemitraan_id] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](kemitraan_id)
GO
GO

IF OBJECT_ID('[SINAV].[SPASIALKULINKK]') IS NOT NULL
	DROP TABLE [SINAV].[SPASIALKULINKK]
GO
CREATE TABLE [SINAV].[SPASIALKULINKK] (
[objectid] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[kulinkk_id] int NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(317) NULL,
[pemegang_izin] varchar(125) NULL,
[kelompok] varchar(125) NULL,
[anak_petak] varchar(62) NULL,
[no_sk_kulinkk] varchar(125) NULL,
[tgl_sk_kulinkk] bigint NULL, 
[tgl_sk_kulinkk_Date] AS (dateadd(millisecond, tgl_sk_kulinkk%(60000), dateadd(minute, tgl_sk_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[wilayah] int NULL,
[luas_hl] float NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_hpk] float NULL,
[luas_kulinkk] float NULL,
[luas_poli] float NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_SPASIALKULINKK_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_SPASIALKULINKK_I5kulinkk_id] ON [SINAV].[SPASIALKULINKK](kulinkk_id)
GO

CREATE SPATIAL INDEX [spidx_SINAV_SPASIALKULINKK_shape] ON [SINAV].[SPASIALKULINKK](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 98.24440004500008,  ymin = -8.416706485999953,  xmax = 117.62154965400009,  ymax = 4.07592463900005));
GO

IF OBJECT_ID('[SINAV].[PENETAPANPENCANTUMANHUTANADAT]') IS NOT NULL
	DROP TABLE [SINAV].[PENETAPANPENCANTUMANHUTANADAT]
GO
CREATE TABLE [SINAV].[PENETAPANPENCANTUMANHUTANADAT] (
[objectid] int NOT NULL,
[wadmkk] varchar(62) NULL,
[wadmpr] varchar(62) NULL,
[wilayah_ad] varchar(62) NULL,
[luas_1] float NULL,
[fkaw] varchar(62) NULL,
[ket_tahap] varchar(312) NULL,
[region] varchar(125) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_SINAV_PENETAPANPENCANTUMANHUTANADAT_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_SINAV_PENETAPANPENCANTUMANHUTANADAT_shape] ON [SINAV].[PENETAPANPENCANTUMANHUTANADAT](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 101.32277720600001,  ymin = -8.508531258000005,  xmax = 121.72183275199995,  ymax = 1.1483015919999957));
GO

IF OBJECT_ID('[SINAV].[PIAPSRevII]') IS NOT NULL
	DROP TABLE [SINAV].[PIAPSRevII]
GO
CREATE TABLE [SINAV].[PIAPSRevII] (
[objectid] int NOT NULL,
[provno] varchar(2) NULL,
[kabkotno] varchar(2) NULL,
[provinsi] varchar(62) NULL,
[kabkot] varchar(62) NULL,
[kecamatan] varchar(62) NULL,
[desa] varchar(62) NULL,
[fungsi] varchar(12) NULL,
[kriteria] varchar(125) NULL,
[luas_ha] float NULL,
[shape_leng] float NULL,
[shape_le_1] float NULL,
[luas_total] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_SINAV_PIAPSRevII_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_SINAV_PIAPSRevII_shape] ON [SINAV].[PIAPSRevII](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.260982189,  ymin = -10.818092017000026,  xmax = 141.00000190699996,  ymax = 5.849857601999986));
GO

IF OBJECT_ID('[SINAV].[PIAPSRevIII]') IS NOT NULL
	DROP TABLE [SINAV].[PIAPSRevIII]
GO
CREATE TABLE [SINAV].[PIAPSRevIII] (
[objectid] int NOT NULL,
[provno] varchar(2) NULL,
[kabkotno] varchar(2) NULL,
[provinsi] varchar(62) NULL,
[kabkot] varchar(62) NULL,
[fungsi] varchar(62) NULL,
[kriteria] varchar(62) NULL,
[luas_ha] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_SINAV_PIAPSRevIII_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_SINAV_PIAPSRevIII_shape] ON [SINAV].[PIAPSRevIII](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.260982189,  ymin = -10.836881633000019,  xmax = 141.00000190699996,  ymax = 5.849857601999986));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_hp_hd]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_hp_hd]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_hp_hd] (
[objectid] int NOT NULL,
[id_hphd] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_hphd] varchar(125) NULL,
[nama_desa_hphd] varchar(125) NULL,
[no_sk_hphd] varchar(250) NULL,
[tgl_sk_hphd] bigint NULL, 
[tgl_sk_hphd_Date] AS (dateadd(millisecond, tgl_sk_hphd%(60000), dateadd(minute, tgl_sk_hphd/(60000), '1970-01-01 00:00:00.000'))),
[luas_hl_hphd] float NULL,
[luas_hp_hphd] float NULL,
[luas_hpt_hphd] float NULL,
[luas_hpk_hphd] float NULL,
[luas_jml_hphd] float NULL,
[id_pak_hd] smallint NULL,
[nama_hd] varchar(125) NULL,
[id_konflik] varchar(62) NULL,
[hd_id] int NULL,
[tgl_input_hphd] bigint NULL, 
[tgl_input_hphd_Date] AS (dateadd(millisecond, tgl_input_hphd%(60000), dateadd(minute, tgl_input_hphd/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_hd] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_hp_hd_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_hp_hd_I3hd_id] ON [SINAV].[dbklhk_pkps_pskl_hp_hd](hd_id)
GO

CREATE INDEX [SINAV_dbklhk_pkps_pskl_hp_hd_I3id_usulan_hd] ON [SINAV].[dbklhk_pkps_pskl_hp_hd](id_usulan_hd)
GO
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_usulan_hd]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_usulan_hd]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_usulan_hd] (
[objectid] int NOT NULL,
[id_usulan_hd] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(62) NULL,
[nama_kec] varchar(62) NULL,
[nama_desa] varchar(62) NULL,
[no_usulan_hd] varchar(62) NULL,
[tgl_usulan_hd] bigint NULL, 
[tgl_usulan_hd_Date] AS (dateadd(millisecond, tgl_usulan_hd%(60000), dateadd(minute, tgl_usulan_hd/(60000), '1970-01-01 00:00:00.000'))),
[nama_kelompok] varchar(62) NULL,
[luas_usulan_hl] float NULL,
[luas_usulan_hp] float NULL,
[luas_usulan_hpt] float NULL,
[luas_usulan_hpk] float NULL,
[luas_usulan_total] float NULL,
[proses_usulan] varchar(62) NULL,
[tgl_proses_usulan] bigint NULL, 
[tgl_proses_usulan_Date] AS (dateadd(millisecond, tgl_proses_usulan%(60000), dateadd(minute, tgl_proses_usulan/(60000), '1970-01-01 00:00:00.000'))),
[no_sk] varchar(62) NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[penelaah] varchar(62) NULL,
[nama_kph] varchar(62) NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_usulan_hd_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_usulan_hd_I5id_usulan_hd] ON [SINAV].[dbklhk_pkps_pskl_usulan_hd](id_usulan_hd)
GO

CREATE SPATIAL INDEX [spidx_SINAV_dbklhk_pkps_pskl_usulan_hd_shape] ON [SINAV].[dbklhk_pkps_pskl_usulan_hd](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.28718405200004,  ymin = -8.299144482999964,  xmax = 134.54603575300007,  ymax = 5.487947716000065));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_iup_hkm]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_iup_hkm]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_iup_hkm] (
[objectid] int NOT NULL,
[id_iuphkm] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_iuphkm] varchar(125) NULL,
[nama_desa_iuphkm] varchar(125) NULL,
[no_sk_iuphkm] varchar(250) NULL,
[tgl_sk_iuphkm] bigint NULL, 
[tgl_sk_iuphkm_Date] AS (dateadd(millisecond, tgl_sk_iuphkm%(60000), dateadd(minute, tgl_sk_iuphkm/(60000), '1970-01-01 00:00:00.000'))),
[luas_hl_iuphkm] float NULL,
[luas_hp_iuphkm] float NULL,
[luas_hpt_iuphkm] float NULL,
[luas_hpk_iuphkm] float NULL,
[luas_jml_iuphkm] float NULL,
[id_pak_hkm] smallint NULL,
[jml_kth_iuphkm] smallint NULL,
[jml_gapoktan_iuphkm] smallint NULL,
[jml_koperasi_iuphkm] smallint NULL,
[nama_hkm] varchar(125) NULL,
[jml_kt_iuphkm] smallint NULL,
[id_konflik] varchar(62) NULL,
[hkm_id] int NULL,
[tgl_input_iuphkm] bigint NULL, 
[tgl_input_iuphkm_Date] AS (dateadd(millisecond, tgl_input_iuphkm%(60000), dateadd(minute, tgl_input_iuphkm/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_hkm] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_iup_hkm_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_iup_hkm_I3hkm_id] ON [SINAV].[dbklhk_pkps_pskl_iup_hkm](hkm_id)
GO

CREATE INDEX [SINAV_dbklhk_pkps_pskl_iup_hkm_I3id_usulan_hkm] ON [SINAV].[dbklhk_pkps_pskl_iup_hkm](id_usulan_hkm)
GO
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_usulan_hkm]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_usulan_hkm]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_usulan_hkm] (
[objectid] int NOT NULL,
[id_usulan_hkm] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(62) NULL,
[nama_kec] varchar(62) NULL,
[nama_desa] varchar(62) NULL,
[no_usulan_hkm] varchar(62) NULL,
[tgl_usulan_hkm] bigint NULL, 
[tgl_usulan_hkm_Date] AS (dateadd(millisecond, tgl_usulan_hkm%(60000), dateadd(minute, tgl_usulan_hkm/(60000), '1970-01-01 00:00:00.000'))),
[nama_kelompok] varchar(62) NULL,
[luas_usulan_hl] float NULL,
[luas_usulan_hp] float NULL,
[luas_usulan_hpt] float NULL,
[luas_usulan_hpk] float NULL,
[luas_usulan_total] float NULL,
[proses_usulan] varchar(62) NULL,
[tgl_proses_usulan] bigint NULL, 
[tgl_proses_usulan_Date] AS (dateadd(millisecond, tgl_proses_usulan%(60000), dateadd(minute, tgl_proses_usulan/(60000), '1970-01-01 00:00:00.000'))),
[no_sk] varchar(62) NULL,
[shape] geometry NULL,
[penelaah] varchar(62) NULL,
[nama_kph] varchar(62) NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_usulan_hkm_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_usulan_hkm_I5id_usulan_hkm] ON [SINAV].[dbklhk_pkps_pskl_usulan_hkm](id_usulan_hkm)
GO

CREATE SPATIAL INDEX [spidx_SINAV_dbklhk_pkps_pskl_usulan_hkm_shape] ON [SINAV].[dbklhk_pkps_pskl_usulan_hkm](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 96.53006947400007,  ymin = -9.629830604999938,  xmax = 119.95738509400007,  ymax = 5.0893426090000276));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_iuphhkhtr]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_iuphhkhtr]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_iuphhkhtr] (
[objectid] int NOT NULL,
[id_iuphhkhtr] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_iuphhkhtr] varchar(125) NULL,
[nama_desa_iuphhkhtr] varchar(125) NULL,
[no_sk_iuphhkhtr] varchar(250) NULL,
[tgl_sk_iuphhkhtr] bigint NULL, 
[tgl_sk_iuphhkhtr_Date] AS (dateadd(millisecond, tgl_sk_iuphhkhtr%(60000), dateadd(minute, tgl_sk_iuphhkhtr/(60000), '1970-01-01 00:00:00.000'))),
[luas_hp_iuphhkhtr] float NULL,
[luas_hpt_iuphhkhtr] float NULL,
[luas_hpk_iuphhkhtr] float NULL,
[luas_jml_iuphhkhtr] float NULL,
[id_pencadangan_htr] smallint NULL,
[jml_kth_iuphhkhtr] smallint NULL,
[jml_gapoktan_iuphhkhtr] smallint NULL,
[jml_koperasi_iuphhkhtr] smallint NULL,
[jml_perorangan_iuphhkhtr] smallint NULL,
[nama_htr] varchar(125) NULL,
[id_konflik] varchar(62) NULL,
[jml_kt_iuphhkhtr] smallint NULL,
[htr_id] int NULL,
[tgl_input_iuphhkhtr] bigint NULL, 
[tgl_input_iuphhkhtr_Date] AS (dateadd(millisecond, tgl_input_iuphhkhtr%(60000), dateadd(minute, tgl_input_iuphhkhtr/(60000), '1970-01-01 00:00:00.000'))),
[id_usulan_htr] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_iuphhkhtr_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_iuphhkhtr_I3htr_id] ON [SINAV].[dbklhk_pkps_pskl_iuphhkhtr](htr_id)
GO

CREATE INDEX [SINAV_dbklhk_pkps_pskl_iuphhkhtr_I3id_usulan_htr] ON [SINAV].[dbklhk_pkps_pskl_iuphhkhtr](id_usulan_htr)
GO
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_usulan_htr]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_usulan_htr]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_usulan_htr] (
[objectid] int NOT NULL,
[id_usulan_htr] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(62) NULL,
[nama_kec] varchar(62) NULL,
[nama_desa] varchar(62) NULL,
[no_usulan_htr] varchar(62) NULL,
[tgl_usulan_htr] bigint NULL, 
[tgl_usulan_htr_Date] AS (dateadd(millisecond, tgl_usulan_htr%(60000), dateadd(minute, tgl_usulan_htr/(60000), '1970-01-01 00:00:00.000'))),
[nama_kelompok] varchar(62) NULL,
[luas_usulan_hp] float NULL,
[luas_usulan_hpt] float NULL,
[luas_usulan_hpk] float NULL,
[luas_usulan_total] float NULL,
[proses_usulan] varchar(62) NULL,
[tgl_proses_usulan] bigint NULL, 
[tgl_proses_usulan_Date] AS (dateadd(millisecond, tgl_proses_usulan%(60000), dateadd(minute, tgl_proses_usulan/(60000), '1970-01-01 00:00:00.000'))),
[no_sk] varchar(62) NULL,
[st_area_shape_] float NULL,
[st_length_shape_] float NULL,
[shape] geometry NULL,
[penelaah] varchar(62) NULL,
[nama_kph] varchar(62) NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_usulan_htr_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_usulan_htr_I5id_usulan_htr] ON [SINAV].[dbklhk_pkps_pskl_usulan_htr](id_usulan_htr)
GO

CREATE SPATIAL INDEX [spidx_SINAV_dbklhk_pkps_pskl_usulan_htr_shape] ON [SINAV].[dbklhk_pkps_pskl_usulan_htr](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 99.03407200500004,  ymin = -10.07990214199998,  xmax = 124.43297454600008,  ymax = 2.775054467000075));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_kemitraan_hut]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut] (
[objectid] int NOT NULL,
[id_kemitraan] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_kemitraan] varchar(125) NULL,
[nama_desa_kemitraan] varchar(125) NULL,
[id_jenis_pemegang_izin] smallint NULL,
[kegiatan_kemitraan] varchar(250) NULL,
[nama_pemegang_izin] varchar(187) NULL,
[no_kontak_pemegang_izin] varchar(62) NULL,
[no_nkk] varchar(125) NULL,
[tgl_nkk] bigint NULL, 
[tgl_nkk_Date] AS (dateadd(millisecond, tgl_nkk%(60000), dateadd(minute, tgl_nkk/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_iphps] varchar(312) NULL,
[tgl_sk_iphps] bigint NULL, 
[tgl_sk_iphps_Date] AS (dateadd(millisecond, tgl_sk_iphps%(60000), dateadd(minute, tgl_sk_iphps/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_kulinkk] varchar(312) NULL,
[tgl_sk_kulinkk] bigint NULL, 
[tgl_sk_kulinkk_Date] AS (dateadd(millisecond, tgl_sk_kulinkk%(60000), dateadd(minute, tgl_sk_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[nama_kontak_pemegang_izin] varchar(125) NULL,
[jenis_sk] varchar(62) NULL,
[luas_hl_kemitraan] float NULL,
[luas_hp_kemitraan] float NULL,
[luas_hpt_kemitraan] float NULL,
[luas_hpk_kemitraan] float NULL,
[id_konflik] varchar(62) NULL,
[luas_konservasi_kemitraan] float NULL,
[luas_kemitraan] float NULL,
[no_sk_konservasi] varchar(312) NULL,
[tgl_sk_konservasi] bigint NULL, 
[tgl_sk_konservasi_Date] AS (dateadd(millisecond, tgl_sk_konservasi%(60000), dateadd(minute, tgl_sk_konservasi/(60000), '1970-01-01 00:00:00.000'))),
[jml_kt_kemitraan] smallint NULL,
[jml_kth_kemitraan] smallint NULL,
[jml_gapoktan_kemitraan] smallint NULL,
[jml_koperasi_kemitraan] smallint NULL,
[kemitraan_id] int NULL,
[tgl_input_kemitraan] bigint NULL, 
[tgl_input_kemitraan_Date] AS (dateadd(millisecond, tgl_input_kemitraan%(60000), dateadd(minute, tgl_input_kemitraan/(60000), '1970-01-01 00:00:00.000'))),
[jml_lmdh_kemitraan] smallint NULL,
[id_usulan_kk] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_kemitraan_hut_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3kemitraan_id] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](kemitraan_id)
GO

CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3id_usulan_kk] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](id_usulan_kk)
GO
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_usulan_iphps]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_usulan_iphps]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_usulan_iphps] (
[objectid] int NOT NULL,
[id_usulan_iphps] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(62) NULL,
[nama_kec] varchar(62) NULL,
[nama_desa] varchar(62) NULL,
[no_usulan_iphps] varchar(62) NULL,
[tgl_usulan_iphps] bigint NULL, 
[tgl_usulan_iphps_Date] AS (dateadd(millisecond, tgl_usulan_iphps%(60000), dateadd(minute, tgl_usulan_iphps/(60000), '1970-01-01 00:00:00.000'))),
[nama_kelompok] varchar(62) NULL,
[luas_usulan_hl] float NULL,
[luas_usulan_hp] float NULL,
[luas_usulan_hpt] float NULL,
[luas_usulan_hpk] float NULL,
[luas_usulan_total] float NULL,
[proses_usulan] varchar(62) NULL,
[tgl_proses_usulan] bigint NULL, 
[tgl_proses_usulan_Date] AS (dateadd(millisecond, tgl_proses_usulan%(60000), dateadd(minute, tgl_proses_usulan/(60000), '1970-01-01 00:00:00.000'))),
[no_sk] varchar(62) NULL,
[shape] geometry NULL,
[penelaah] varchar(62) NULL,
[nama_kph] varchar(62) NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_usulan_iphps_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_usulan_iphps_I5id_usulan_iphp] ON [SINAV].[dbklhk_pkps_pskl_usulan_iphps](id_usulan_iphps)
GO

CREATE SPATIAL INDEX [spidx_SINAV_dbklhk_pkps_pskl_usulan_iphps_shape] ON [SINAV].[dbklhk_pkps_pskl_usulan_iphps](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 114.024118595,  ymin = -8.552478343999951,  xmax = 114.35918235500003,  ymax = -8.430739194999944));
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_kemitraan_hut]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_kemitraan_hut] (
[objectid] int NOT NULL,
[id_kemitraan] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_kec_kemitraan] varchar(125) NULL,
[nama_desa_kemitraan] varchar(125) NULL,
[id_jenis_pemegang_izin] smallint NULL,
[kegiatan_kemitraan] varchar(250) NULL,
[nama_pemegang_izin] varchar(187) NULL,
[no_kontak_pemegang_izin] varchar(62) NULL,
[no_nkk] varchar(125) NULL,
[tgl_nkk] bigint NULL, 
[tgl_nkk_Date] AS (dateadd(millisecond, tgl_nkk%(60000), dateadd(minute, tgl_nkk/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_iphps] varchar(312) NULL,
[tgl_sk_iphps] bigint NULL, 
[tgl_sk_iphps_Date] AS (dateadd(millisecond, tgl_sk_iphps%(60000), dateadd(minute, tgl_sk_iphps/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_kulinkk] varchar(312) NULL,
[tgl_sk_kulinkk] bigint NULL, 
[tgl_sk_kulinkk_Date] AS (dateadd(millisecond, tgl_sk_kulinkk%(60000), dateadd(minute, tgl_sk_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[nama_kontak_pemegang_izin] varchar(125) NULL,
[jenis_sk] varchar(62) NULL,
[luas_hl_kemitraan] float NULL,
[luas_hp_kemitraan] float NULL,
[luas_hpt_kemitraan] float NULL,
[luas_hpk_kemitraan] float NULL,
[id_konflik] varchar(62) NULL,
[luas_konservasi_kemitraan] float NULL,
[luas_kemitraan] float NULL,
[no_sk_konservasi] varchar(312) NULL,
[tgl_sk_konservasi] bigint NULL, 
[tgl_sk_konservasi_Date] AS (dateadd(millisecond, tgl_sk_konservasi%(60000), dateadd(minute, tgl_sk_konservasi/(60000), '1970-01-01 00:00:00.000'))),
[jml_kt_kemitraan] smallint NULL,
[jml_kth_kemitraan] smallint NULL,
[jml_gapoktan_kemitraan] smallint NULL,
[jml_koperasi_kemitraan] smallint NULL,
[kemitraan_id] int NULL,
[tgl_input_kemitraan] bigint NULL, 
[tgl_input_kemitraan_Date] AS (dateadd(millisecond, tgl_input_kemitraan%(60000), dateadd(minute, tgl_input_kemitraan/(60000), '1970-01-01 00:00:00.000'))),
[jml_lmdh_kemitraan] smallint NULL,
[id_usulan_kk] smallint NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_kemitraan_hut_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3kemitraan_id] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](kemitraan_id)
GO

CREATE INDEX [SINAV_dbklhk_pkps_pskl_kemitraan_hut_I3id_usulan_kk] ON [SINAV].[dbklhk_pkps_pskl_kemitraan_hut](id_usulan_kk)
GO
GO

IF OBJECT_ID('[SINAV].[dbklhk_pkps_pskl_usulan_kulinkk]') IS NOT NULL
	DROP TABLE [SINAV].[dbklhk_pkps_pskl_usulan_kulinkk]
GO
CREATE TABLE [SINAV].[dbklhk_pkps_pskl_usulan_kulinkk] (
[objectid] int NOT NULL,
[id_usulan_kulinkk] smallint NULL,
[kodprv] smallint NULL,
[kodkab] smallint NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(62) NULL,
[nama_kec] varchar(62) NULL,
[nama_desa] varchar(62) NULL,
[no_usulan_kulinkk] varchar(62) NULL,
[tgl_usulan_kulinkk] bigint NULL, 
[tgl_usulan_kulinkk_Date] AS (dateadd(millisecond, tgl_usulan_kulinkk%(60000), dateadd(minute, tgl_usulan_kulinkk/(60000), '1970-01-01 00:00:00.000'))),
[nama_kelompok] varchar(62) NULL,
[luas_usulan_hl] float NULL,
[luas_usulan_hp] float NULL,
[luas_usulan_hpt] float NULL,
[luas_usulan_hpk] float NULL,
[luas_usulan_total] float NULL,
[proses_usulan] varchar(62) NULL,
[tgl_proses_usulan] bigint NULL, 
[tgl_proses_usulan_Date] AS (dateadd(millisecond, tgl_proses_usulan%(60000), dateadd(minute, tgl_proses_usulan/(60000), '1970-01-01 00:00:00.000'))),
[no_sk] varchar(62) NULL,
[shape] geometry NULL,
[penelaah] varchar(62) NULL,
[nama_kph] varchar(62) NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_SINAV_dbklhk_pkps_pskl_usulan_kulinkk_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [SINAV_dbklhk_pkps_pskl_usulan_kulinkk_I5id_usulan_kuli] ON [SINAV].[dbklhk_pkps_pskl_usulan_kulinkk](id_usulan_kulinkk)
GO

CREATE SPATIAL INDEX [spidx_SINAV_dbklhk_pkps_pskl_usulan_kulinkk_shape] ON [SINAV].[dbklhk_pkps_pskl_usulan_kulinkk](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 99.23273085400007,  ymin = -8.634736241999974,  xmax = 115.56227071500007,  ymax = 2.6630199500000344));
IF OBJECT_ID('[test].[AdminProv]') IS NOT NULL
	DROP TABLE [test].[AdminProv]
GO
CREATE TABLE [test].[AdminProv] (
[FID] int NOT NULL,
[Shape] geometry NULL,
[objectid] int NULL,
[kw] varchar(8) NULL,
[wa] varchar(50) NULL,
[ta] varchar(18) NULL,
[dh] varchar(27) NULL,
[wi] varchar(50) NULL,
[lsh] varchar(18) NULL,
[lu] float NULL,
[ket] varchar(18) NULL,
[st_area_sh] float NULL,
[st_length_] float NULL,
CONSTRAINT [pk_test_AdminProv_FID] PRIMARY KEY([FID])
)
GO

CREATE SPATIAL INDEX [spidx_test_AdminProv_Shape] ON [test].[AdminProv](Shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10572308.484441176,  ymin = -1232970.3872867082,  xmax = 15699380.711553814,  ymax = 677753.8042168831));
GO

IF OBJECT_ID('[test].[dbklhk_jds_pktl_PIAPS_Revisi_1_2017]') IS NOT NULL
	DROP TABLE [test].[dbklhk_jds_pktl_PIAPS_Revisi_1_2017]
GO
CREATE TABLE [test].[dbklhk_jds_pktl_PIAPS_Revisi_1_2017] (
[objectid] int NOT NULL,
[kode_prov] int NULL,
[shape_leng] float NULL,
[luas_ha] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_jds_pktl_PIAPS_Revisi_1_2017_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_jds_pktl_PIAPS_Revisi_1_2017_shape] ON [test].[dbklhk_jds_pktl_PIAPS_Revisi_1_2017](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.28660365773362,  ymin = -10.818092016732408,  xmax = 140.99999999170734,  ymax = 5.37118399774414));
GO

IF OBJECT_ID('[test].[PIAPS]') IS NOT NULL
	DROP TABLE [test].[PIAPS]
GO
CREATE TABLE [test].[PIAPS] (
[objectid] int NOT NULL,
[kode_prov] int NULL,
[shape_leng] float NULL,
[luas_ha] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_PIAPS_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_test_PIAPS_shape] ON [test].[PIAPS](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 10607256.198599385,  ymin = -1211484.214734089,  xmax = 15696048.200928438,  ymax = 598795.1559319316));
GO

IF OBJECT_ID('[test].[dbklhk_pktha_pskl_potensi_konflik_jabalnus]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_jabalnus]
GO
CREATE TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_jabalnus] (
[objectid_12] int NOT NULL,
[objectid] int NULL,
[fid_pl__ko] int NULL,
[objectid_1] int NULL,
[keterangan] varchar(162) NULL,
[fungsi] varchar(18) NULL,
[fungsi_kws] float NULL,
[kd_kws] varchar(5) NULL,
[objectid_2] float NULL,
[wa] varchar(50) NULL,
[shape_leng] float NULL,
[fid_beriji] int NULL,
[layer] varchar(21) NULL,
[ijin] varchar(25) NULL,
[shape_le_1] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pktha_pskl_potensi_konflik_jabalnus_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pktha_pskl_potensi_konflik_jabalnus_shape] ON [test].[dbklhk_pktha_pskl_potensi_konflik_jabalnus](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 105.32549285900001,  ymin = -10.906157226000005,  xmax = 125.12124870800005,  ymax = -5.048463662000017));
GO

IF OBJECT_ID('[test].[dbklhk_pktha_pskl_potensi_konflik_kalimantan]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_kalimantan]
GO
CREATE TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_kalimantan] (
[objectid_12] int NOT NULL,
[objectid] int NULL,
[fid_pl__ko] int NULL,
[objectid_1] int NULL,
[keterangan] varchar(162) NULL,
[fungsi] varchar(18) NULL,
[fungsi_kws] float NULL,
[kd_kws] varchar(5) NULL,
[objectid_2] float NULL,
[wa] varchar(50) NULL,
[shape_leng] float NULL,
[fid_beriji] int NULL,
[layer] varchar(21) NULL,
[ijin] varchar(25) NULL,
[shape_le_1] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pktha_pskl_potensi_konflik_kalimantan_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pktha_pskl_potensi_konflik_kalimantan_shape] ON [test].[dbklhk_pktha_pskl_potensi_konflik_kalimantan](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 108.909263281,  ymin = -4.142441781999992,  xmax = 118.9870224,  ymax = 4.354490688999988));
GO

IF OBJECT_ID('[test].[dbklhk_pktha_pskl_potensi_konflik_maluku_papua]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_maluku_papua]
GO
CREATE TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_maluku_papua] (
[objectid_12] int NOT NULL,
[objectid] int NULL,
[fid_pl__ko] int NULL,
[objectid_1] int NULL,
[keterangan] varchar(162) NULL,
[fungsi] varchar(18) NULL,
[fungsi_kws] float NULL,
[kd_kws] varchar(5) NULL,
[objectid_2] float NULL,
[wa] varchar(50) NULL,
[shape_leng] float NULL,
[fid_beriji] int NULL,
[layer] varchar(21) NULL,
[ijin] varchar(25) NULL,
[shape_le_1] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pktha_pskl_potensi_konflik_maluku_papua_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pktha_pskl_potensi_konflik_maluku_papua_shape] ON [test].[dbklhk_pktha_pskl_potensi_konflik_maluku_papua](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 124.294723514,  ymin = -9.00226402200002,  xmax = 141.00782628699994,  ymax = 2.644016743999998));
GO

IF OBJECT_ID('[test].[dbklhk_pktha_pskl_potensi_konflik_sulawesi]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_sulawesi]
GO
CREATE TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_sulawesi] (
[objectid_12] int NOT NULL,
[objectid] int NULL,
[fid_pl__ko] int NULL,
[objectid_1] int NULL,
[keterangan] varchar(162) NULL,
[fungsi] varchar(18) NULL,
[fungsi_kws] float NULL,
[kd_kws] varchar(5) NULL,
[objectid_2] float NULL,
[wa] varchar(50) NULL,
[shape_leng] float NULL,
[fid_beriji] int NULL,
[layer] varchar(21) NULL,
[ijin] varchar(25) NULL,
[shape_le_1] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pktha_pskl_potensi_konflik_sulawesi_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pktha_pskl_potensi_konflik_sulawesi_shape] ON [test].[dbklhk_pktha_pskl_potensi_konflik_sulawesi](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 118.76217434399996,  ymin = -7.298398067999983,  xmax = 126.88684398600003,  ymax = 4.500359736000007));
GO

IF OBJECT_ID('[test].[dbklhk_pktha_pskl_potensi_konflik_sumatera]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_sumatera]
GO
CREATE TABLE [test].[dbklhk_pktha_pskl_potensi_konflik_sumatera] (
[objectid_12] int NOT NULL,
[objectid] int NULL,
[fid_pl__ko] int NULL,
[objectid_1] int NULL,
[keterangan] varchar(162) NULL,
[fungsi] varchar(18) NULL,
[fungsi_kws] float NULL,
[kd_kws] varchar(5) NULL,
[objectid_2] float NULL,
[wa] varchar(50) NULL,
[shape_leng] float NULL,
[fid_beriji] int NULL,
[layer] varchar(21) NULL,
[ijin] varchar(25) NULL,
[shape_le_1] float NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pktha_pskl_potensi_konflik_sumatera_objectid_12] PRIMARY KEY([objectid_12])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pktha_pskl_potensi_konflik_sumatera_shape] ON [test].[dbklhk_pktha_pskl_potensi_konflik_sumatera](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 95.01329377600001,  ymin = -6.110178451000024,  xmax = 109.15715789799998,  ymax = 5.906965167999999));
GO

IF OBJECT_ID('[test].[SPASIALHPHD]') IS NOT NULL
	DROP TABLE [test].[SPASIALHPHD]
GO
CREATE TABLE [test].[SPASIALHPHD] (
[objectid] int NOT NULL,
[kodprv] int NULL,
[kodkab] int NULL,
[hd_id] int NULL,
[nama_prov] varchar(62) NULL,
[nama_kab] varchar(87) NULL,
[nama_kec] varchar(87) NULL,
[nama_desa] varchar(87) NULL,
[nama_hd] varchar(87) NULL,
[no_sk_hphd] varchar(62) NULL,
[tgl_sk_hphd] bigint NULL, 
[tgl_sk_hphd_Date] AS (dateadd(millisecond, tgl_sk_hphd%(60000), dateadd(minute, tgl_sk_hphd/(60000), '1970-01-01 00:00:00.000'))),
[no_sk_pak_hd] varchar(62) NULL,
[tgl_sk_pak_hd] bigint NULL, 
[tgl_sk_pak_hd_Date] AS (dateadd(millisecond, tgl_sk_pak_hd%(60000), dateadd(minute, tgl_sk_pak_hd/(60000), '1970-01-01 00:00:00.000'))),
[wilayah] varchar(2) NULL,
[luas_hl] float NULL,
[luas_hp] float NULL,
[luas_hpt] float NULL,
[luas_hpk] float NULL,
[luas_hphd] float NULL,
[luas_poli] float NULL,
[nama_lembaga] varchar(62) NULL,
[ketua_lembaga] varchar(62) NULL,
[kontak_lembaga] varchar(62) NULL,
[pendamping] varchar(62) NULL,
[shape_leng] float NULL,
[shape] geometry NULL,
[shape_Length] float NULL,
[shape_Area] float NULL,
CONSTRAINT [pk_test_SPASIALHPHD_objectid] PRIMARY KEY([objectid])
)CREATE INDEX [test_SPASIALHPHD_I5hd_id] ON [test].[SPASIALHPHD](hd_id)
GO

CREATE SPATIAL INDEX [spidx_test_SPASIALHPHD_shape] ON [test].[SPASIALHPHD](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 96.06893093900004,  ymin = -8.452012674999935,  xmax = 140.65752208800006,  ymax = 5.176126444000033));
GO

IF OBJECT_ID('[test].[dbklhk_pdluk_pktl_Batas_Ekologis_2]') IS NOT NULL
	DROP TABLE [test].[dbklhk_pdluk_pktl_Batas_Ekologis_2]
GO
CREATE TABLE [test].[dbklhk_pdluk_pktl_Batas_Ekologis_2] (
[objectid] int NOT NULL,
[nama_pemra] varchar(100) NULL,
[layer] varchar(62) NULL,
[nama_kegia] varchar(100) NULL,
[jenis_doku] varchar(37) NULL,
[tahun] float NULL,
[lokasi] varchar(100) NULL,
[luas] float NULL,
[shape_leng] float NULL,
[skala_data] varchar(37) NULL,
[tipe_gps] varchar(37) NULL,
[shape] geometry NULL,
[st_areashape] float NULL,
[st_lengthshape] float NULL,
CONSTRAINT [pk_test_dbklhk_pdluk_pktl_Batas_Ekologis_2_objectid] PRIMARY KEY([objectid])
)
GO

CREATE SPATIAL INDEX [spidx_test_dbklhk_pdluk_pktl_Batas_Ekologis_2_shape] ON [test].[dbklhk_pdluk_pktl_Batas_Ekologis_2](shape) USING GEOMETRY_AUTO_GRID  WITH (BOUNDING_BOX = (xmin = 111.67373225400002,  ymin = -7.208387937999987,  xmax = 111.72690881599999,  ymax = -7.128952169999991));