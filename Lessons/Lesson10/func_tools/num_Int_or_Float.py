def num_Int_or_Float(num):
    if '.' in num:
        try:
            return float(num)
        except ValueError:
            return False
    else:
        try:
            return int(num)
        except ValueError:
            return False