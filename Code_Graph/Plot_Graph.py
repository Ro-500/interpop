import pandas as pd
import numpy as np
import pygal as pg
line_chart = pg.Bar()

def main(phone='all', age='all'):
    if phone == 'all':
        if age == 'all':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone ทั้งหมด(%)'
            all_all()
        elif age == '6-10':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 6-10 ปี(%)'
            all_age(0)
        elif age == '10-14':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 10-14 ปี(%)'
            all_age(1)
        elif age == '15-19':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 15-19 ปี(%)'
            all_age(2)
        elif age == '20-24':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 20-24 ปี(%)'
            all_age(3)
        elif age == '25-29':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 25-29 ปี(%)'
            all_age(4)
        elif age == '30-34':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 30-34 ปี(%)'
            all_age(5)
        elif age == '35-39':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 35-39 ปี(%)'
            all_age(6)
        elif age == '40-49':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 40-49 ปี(%)'
            all_age(7)
        elif age == '50-59':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 40-49 ปี(%)'
            all_age(8)
        elif age == '60 and over':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone และ Smart Phone อายุ 60 ปีหรือมากกว่า(%)'
            all_age(9)
    elif phone == 'feature phone':
        if age == 'all':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone ทั้งหมด(%)'
            fp_all()
        elif age == '6-10':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 6-10 ปี(%)'
            fp_age(0)
        elif age == '10-14':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 10-14 ปี(%)'
            fp_age(1)
        elif age == '15-19':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 15-19 ปี(%)'
            fp_age(2)
        elif age == '20-24':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 20-24 ปี(%)'
            fp_age(3)
        elif age == '25-29':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 25-29 ปี(%)'
            fp_age(4)
        elif age == '30-34':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 30-34 ปี(%)'
            fp_age(5)
        elif age == '35-39':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 35-39 ปี(%)'
            fp_age(6)
        elif age == '40-49':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 40-49 ปี(%)'
            fp_age(7)
        elif age == '50-59':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 50-59 ปี(%)'
            fp_age(8)
        elif age == '60 and over':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Feature Phone อายุ 60 ปีหรือมากกว่า(%)'
            fp_age(9)
    elif phone == 'smart phone':
        if age == 'all':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone ทั้งหมด(%)'
            sp_all()
        elif age == '6-10':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 6-10 ปี(%)'
            sp_age(0)
        elif age == '10-14':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 10-14 ปี(%)'
            sp_age(1)
        elif age == '15-19':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 15-19 ปี(%)'
            sp_age(2)
        elif age == '20-24':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 20-24 ปี(%)'
            sp_age(3)
        elif age == '25-29':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 25-29 ปี(%)'
            sp_age(4)
        elif age == '30-34':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 30-34 ปี(%)'
            sp_age(5)
        elif age == '35-39':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 35-39 ปี(%)'
            sp_age(6)
        elif age == '40-49':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 40-49 ปี(%)'
            sp_age(7)
        elif age == '50-59':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 50-59 ปี(%)'
            sp_age(8)
        elif age == '60 and over':
            line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone อายุ 60 ปีหรือมากกว่า(%)'
            sp_age(9)

