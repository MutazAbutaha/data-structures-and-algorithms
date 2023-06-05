import pytest 
from stack_queue_brackets import is_balanced

def test_is_balanced():
    output = is_balanced("(qqqqqq){sssss}[qqqqq]")
    
    assert output ==  True



def test_is_balanced2():
    output = is_balanced("({)}")
    
    assert output ==  False


def test_is_balanced3():
    output = is_balanced("[{aaaaaaaa}[(Ssssss)]")
   
    assert output ==  False

def test_is_balanced4():
    output = is_balanced("[{aaaaaaaa}(Ssssss){}]")
   
    assert output ==  True



