# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:31:28 2020

@author: guoyuchen

@e-mail：guoyc1994@163.com

@tel: 15801369263

"""

import numpy as np

def read_Himawari(inputfile):
    resolution=int(inputfile[-12])
    if resolution==1:
        res=12100000
        nlin=1100
        ncol=11000
    elif resolution==2:
        res=3025000
        nlin=550
        ncol=5500
    else:
        res=48400000
        nlin=2200
        ncol=22000
        
    band=int(inputfile[-21:-19])
    if band < 7:
            formation = [('Block number1', 'i1', 1), \
                         ('Block length1', 'i2', 1), \
                         ('Total number of header blocks ', 'i2', 1), \
                         ('Byte order', 'i1', 1), \
                         ('Satellite name', 'S1', 16), \
                         ('Processing center name', 'S1', 16), \
                         ('Observation area', 'S1', 4), \
                         ('Other observation information', 'S1', 2), \
                         ('Observation timeline', 'i2', 1), \
                         ('Observation start time', 'float64', 1), \
                         ('Observation end time', 'float64', 1), \
                         ('File creation time', 'float64', 1), \
                         ('Total header length', 'i4', 1), \
                         ('Total data length', 'i4', 1), \
                         ('Quality flag 1', 'i1', 1), \
                         ('Quality flag 2 ', 'i1', 1), \
                         ('Quality flag 3', 'i1', 1), \
                         ('Quality flag 4', 'i1', 1), \
                         ('File format version', 'S1', 32), \
                         ('File name ', 'S1', 128), \
                         ('Spare1', 'S1', 40), \

                         ('Block number2', 'i1', 1), \
                         ('Block length2', 'i2', 1), \
                         ('Number of bits per pixel', 'i2', 1), \
                         ('Number of columns', 'i2', 1), \
                         ('Number of lines', 'i2', 1), \
                         ('Compression flag for data', 'i1', 1), \
                         ('Spare2', 'S1', 40), \

                         ('Block number3', 'i1', 1), \
                         ('Block length3', 'i2', 1), \
                         ('sub_lon', 'float64', 1), \
                         ('Column scaling factor', 'i4', 1), \
                         ('Line scaling factor', 'i4', 1), \
                         ('Column offset', 'float32', 1), \
                         ('Line offset', 'float32', 1), \
                         ('Distance from Earth’s center to virtual satellite', 'float64', 1), \
                         ('Earth’s equatorial radius', 'float64', 1), \
                         ('Earth’s polar radius', 'float64', 1), \
                         ('var1', 'float64', 1), \
                         ('var2', 'float64', 1), \
                         ('var3', 'float64', 1), \
                         ('Coefficient for sd', 'float64', 1), \
                         ('Resampling types', 'i2', 1), \
                         ('Resampling size', 'i2', 1), \
                         ('Spare3', 'S1', 40), \

                         ('Block number4', 'i1', 1), \
                         ('Block length4', 'i2', 1), \
                         ('Navigation information time', 'float64', 1), \
                         ('SSP longitude', 'float64', 1), \
                         ('SSP latitude', 'float64', 1), \
                         ('Distance from Earth’s center to Satellite', 'float64', 1), \
                         ('Nadir longitude', 'float64', 1), \
                         ('Nadir latitude', 'float64', 1), \
                         ('Sun’s position', 'float64', 3), \
                         ('Moon’s position', 'float64', 3), \
                         ('Spare4', 'S1', 40), \

                         ('Block number5', 'i1', 1), \
                         ('Block length5', 'i2', 1), \
                         ('Band number', 'i2', 1), \
                         ('Central wave length', 'float64', 1), \
                         ('Valid number of bits per pixel', 'i2', 1), \
                         ('Count value of error pixels', 'uint16', 1), \
                         ('Count value of pixels outside scan area', 'uint16', 1), \
                         ('Slope for count-radiance conversion equation ', 'float64', 1), \
                         ('Intercept for count-radiance conversion equation', 'float64', 1), \
                         ('Coefficient for transformation from radiance  to albedo', 'float64', 1), \
                         ('Update time of the values of the following No. 12 and No. 13', 'float64', 1), \
                         ('Calibrated Slope for count-radiance conversion equation_updated value of No. 8 of this block ', 'float64', 1),\
                         ('Calibrated Intercept for count-radiance conversion equation_updated value of No. 9 of this block ', 'float64', 1),\
                         ('Spare5', 'S1', 80), \

                         ('Block number6', 'i1', 1), \
                         ('Block length6', 'i2', 1), \
                         ('GSICS calibration coefficient_Intercept', 'float64', 1), \
                         ('GSICS calibration coefficient_Slope', 'float64', 1), \
                         ('GSICS calibration coefficient_Quadratic term', 'float64', 1), \
                         ('Radiance bias for standard scene', 'float64', 1), \
                         ('Uncertainty of radiance bias for standard scene', 'float64', 1), \
                         ('Radiance for standard scene', 'float64', 1), \
                         ('Start time of GSICS Correction validity period', 'float64', 1), \
                         ('End time of GSICS Correction validity period', 'float64', 1), \
                         ('Radiance validity range of GSICS calibration coefficients_upper limit', 'float32', 1), \
                         ('Radiance validity range of GSICS calibration coefficients_lower limit', 'float32', 1), \
                         ('File name of GSICS Correction', 'S1', 128), \
                         ('Spare6', 'S1', 56), \

                         ('Block number7', 'i1', 1), \
                         ('Block length7', 'i2', 1), \
                         ('Total number of segments', 'i1', 1), \
                         ('Segment sequence number', 'i1', 1), \
                         ('First line number of image segment', 'i2', 1), \
                         ('Spare7', 'S1', 40), \

                         ('Block number8', 'i1', 1), \
                         ('Block length8', 'i2', 1), \
                         ('Center column of rotation', 'float32', 1), \
                         ('Center line of rotation', 'float32', 1), \
                         ('Amount of rotational correction', 'float64', 1), \
                         ('Number of correction information data for column and line direction', 'i2', 1), \
                         ('Line number after rotation', 'i2', 1), \
                         ('Shift amount for column direction', 'float32', 1), \
                         ('Shift amount for line direction8', 'float32', 1), \
                         ('Spare8', 'S1', 50), \

                         ('Block number9', 'i1', 1), \
                         ('Block length9', 'i2', 1), \
                         ('Number of observation times9', 'i2', 1), \
                         ('Line number9', 'i2', 1), \
                         ('Observation time9', 'float64', 1), \
                         ('Spare9', 'S1', 70), \

                         ('Block number10', 'i1', 1), \
                         ('Block length10', 'i4', 1), \
                         ('Number of error information data', 'i2', 1), \
                         ('Line number10', 'i2', 1), \
                         ('Number of error pixels per line10', 'i2', 1), \
                         ('Spare10', 'S1', 36), \

                         ('Block number11', 'i1', 1), \
                         ('Block length11', 'i2', 1), \
                         ('Spare11', 'S1', 256), \

                         ('Count value of each pixel', 'i2', res)]
    else:
        formation=[('Block number1','i1',1),\
                    ('Block length1','i2',1),\
                    ('Total number of header blocks ','i2',1),\
                    ('Byte order','i1',1),\
                    ('Satellite name','S1',16),\
                    ('Processing center name','S1',16),\
                    ('Observation area','S1',4),\
                    ('Other observation information','S1',2),\
                    ('Observation timeline','i2',1),\
                    ('Observation start time','float64',1),\
                    ('Observation end time','float64',1),\
                    ('File creation time','float64',1),\
                    ('Total header length','i4',1),\
                    ('Total data length','i4',1),\
                    ('Quality flag 1','i1',1),\
                    ('Quality flag 2 ','i1',1),\
                    ('Quality flag 3','i1',1),\
                    ('Quality flag 4','i1',1),\
                    ('File format version','S1',32),\
                    ('File name ','S1',128),\
                    ('Spare1','S1',40),\

                    ('Block number2','i1',1),\
                    ('Block length2','i2',1),\
                    ('Number of bits per pixel','i2',1),\
                    ('Number of columns','i2',1),\
                    ('Number of lines','i2',1),\
                    ('Compression flag for data','i1',1),\
                    ('Spare2','S1',40),\

                    ('Block number3','i1',1),\
                    ('Block length3','i2',1),\
                    ('sub_lon','float64',1),\
                    ('Column scaling factor','i4',1),\
                    ('Line scaling factor','i4',1),\
                    ('Column offset','float32',1),\
                    ('Line offset','float32',1),\
                    ('Distance from Earth’s center to virtual satellite','float64',1),\
                    ('Earth’s equatorial radius','float64',1),\
                    ('Earth’s polar radius','float64',1),\
                    ('var1','float64',1),\
                    ('var2','float64',1),\
                    ('var3','float64',1),\
                    ('Coefficient for sd','float64',1),\
                    ('Resampling types','i2',1),\
                    ('Resampling size','i2',1),\
                    ('Spare3','S1',40),\

                    ('Block number4','i1',1),\
                    ('Block length4','i2',1),\
                    ('Navigation information time','float64',1),\
                    ('SSP longitude','float64',1),\
                    ('SSP latitude','float64',1),\
                    ('Distance from Earth’s center to Satellite','float64',1),\
                    ('Nadir longitude','float64',1),\
                    ('Nadir latitude','float64',1),\
                    ('Sun’s position','float64',3),\
                    ('Moon’s position','float64',3),\
                    ('Spare4','S1',40),\

                    ('Block number5','i1',1),\
                    ('Block length5','i2',1),\
                    ('Band number','i2',1),\
                    ('Central wave length','float64',1),\
                    ('Valid number of bits per pixel','i2',1),\
                    ('Count value of error pixels','i2',1),\
                    ('Count value of pixels outside scan area','i2',1),\
                    ('Slope for count-radiance conversion equation ','float64',1),\
                    ('Intercept for count-radiance conversion equation','float64',1),\
                    ('radiance to brightness temperature_c0','float64',1),\
                    ('radiance to brightness temperature_c1','float64',1),\
                    ('radiance to brightness temperature_c2','float64',1),\
                    ('brightness temperature to radiance_C0','float64',1),\
                    ('brightness temperature to radianceC1','float64',1),\
                    ('brightness temperature to radianceC2','float64',1),\
                    ('Speed of light','float64',1),\
                    ('Planck constant','float64',1),\
                    ('Boltzmann constant','float64',1),\
                    ('Spare5','S1',40), \

                   ('Block number6', 'i1', 1), \
                   ('Block length6', 'i2', 1), \
                   ('GSICS calibration coefficient_Intercept', 'float64', 1), \
                   ('GSICS calibration coefficient_Slope', 'float64', 1), \
                   ('GSICS calibration coefficient_Quadratic term', 'float64', 1), \
                   ('Radiance bias for standard scene', 'float64', 1), \
                   ('Uncertainty of radiance bias for standard scene', 'float64', 1), \
                   ('Radiance for standard scene', 'float64', 1), \
                   ('Start time of GSICS Correction validity period', 'float64', 1), \
                   ('End time of GSICS Correction validity period', 'float64', 1), \
                   ('Radiance validity range of GSICS calibration coefficients_upper limit', 'float32', 1), \
                   ('Radiance validity range of GSICS calibration coefficients_lower limit', 'float32', 1), \
                   ('File name of GSICS Correction', 'S1', 128), \
                   ('Spare6', 'S1', 56), \

                   ('Block number7', 'i1', 1), \
                   ('Block length7', 'i2', 1), \
                   ('Total number of segments', 'i1', 1), \
                   ('Segment sequence number', 'i1', 1), \
                   ('First line number of image segment', 'i2', 1), \
                   ('Spare7', 'S1', 40), \

                   ('Block number8', 'i1', 1), \
                   ('Block length8', 'i2', 1), \
                   ('Center column of rotation', 'float32', 1), \
                   ('Center line of rotation', 'float32', 1), \
                   ('Amount of rotational correction', 'float64', 1), \
                   ('Number of correction information data for column and line direction', 'i2', 1), \
                   ('Line number after rotation', 'i2', 1), \
                   ('Shift amount for column direction', 'float32', 1), \
                   ('Shift amount for line direction8', 'float32', 1), \
                   ('Spare8', 'S1', 50), \

                   ('Block number9', 'i1', 1), \
                   ('Block length9', 'i2', 1), \
                   ('Number of observation times9', 'i2', 1), \
                   ('Line number9', 'i2', 1), \
                   ('Observation time9', 'float64', 1), \
                   ('Spare9', 'S1', 70), \

                   ('Block number10', 'i1', 1), \
                   ('Block length10', 'i4', 1), \
                   ('Number of error information data', 'i2', 1), \
                   ('Line number10', 'i2', 1), \
                   ('Number of error pixels per line10', 'i2', 1), \
                   ('Spare10', 'S1', 36), \

                   ('Block number11', 'i1', 1), \
                   ('Block length11', 'i2', 1), \
                   ('Spare11', 'S1', 256), \


                   ('Count value of each pixel', 'i2', res)]
    data=np.fromfile(inputfile,dtype=formation)

    band=data['Count value of each pixel'].reshape(nlin,ncol)
    return band


def read_Himawari_info(inputfile):
    resolution=int(inputfile[-12])
    if resolution==1:
        res=12100000
    elif resolution==2:
        res=3025000
    else:
        res=48400000
    band=int(inputfile[-21:-19])
    if band < 7:
            formation = [('Block number1', 'i1', 1), \
                         ('Block length1', 'i2', 1), \
                         ('Total number of header blocks ', 'i2', 1), \
                         ('Byte order', 'i1', 1), \
                         ('Satellite name', 'S1', 16), \
                         ('Processing center name', 'S1', 16), \
                         ('Observation area', 'S1', 4), \
                         ('Other observation information', 'S1', 2), \
                         ('Observation timeline', 'i2', 1), \
                         ('Observation start time', 'float64', 1), \
                         ('Observation end time', 'float64', 1), \
                         ('File creation time', 'float64', 1), \
                         ('Total header length', 'i4', 1), \
                         ('Total data length', 'i4', 1), \
                         ('Quality flag 1', 'i1', 1), \
                         ('Quality flag 2 ', 'i1', 1), \
                         ('Quality flag 3', 'i1', 1), \
                         ('Quality flag 4', 'i1', 1), \
                         ('File format version', 'S1', 32), \
                         ('File name ', 'S1', 128), \
                         ('Spare1', 'S1', 40), \

                         ('Block number2', 'i1', 1), \
                         ('Block length2', 'i2', 1), \
                         ('Number of bits per pixel', 'i2', 1), \
                         ('Number of columns', 'i2', 1), \
                         ('Number of lines', 'i2', 1), \
                         ('Compression flag for data', 'i1', 1), \
                         ('Spare2', 'S1', 40), \

                         ('Block number3', 'i1', 1), \
                         ('Block length3', 'i2', 1), \
                         ('sub_lon', 'float64', 1), \
                         ('Column scaling factor', 'i4', 1), \
                         ('Line scaling factor', 'i4', 1), \
                         ('Column offset', 'float32', 1), \
                         ('Line offset', 'float32', 1), \
                         ('Distance from Earth’s center to virtual satellite', 'float64', 1), \
                         ('Earth’s equatorial radius', 'float64', 1), \
                         ('Earth’s polar radius', 'float64', 1), \
                         ('var1', 'float64', 1), \
                         ('var2', 'float64', 1), \
                         ('var3', 'float64', 1), \
                         ('Coefficient for sd', 'float64', 1), \
                         ('Resampling types', 'i2', 1), \
                         ('Resampling size', 'i2', 1), \
                         ('Spare3', 'S1', 40), \

                         ('Block number4', 'i1', 1), \
                         ('Block length4', 'i2', 1), \
                         ('Navigation information time', 'float64', 1), \
                         ('SSP longitude', 'float64', 1), \
                         ('SSP latitude', 'float64', 1), \
                         ('Distance from Earth’s center to Satellite', 'float64', 1), \
                         ('Nadir longitude', 'float64', 1), \
                         ('Nadir latitude', 'float64', 1), \
                         ('Sun’s position', 'float64', 3), \
                         ('Moon’s position', 'float64', 3), \
                         ('Spare4', 'S1', 40), \

                         ('Block number5', 'i1', 1), \
                         ('Block length5', 'i2', 1), \
                         ('Band number', 'i2', 1), \
                         ('Central wave length', 'float64', 1), \
                         ('Valid number of bits per pixel', 'i2', 1), \
                         ('Count value of error pixels', 'uint16', 1), \
                         ('Count value of pixels outside scan area', 'uint16', 1), \
                         ('Slope for count-radiance conversion equation ', 'float64', 1), \
                         ('Intercept for count-radiance conversion equation', 'float64', 1), \
                         ('Coefficient for transformation from radiance  to albedo', 'float64', 1), \
                         ('Update time of the values of the following No. 12 and No. 13', 'float64', 1), \
                         ('Calibrated Slope for count-radiance conversion equation_updated value of No. 8 of this block ', 'float64', 1),\
                         ('Calibrated Intercept for count-radiance conversion equation_updated value of No. 9 of this block ', 'float64', 1),\
                         ('Spare5', 'S1', 80), \

                         ('Block number6', 'i1', 1), \
                         ('Block length6', 'i2', 1), \
                         ('GSICS calibration coefficient_Intercept', 'float64', 1), \
                         ('GSICS calibration coefficient_Slope', 'float64', 1), \
                         ('GSICS calibration coefficient_Quadratic term', 'float64', 1), \
                         ('Radiance bias for standard scene', 'float64', 1), \
                         ('Uncertainty of radiance bias for standard scene', 'float64', 1), \
                         ('Radiance for standard scene', 'float64', 1), \
                         ('Start time of GSICS Correction validity period', 'float64', 1), \
                         ('End time of GSICS Correction validity period', 'float64', 1), \
                         ('Radiance validity range of GSICS calibration coefficients_upper limit', 'float32', 1), \
                         ('Radiance validity range of GSICS calibration coefficients_lower limit', 'float32', 1), \
                         ('File name of GSICS Correction', 'S1', 128), \
                         ('Spare6', 'S1', 56), \

                         ('Block number7', 'i1', 1), \
                         ('Block length7', 'i2', 1), \
                         ('Total number of segments', 'i1', 1), \
                         ('Segment sequence number', 'i1', 1), \
                         ('First line number of image segment', 'i2', 1), \
                         ('Spare7', 'S1', 40), \

                         ('Block number8', 'i1', 1), \
                         ('Block length8', 'i2', 1), \
                         ('Center column of rotation', 'float32', 1), \
                         ('Center line of rotation', 'float32', 1), \
                         ('Amount of rotational correction', 'float64', 1), \
                         ('Number of correction information data for column and line direction', 'i2', 1), \
                         ('Line number after rotation', 'i2', 1), \
                         ('Shift amount for column direction', 'float32', 1), \
                         ('Shift amount for line direction8', 'float32', 1), \
                         ('Spare8', 'S1', 50), \

                         ('Block number9', 'i1', 1), \
                         ('Block length9', 'i2', 1), \
                         ('Number of observation times9', 'i2', 1), \
                         ('Line number9', 'i2', 1), \
                         ('Observation time9', 'float64', 1), \
                         ('Spare9', 'S1', 70), \

                         ('Block number10', 'i1', 1), \
                         ('Block length10', 'i4', 1), \
                         ('Number of error information data', 'i2', 1), \
                         ('Line number10', 'i2', 1), \
                         ('Number of error pixels per line10', 'i2', 1), \
                         ('Spare10', 'S1', 36), \

                         ('Block number11', 'i1', 1), \
                         ('Block length11', 'i2', 1), \
                         ('Spare11', 'S1', 256), \

                         ('Count value of each pixel', 'i2', res)]
    else:
        formation=[('Block number1','i1',1),\
                    ('Block length1','i2',1),\
                    ('Total number of header blocks ','i2',1),\
                    ('Byte order','i1',1),\
                    ('Satellite name','S1',16),\
                    ('Processing center name','S1',16),\
                    ('Observation area','S1',4),\
                    ('Other observation information','S1',2),\
                    ('Observation timeline','i2',1),\
                    ('Observation start time','float64',1),\
                    ('Observation end time','float64',1),\
                    ('File creation time','float64',1),\
                    ('Total header length','i4',1),\
                    ('Total data length','i4',1),\
                    ('Quality flag 1','i1',1),\
                    ('Quality flag 2 ','i1',1),\
                    ('Quality flag 3','i1',1),\
                    ('Quality flag 4','i1',1),\
                    ('File format version','S1',32),\
                    ('File name ','S1',128),\
                    ('Spare1','S1',40),\

                    ('Block number2','i1',1),\
                    ('Block length2','i2',1),\
                    ('Number of bits per pixel','i2',1),\
                    ('Number of columns','i2',1),\
                    ('Number of lines','i2',1),\
                    ('Compression flag for data','i1',1),\
                    ('Spare2','S1',40),\

                    ('Block number3','i1',1),\
                    ('Block length3','i2',1),\
                    ('sub_lon','float64',1),\
                    ('Column scaling factor','i4',1),\
                    ('Line scaling factor','i4',1),\
                    ('Column offset','float32',1),\
                    ('Line offset','float32',1),\
                    ('Distance from Earth’s center to virtual satellite','float64',1),\
                    ('Earth’s equatorial radius','float64',1),\
                    ('Earth’s polar radius','float64',1),\
                    ('var1','float64',1),\
                    ('var2','float64',1),\
                    ('var3','float64',1),\
                    ('Coefficient for sd','float64',1),\
                    ('Resampling types','i2',1),\
                    ('Resampling size','i2',1),\
                    ('Spare3','S1',40),\

                    ('Block number4','i1',1),\
                    ('Block length4','i2',1),\
                    ('Navigation information time','float64',1),\
                    ('SSP longitude','float64',1),\
                    ('SSP latitude','float64',1),\
                    ('Distance from Earth’s center to Satellite','float64',1),\
                    ('Nadir longitude','float64',1),\
                    ('Nadir latitude','float64',1),\
                    ('Sun’s position','float64',3),\
                    ('Moon’s position','float64',3),\
                    ('Spare4','S1',40),\

                    ('Block number5','i1',1),\
                    ('Block length5','i2',1),\
                    ('Band number','i2',1),\
                    ('Central wave length','float64',1),\
                    ('Valid number of bits per pixel','i2',1),\
                    ('Count value of error pixels','i2',1),\
                    ('Count value of pixels outside scan area','i2',1),\
                    ('Slope for count-radiance conversion equation ','float64',1),\
                    ('Intercept for count-radiance conversion equation','float64',1),\
                    ('radiance to brightness temperature_c0','float64',1),\
                    ('radiance to brightness temperature_c1','float64',1),\
                    ('radiance to brightness temperature_c2','float64',1),\
                    ('brightness temperature to radiance_C0','float64',1),\
                    ('brightness temperature to radianceC1','float64',1),\
                    ('brightness temperature to radianceC2','float64',1),\
                    ('Speed of light','float64',1),\
                    ('Planck constant','float64',1),\
                    ('Boltzmann constant','float64',1),\
                    ('Spare5','S1',40), \

                   ('Block number6', 'i1', 1), \
                   ('Block length6', 'i2', 1), \
                   ('GSICS calibration coefficient_Intercept', 'float64', 1), \
                   ('GSICS calibration coefficient_Slope', 'float64', 1), \
                   ('GSICS calibration coefficient_Quadratic term', 'float64', 1), \
                   ('Radiance bias for standard scene', 'float64', 1), \
                   ('Uncertainty of radiance bias for standard scene', 'float64', 1), \
                   ('Radiance for standard scene', 'float64', 1), \
                   ('Start time of GSICS Correction validity period', 'float64', 1), \
                   ('End time of GSICS Correction validity period', 'float64', 1), \
                   ('Radiance validity range of GSICS calibration coefficients_upper limit', 'float32', 1), \
                   ('Radiance validity range of GSICS calibration coefficients_lower limit', 'float32', 1), \
                   ('File name of GSICS Correction', 'S1', 128), \
                   ('Spare6', 'S1', 56), \

                   ('Block number7', 'i1', 1), \
                   ('Block length7', 'i2', 1), \
                   ('Total number of segments', 'i1', 1), \
                   ('Segment sequence number', 'i1', 1), \
                   ('First line number of image segment', 'i2', 1), \
                   ('Spare7', 'S1', 40), \

                   ('Block number8', 'i1', 1), \
                   ('Block length8', 'i2', 1), \
                   ('Center column of rotation', 'float32', 1), \
                   ('Center line of rotation', 'float32', 1), \
                   ('Amount of rotational correction', 'float64', 1), \
                   ('Number of correction information data for column and line direction', 'i2', 1), \
                   ('Line number after rotation', 'i2', 1), \
                   ('Shift amount for column direction', 'float32', 1), \
                   ('Shift amount for line direction8', 'float32', 1), \
                   ('Spare8', 'S1', 50), \

                   ('Block number9', 'i1', 1), \
                   ('Block length9', 'i2', 1), \
                   ('Number of observation times9', 'i2', 1), \
                   ('Line number9', 'i2', 1), \
                   ('Observation time9', 'float64', 1), \
                   ('Spare9', 'S1', 70), \

                   ('Block number10', 'i1', 1), \
                   ('Block length10', 'i4', 1), \
                   ('Number of error information data', 'i2', 1), \
                   ('Line number10', 'i2', 1), \
                   ('Number of error pixels per line10', 'i2', 1), \
                   ('Spare10', 'S1', 36), \

                   ('Block number11', 'i1', 1), \
                   ('Block length11', 'i2', 1), \
                   ('Spare11', 'S1', 256), \


                   ('Count value of each pixel', 'i2', res)]
    data=np.fromfile(inputfile,dtype=formation)

    return data


def latlon2idx(lon,lat,B,A,H,pi,STAR_POINT_LON,COFF,CFAC):

    ANG = np.pi / 180

    lon = np.array(lon)
    lat = np.array(lat)
    lon = lon * ANG
    lat = lat * ANG
    f = np.arctan(np.tan(lat) * (A * A) / (B * B))
    re = B / (np.sqrt(1 - (np.cos(f) * np.cos(f)) * (A * A - B * B) / (A * A)))

    r1 = H - re * np.cos(f) * np.cos(lon - (STAR_POINT_LON * ANG))
    r2 = 0 - re * np.cos(f) * np.sin(lon - (STAR_POINT_LON * ANG))

    r3 = re * np.sin(f)
    rn = np.sqrt(r1 * r1 + r2 * r2 + r3 * r3)
    x = np.arctan(0 - r2 / r1) * 180 / np.pi
    y = np.arcsin(0 - r3 / rn) * 180 / np.pi
    col = (COFF + x * CFAC / 2**16).astype(int)
    row = (COFF + y * CFAC / 2**16).astype(int)

    return col, row


def mergeAHI8(un_path,time,bd,res):

    DATA = {}
    for i in np.arange(1,11,1):
        
        inputfile = un_path+'/HS_H08_'+time+'_'+bd+'_FLDK_'+res+'_S{:02d}10.DAT'.format(i)
        
        data = read_Himawari(inputfile)
        
        DATA[i] = data
    BAND = np.vstack((DATA[1],DATA[2],DATA[3],DATA[4],DATA[5],DATA[6],DATA[7],DATA[8],DATA[9],DATA[10])).astype(int)

    return BAND,inputfile


def bandextraction(un_path,time,bd,res):
    band,inputfile = mergeAHI8(un_path,time,bd,res)

    info = read_Himawari_info(inputfile)

    BAND = ToALBEDOorBT(band,info)

    band_ccl,longitude,latitude = fulldisktoCCL(BAND,info)
    return band_ccl,longitude,latitude

def ToALBEDOorBT(BAND,info):

    index = np.where(BAND>0)
    indexunvalid = np.where(BAND<=0)
    rad = BAND
                
    Slop = float(info['Slope for count-radiance conversion equation '][0])
    Int = float(info['Intercept for count-radiance conversion equation'][0])

    if int(bd[1:])<7:
        c = float(info['Coefficient for transformation from radiance  to albedo'])
        BAND = (BAND*Slop+Int)*c
        BAND[indexunvalid] = -2 
    else:   
        h = float(info['Planck constant'][0])
        c = float(info['Speed of light'][0])
        k = float(info['Boltzmann constant'][0])
        wv = float(info['Central wave length'][0])* 1e-6
        c0 = float(info['radiance to brightness temperature_c0'][0])
        c1 = float(info['radiance to brightness temperature_c1'][0])
        c2 = float(info['radiance to brightness temperature_c2'][0])
        rad = (rad*Slop+Int)*1e6
        Te = h*c/((k*wv)*(np.log(2*h*c*c/((wv**5)*rad)+1)))
        BT = c0 + c1 * Te + c2 * Te * Te
        BAND[index] = BT
    return BAND

def fulldisktoCCL(BAND,info):   
    B = float(info['Earth’s equatorial radius'][0])
    #地球短半轴KM
    A = float(info['Earth’s polar radius'][0])
    #卫星到质心的距离KM
    H = float(info['Distance from Earth’s center to virtual satellite'][0])
    #pi
    pi = np.pi
    #星下点所在经度
    STAR_POINT_LON = 140.7
    #2KM偏移量
    COFF = float(info['Column offset'][0])
    #2KM偏移因子
    CFAC = float(info['Column scaling factor'][0])
    
    longitude = np.arange(73-1,135+70-22-1,0.02)

    latitude = np.arange(55,-55,-0.02)

    lon,lat = np.meshgrid(longitude,latitude)

    col,row = latlon2idx(lon,lat,B,A,H,pi,STAR_POINT_LON,COFF,CFAC)

    #####

    band_ccl = np.zeros(lon.shape)

    band_ccl = BAND[row,col]

    return band_ccl,longitude,latitude






time = '20200701_0800'

un_path="C://Users/guoyuchen/Desktop/fulldisk/output/"

bandlist = ['B03']#,'B02']#['B03','B04','B05','B06','B07','B08','B09','B10','B11','B12','B13','B14','B15','B16']
reslist = ['R10']#,'R20','R05']


bd = 'B01'

#ALLBAND = {}

#for bd in bandlist:
#    band_ccl,longitude,latitude = bandextraction(un_path,time,bd,'R05')
#    ALLBAND[bd] = band_ccl



res = reslist[0]

DATA = {}
for i in np.arange(1,11,1):
    
    inputfile = un_path+'/HS_H08_'+time+'_'+bd+'_FLDK_'+res+'_S{:02d}10.DAT'.format(i)
    
    data = read_Himawari(inputfile)
    
    DATA[i] = data
    
BAND = np.vstack((DATA[1],DATA[2],DATA[3],DATA[4],DATA[5],DATA[6],DATA[7],DATA[8],DATA[9],DATA[10])).astype(int)


info = read_Himawari_info(inputfile)

BAND = ToALBEDOorBT(BAND,info)

band_ccl,longitude,latitude = fulldisktoCCL(BAND,info)

'''
img = np.zeros((5500,5500,3))

img[:,:,0] = np.clip(ALLBAND['B01'],0,1)
img[:,:,1] = np.clip(ALLBAND['B02'],0,1)
img[:,:,2] = np.clip(ALLBAND['B01'],0,1)
'''