def all_all():
    tab32 = pd.read_csv('DATA/ALL_ALL.csv').to_dict()
    line_chart.x_labels = ('6 -> 10', '10 -> 14', '15 -> 19', '20 -> 24', '25 -> 29', '30 -> 34', '35 -> 39', '40 -> 49', '50 -> 59', '60 and over')
    line_chart.add('No feature phone', [(((tab32['FP no mobile'])[0])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP no mobile'])[1])*100)/((tab32['FP no mobile'])[10]), \
                                             (((tab32['FP no mobile'])[2])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP no mobile'])[3])*100)/((tab32['FP no mobile'])[10]), \
                                             (((tab32['FP no mobile'])[4])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP no mobile'])[5])*100)/((tab32['FP no mobile'])[10]), \
                                             (((tab32['FP no mobile'])[6])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP no mobile'])[7])*100)/((tab32['FP no mobile'])[10]), \
                                             (((tab32['FP no mobile'])[8])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP no mobile'])[9])*100)/((tab32['FP no mobile'])[10])])
    line_chart.add('1 Feature phone', [(((tab32['FP 1 mobile'])[0])*100)/((tab32['FP 1 mobile'])[10]), (((tab32['FP 1 mobile'])[1])*100)/((tab32['FP 1 mobile'])[10]), \
                                             (((tab32['FP 1 mobile'])[2])*100)/((tab32['FP 1 mobile'])[10]), (((tab32['FP 1 mobile'])[3])*100)/((tab32['FP 1 mobile'])[10]), \
                                             (((tab32['FP 1 mobile'])[4])*100)/((tab32['FP 1 mobile'])[10]), (((tab32['FP 1 mobile'])[5])*100)/((tab32['FP 1 mobile'])[10]), \
                                             (((tab32['FP 1 mobile'])[6])*100)/((tab32['FP 1 mobile'])[10]), (((tab32['FP 1 mobile'])[7])*100)/((tab32['FP 1 mobile'])[10]), \
                                             (((tab32['FP 1 mobile'])[8])*100)/((tab32['FP 1 mobile'])[10]), (((tab32['FP 1 mobile'])[9])*100)/((tab32['FP 1 mobile'])[10])])
    line_chart.add('2 Feature phone', [(((tab32['FP 2 mobile'])[0])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 2 mobile'])[1])*100)/((tab32['FP 2 mobile'])[10]), \
                                             (((tab32['FP 2 mobile'])[2])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 2 mobile'])[3])*100)/((tab32['FP 2 mobile'])[10]), \
                                             (((tab32['FP 2 mobile'])[4])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 2 mobile'])[5])*100)/((tab32['FP 2 mobile'])[10]), \
                                             (((tab32['FP 2 mobile'])[6])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 2 mobile'])[7])*100)/((tab32['FP 2 mobile'])[10]), \
                                             (((tab32['FP 2 mobile'])[8])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 2 mobile'])[9])*100)/((tab32['FP 2 mobile'])[10])])
    line_chart.add('3 Feature phone', [(((tab32['FP 3 mobile'])[0])*100)/((tab32['FP 3 mobile'])[10]), (((tab32['FP 3 mobile'])[1])*100)/((tab32['FP 3 mobile'])[10]), \
                                             (((tab32['FP 3 mobile'])[2])*100)/((tab32['FP 3 mobile'])[10]), (((tab32['FP 3 mobile'])[3])*100)/((tab32['FP 3 mobile'])[10]), \
                                             (((tab32['FP 3 mobile'])[4])*100)/((tab32['FP 3 mobile'])[10]), (((tab32['FP 3 mobile'])[5])*100)/((tab32['FP 3 mobile'])[10]), \
                                             (((tab32['FP 3 mobile'])[6])*100)/((tab32['FP 3 mobile'])[10]), (((tab32['FP 3 mobile'])[7])*100)/((tab32['FP 3 mobile'])[10]), \
                                             (((tab32['FP 3 mobile'])[8])*100)/((tab32['FP 3 mobile'])[10]), (((tab32['FP 3 mobile'])[9])*100)/((tab32['FP 3 mobile'])[10])])
    line_chart.add('No smart phone', [(((tab32['SP no mobile'])[0])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP no mobile'])[1])*100)/((tab32['SP no mobile'])[10]), \
                                             (((tab32['SP no mobile'])[2])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP no mobile'])[3])*100)/((tab32['SP no mobile'])[10]), \
                                             (((tab32['SP no mobile'])[4])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP no mobile'])[5])*100)/((tab32['SP no mobile'])[10]), \
                                             (((tab32['SP no mobile'])[6])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP no mobile'])[7])*100)/((tab32['SP no mobile'])[10]), \
                                             (((tab32['SP no mobile'])[8])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP no mobile'])[9])*100)/((tab32['SP no mobile'])[10])])
    line_chart.add('1 Smart phone', [(((tab32['SP 1 mobile'])[0])*100)/((tab32['SP 1 mobile'])[10]), (((tab32['SP 1 mobile'])[1])*100)/((tab32['SP 1 mobile'])[10]), \
                                             (((tab32['SP 1 mobile'])[2])*100)/((tab32['SP 1 mobile'])[10]), (((tab32['SP 1 mobile'])[3])*100)/((tab32['SP 1 mobile'])[10]), \
                                             (((tab32['SP 1 mobile'])[4])*100)/((tab32['SP 1 mobile'])[10]), (((tab32['SP 1 mobile'])[5])*100)/((tab32['SP 1 mobile'])[10]), \
                                             (((tab32['SP 1 mobile'])[6])*100)/((tab32['SP 1 mobile'])[10]), (((tab32['SP 1 mobile'])[7])*100)/((tab32['SP 1 mobile'])[10]), \
                                             (((tab32['SP 1 mobile'])[8])*100)/((tab32['SP 1 mobile'])[10]), (((tab32['SP 1 mobile'])[9])*100)/((tab32['SP 1 mobile'])[10])])
    line_chart.add('2 Smart phone', [(((tab32['SP 2 mobile'])[0])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 2 mobile'])[1])*100)/((tab32['SP 2 mobile'])[10]), \
                                             (((tab32['SP 2 mobile'])[2])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 2 mobile'])[3])*100)/((tab32['SP 2 mobile'])[10]), \
                                             (((tab32['SP 2 mobile'])[4])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 2 mobile'])[5])*100)/((tab32['SP 2 mobile'])[10]), \
                                             (((tab32['SP 2 mobile'])[6])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 2 mobile'])[7])*100)/((tab32['SP 2 mobile'])[10]), \
                                             (((tab32['SP 2 mobile'])[8])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 2 mobile'])[9])*100)/((tab32['SP 2 mobile'])[10])])
    line_chart.add('3 Smart phone', [(((tab32['SP 3 mobile'])[0])*100)/((tab32['SP 3 mobile'])[10]), (((tab32['SP 3 mobile'])[1])*100)/((tab32['SP 3 mobile'])[10]), \
                                             (((tab32['SP 3 mobile'])[2])*100)/((tab32['SP 3 mobile'])[10]), (((tab32['SP 3 mobile'])[3])*100)/((tab32['SP 3 mobile'])[10]), \
                                             (((tab32['SP 3 mobile'])[4])*100)/((tab32['SP 3 mobile'])[10]), (((tab32['SP 3 mobile'])[5])*100)/((tab32['SP 3 mobile'])[10]), \
                                             (((tab32['SP 3 mobile'])[6])*100)/((tab32['SP 3 mobile'])[10]), (((tab32['SP 3 mobile'])[7])*100)/((tab32['SP 3 mobile'])[10]), \
                                             (((tab32['SP 3 mobile'])[8])*100)/((tab32['SP 3 mobile'])[10]), (((tab32['SP 3 mobile'])[9])*100)/((tab32['SP 3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')

def all_age(number):
    tab32 = pd.read_csv('DATA/ALL_ALL.csv').to_dict()
    line_chart.x_labels = ('No feature phone', '1 Feature phone', '2 Feature phone', '3 Feature phone', 'No smart phone', '1 Smart phone', '2 Smart phone', '3 Smart phone')
    line_chart.add('Amount', [(((tab32['FP no mobile'])[number])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP 1 mobile'])[number])*100)/((tab32['FP 1 mobile'])[10]), \
                              (((tab32['FP 2 mobile'])[number])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 3 mobile'])[number])*100)/((tab32['FP 3 mobile'])[10]), \
                              (((tab32['SP no mobile'])[number])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP 1 mobile'])[number])*100)/((tab32['FP 1 mobile'])[10]), \
                              (((tab32['SP 2 mobile'])[number])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 3 mobile'])[number])*100)/((tab32['SP 3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')


def fp_all():
    tab32 = pd.read_csv('DATA/FP_ALL.csv').to_dict()
    line_chart.x_labels = ('6 -> 10', '10 -> 14', '15 -> 19', '20 -> 24', '25 -> 29', '30 -> 34', '35 -> 39', '40 -> 49', '50 -> 59', '60 and over')
    line_chart.add('no mobile', [(((tab32['no mobile'])[0])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[1])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[2])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[3])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[4])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[5])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[6])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[7])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[8])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[9])*100)/((tab32['no mobile'])[10])])
    line_chart.add('1 mobile', [(((tab32['1 mobile'])[0])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[1])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[2])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[3])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[4])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[5])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[6])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[7])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[8])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[9])*100)/((tab32['1 mobile'])[10])])
    line_chart.add('2 mobile', [(((tab32['2 mobile'])[0])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[1])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[2])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[3])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[4])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[5])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[6])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[7])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[8])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[9])*100)/((tab32['2 mobile'])[10])])
    line_chart.add('3 mobile', [(((tab32['3 mobile'])[0])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[1])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[2])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[3])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[4])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[5])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[6])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[7])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[8])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[9])*100)/((tab32['3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')

def fp_age(number):
    tab32 = pd.read_csv('DATA/ALL_ALL.csv').to_dict()
    line_chart.x_labels = ('No feature phone', '1 Feature phone', '2 Feature phone', '3 Feature phone', 'No smart phone', '1 Smart phone', '2 Smart phone', '3 Smart phone')
    line_chart.add('Amount', [(((tab32['FP no mobile'])[number])*100)/((tab32['FP no mobile'])[10]), (((tab32['FP 1 mobile'])[number])*100)/((tab32['FP 1 mobile'])[10]), \
                              (((tab32['FP 2 mobile'])[number])*100)/((tab32['FP 2 mobile'])[10]), (((tab32['FP 3 mobile'])[number])*100)/((tab32['FP 3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')
    
def sp_all():
    tab32 = pd.read_csv('DATA/SP_ALL.csv').to_dict()
    line_chart = pg.Bar()
    line_chart.title = 'ผู้ใช้โทรศัพท์มือถือแบบ Smart Phone ทั้งหมด(%)'
    line_chart.x_labels = ('6 -> 10', '10 -> 14', '15 -> 19', '20 -> 24', '25 -> 29', '30 -> 34', '35 -> 39', '40 -> 49', '50 -> 59', '60 and over')
    line_chart.add('no mobile', [(((tab32['no mobile'])[0])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[1])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[2])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[3])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[4])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[5])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[6])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[7])*100)/((tab32['no mobile'])[10]), \
                                             (((tab32['no mobile'])[8])*100)/((tab32['no mobile'])[10]), (((tab32['no mobile'])[9])*100)/((tab32['no mobile'])[10])])
    line_chart.add('1 mobile', [(((tab32['1 mobile'])[0])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[1])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[2])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[3])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[4])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[5])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[6])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[7])*100)/((tab32['1 mobile'])[10]), \
                                             (((tab32['1 mobile'])[8])*100)/((tab32['1 mobile'])[10]), (((tab32['1 mobile'])[9])*100)/((tab32['1 mobile'])[10])])
    line_chart.add('2 mobile', [(((tab32['2 mobile'])[0])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[1])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[2])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[3])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[4])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[5])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[6])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[7])*100)/((tab32['2 mobile'])[10]), \
                                             (((tab32['2 mobile'])[8])*100)/((tab32['2 mobile'])[10]), (((tab32['2 mobile'])[9])*100)/((tab32['2 mobile'])[10])])
    line_chart.add('3 mobile', [(((tab32['3 mobile'])[0])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[1])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[2])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[3])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[4])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[5])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[6])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[7])*100)/((tab32['3 mobile'])[10]), \
                                             (((tab32['3 mobile'])[8])*100)/((tab32['3 mobile'])[10]), (((tab32['3 mobile'])[9])*100)/((tab32['3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')

def sp_age(number):
    tab32 = pd.read_csv('DATA/ALL_ALL.csv').to_dict()
    line_chart.x_labels = ('No feature phone', '1 Feature phone', '2 Feature phone', '3 Feature phone', 'No smart phone', '1 Smart phone', '2 Smart phone', '3 Smart phone')
    line_chart.add('Amount', [(((tab32['SP no mobile'])[number])*100)/((tab32['SP no mobile'])[10]), (((tab32['SP 1 mobile'])[number])*100)/((tab32['FP 1 mobile'])[10]), \
                              (((tab32['SP 2 mobile'])[number])*100)/((tab32['SP 2 mobile'])[10]), (((tab32['SP 3 mobile'])[number])*100)/((tab32['SP 3 mobile'])[10])])
    line_chart.render_to_file('Graph_main.svg')

main(input(), input())
