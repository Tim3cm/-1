from main_Nikita_ivanchenko import *

def test1():
    data = ['0,1,0,40,30,male,80,80,80,10,10',  '0,1,0,0,0,male,80,80,80,10,10', '0,1,0,0,0,0,80,80,80,10.10','0,1,0,0,0,0,80,80,80,10,10', '0,1,0,0,0,0,80,80,80,10,10' ]
    assert result(data) == [10.0, 10.0]

def test2():
    data = ['0,1,0,40,30,male,80,80,80,10,10,',  '0,1,0,0,0,male,80,80,80,10,10,', '0,1,0,0,0,male,80,80,80,10,10', '0,1,0,0,0,male,80,80,80,10,10', '0,1,0,0,0,male,80,80,80,10,10']
    assert result(data) == [10.0, 10.0, 10.0, 10.0, 10.0]