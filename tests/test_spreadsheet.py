import pytest
from src.spreadsheet import Spreadsheet

@pytest.fixture
def spreadsheet():
    '''returns spreadsheet instance'''
    return Spreadsheet()

def test_set_and_get_cell_value(spreadsheet):
    '''implement test case from example'''
    spreadsheet.set_cell_value('A1', '13')
    spreadsheet.set_cell_value('A2','14')
    spreadsheet.set_cell_value('A3', '=A1+A2')
    assert spreadsheet.get_cell_value('A3') == 27
    spreadsheet.set_cell_value('A4', '=A1+A2+A3')
    assert spreadsheet.get_cell_value('A4') == 54

def test_formula_reference_update(spreadsheet):
    '''ensure that changes in referenced cells are detected'''
    spreadsheet.set_cell_value('A1', 1)
    spreadsheet.set_cell_value('A2', '=A1')
    assert spreadsheet.get_cell_value('A2') == 1
    spreadsheet.set_cell_value('A1', 2)
    assert spreadsheet.get_cell_value('A2') == 2

def test_reference_cell_not_exists(spreadsheet):
    ''''''
    spreadsheet.set_cell_value('A1', '=A2+1')
    assert spreadsheet.get_cell_value('A1') == 1
    assert 'A2' in spreadsheet.data
    assert spreadsheet.get_cell_value('A2') == 0

def test_detect_cyclic_reference(spreadsheet):
    spreadsheet.set_cell_value('A1','A2')
    with pytest.raises(Exception) as e:
        spreadsheet.set_cell_value('A2','A1')
    assert e.type == RecursionError
