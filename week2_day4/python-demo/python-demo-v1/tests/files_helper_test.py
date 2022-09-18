from files_helper import is_valid_path, build_full_filename

def is_valid_path_return_false():
    result = is_valid_path(None)
    print(not result)
    assert result == False, 'expected False for path=None'

def is_valid_path_return_true():
    result = is_valid_path('')
    print(result)
    assert result == True, 'expected False for path=None'

def is_valid_path_non_empty_path_returns_true():
    path = "output"
    result = is_valid_path(path)
    print(result)
    assert result == True, 'expected False for path=None'

def build_full_filename_empty_path():
    path = ""
    filename = "x.txt"
    full_filename = build_full_filename(path, filename)
    
    #expected 'x.txt'
    assert full_filename is not None and not ( '/' in full_filename), 'expected full_filename = {filename}'

def main():
    is_valid_path_return_false()
    is_valid_path_return_true()
    is_valid_path_non_empty_path_returns_true()
    build_full_filename_empty_path()

main()    