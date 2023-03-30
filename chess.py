class Field:
    def __init__(self):
        self.field = {}
        for a in 'ABCDEFGHIKL':
            for i in range(1, 12):
                self.field[(a, i)] = '.'
        for a in 'ABCDEFGHIKL':
            self.field[(a, 7)] = 'P'

        self.field[('F', 5)] = 'p'
        self.field[('E', 4)] = 'p'
        self.field[('G', 4)] = 'p'
        self.field[('D', 3)] = 'p'
        self.field[('H', 3)] = 'p'
        self.field[('C', 2)] = 'p'
        self.field[('I', 2)] = 'p'
        self.field[('B', 1)] = 'p'
        self.field[('K', 1)] = 'p'

        self.field[('C', 1)], self.field[('I', 1)] = 'r', 'r'
        self.field[('C', 8)], self.field[('I', 8)] = 'R', 'R'

        self.field[('F', 1)], self.field[('F', 2)], self.field[('F', 3)] = 'b', 'b', 'b'
        self.field[('F', 11)], self.field[('F', 10)], self.field[('F', 9)] = 'B', 'B', 'B'

        self.field[('D', 1)], self.field[('H', 1)] = 'n', 'n'
        self.field[('D', 9)], self.field[('H', 9)] = 'N', 'N'

        self.field[('E', 1)], self.field[('G', 1)] = 'q', 'k'
        self.field[('E', 10)], self.field[('G', 10)] = 'Q', 'K'

    def print_field(self):
        print(f"         11   11    ")
        print(f"       10   {self.field[('F', 11)]}   10")
        print(f"      9   {self.field[('E', 10)]}   {self.field[('G', 10)]}   9")
        print(f"    8   {self.field[('D', 9)]}   {self.field[('F', 10)]}   {self.field[('H', 9)]}   8")
        print(
            f"  7   {self.field[('C', 8)]}   {self.field[('E', 9)]}   {self.field[('G', 9)]}   {self.field[('I', 8)]}   7")
        for i in range(7, 1, -1):
            print(
                f"{i - 1}   {self.field[('B', i)]}   {self.field[('D', i + 1)]}   {self.field[('F', i + 2)]}   {self.field[('H', i + 1)]}   {self.field[('K', i)]}   {i - 1}")
            print(
                f"  {self.field[('A', i - 1)]}   {self.field[('C', i)]}   {self.field[('E', i + 1)]}   {self.field[('G', i + 1)]}   {self.field[('I', i)]}   {self.field[('L', i - 1)]}")

        print(
            f"  a {self.field[('B', 1)]}   {self.field[('D', 2)]}   {self.field[('F', 3)]}   {self.field[('H', 2)]}   {self.field[('K', 1)]} l")
        print(
            f"    b {self.field[('C', 1)]}   {self.field[('E', 2)]}   {self.field[('G', 2)]}   {self.field[('I', 1)]} k")
        print(f"      c {self.field[('D', 1)]}   {self.field[('F', 2)]}   {self.field[('H', 1)]} i")
        print(f"        d {self.field[('E', 1)]}   {self.field[('G', 1)]} h")
        print(f"          e {self.field[('F', 1)]} g")
        print(f"            f")

    @classmethod
    def print_field_copy(self, field):
        print(f"         11   11    ")
        print(f"       10   {field[('F', 11)]}   10")
        print(f"      9   {field[('E', 10)]}   {field[('G', 10)]}   9")
        print(f"    8   {field[('D', 9)]}   {field[('F', 10)]}   {field[('H', 9)]}   8")
        print(
            f"  7   {field[('C', 8)]}   {field[('E', 9)]}   {field[('G', 9)]}   {field[('I', 8)]}   7")
        for i in range(7, 1, -1):
            print(
                f"{i - 1}   {field[('B', i)]}   {field[('D', i + 1)]}   {field[('F', i + 2)]}   {field[('H', i + 1)]}   {field[('K', i)]}   {i - 1}")
            print(
                f"  {field[('A', i - 1)]}   {field[('C', i)]}   {field[('E', i + 1)]}   {field[('G', i + 1)]}   {field[('I', i)]}   {field[('L', i - 1)]}")

        print(
            f"  a {field[('B', 1)]}   {field[('D', 2)]}   {field[('F', 3)]}   {field[('H', 2)]}   {field[('K', 1)]} l")
        print(
            f"    b {field[('C', 1)]}   {field[('E', 2)]}   {field[('G', 2)]}   {field[('I', 1)]} k")
        print(f"      c {field[('D', 1)]}   {field[('F', 2)]}   {field[('H', 1)]} i")
        print(f"        d {field[('E', 1)]}   {field[('G', 1)]} h")
        print(f"          e {field[('F', 1)]} g")
        print(f"            f")


class Figure:
    symbols = ''

    def get_symbols(self):
        return self.symbols


class PawnWhite(Figure):

    def __init__(self):
        self.symbols = 'p'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if field[(i, j + 1)] == '.':
            arr_ret.add((i, j + 1))
        alf = 'ABCDEFGHIKL'
        # (alf[alf.index(a_ind) + 1], i_ind + 3)
        if 'F' > i > 'A' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j))
        if 'F' > i and field[(alf[alf.index(i) + 1], j + 1)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j + 1))

        if i == 'F' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j))

        if 'F' == i and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j))

        if 'F' < i < 'L' and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j))
        if i > 'F' and field[(alf[alf.index(i) - 1], j + 1)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j + 1))
        return list(arr_ret)


class PawnBlack(Figure):

    def __init__(self):
        self.symbols = 'P'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if field[(i, j - 1)] == '.':
            arr_ret.add((i, j - 1))
        alf = 'ABCDEFGHIKL'
        # (alf[alf.index(a_ind) + 1], i_ind + 3)
        if 'F' > i > 'A' and field[(alf[alf.index(i) - 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j - 1))
        if 'F' > i and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j))

        if i == 'F' and field[(alf[alf.index(i) - 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j - 1))

        if 'F' == i and field[(alf[alf.index(i) + 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j - 1))

        if 'F' < i < 'L' and field[(alf[alf.index(i) + 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j - 1))
        if i > 'F' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j))
        return list(arr_ret)


class RookWhite(Figure):

    def __init__(self):
        self.symbols = 'r'

    def get_all_movies(self, a_ind, i_ind, field):
        arr_ret = set()
        answ = set()
        for i in range(i_ind + 1, 12):
            if field[(a_ind, i)] == '.':

                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'):
                    answ.add((a_ind, i))
                break

        for i in range(i_ind - 1, 0, -1):
            if field[(a_ind, i)] == '.':
                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'):
                    answ.add((a_ind, i))
                break

        if a_ind == 'F':
            new_i = i_ind
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind - 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        ###################################################################
        elif a_ind > 'F':
            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F')::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1::]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

        elif a_ind < 'F':
            new_i = i_ind
            if a_ind > 'A':
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                        elif field[(a, new_i)] in list('PRHEQK'):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            break
                    except:
                        pass
            if a_ind > 'A':
                new_i = i_ind - 1
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                            new_i -= 1
                        elif field[(a, new_i)] in list('PRHEQK'):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            break
                    except:
                        pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        return list(answ)


class RookBlack(Figure):

    def __init__(self):
        self.symbols = 'R'

    def get_all_movies(self, a_ind, i_ind, field):
        arr_ret = set()
        answ = set()
        for i in range(i_ind + 1, 12):
            if field[(a_ind, i)] == '.':

                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'.lower()):
                    answ.add((a_ind, i))
                break

        for i in range(i_ind - 1, 0, -1):
            if field[(a_ind, i)] == '.':
                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'.lower()):
                    answ.add((a_ind, i))
                break

        if a_ind == 'F':
            new_i = i_ind
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind - 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        ###################################################################
        elif a_ind > 'F':
            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F')::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1::]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

        elif a_ind < 'F':
            new_i = i_ind
            if a_ind > 'A':
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'):
                            break
                    except:
                        pass
            if a_ind > 'A':
                new_i = i_ind - 1
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                            new_i -= 1
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'):
                            break
                    except:
                        pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        return list(answ)


class BishopWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()

        arr_ret = set()

        if a_ind == 'A':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('L', 0 + i_ind))
        elif a_ind == 'B':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('K', i_ind))
        elif a_ind == 'C':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('I', i_ind))
        elif a_ind == 'D':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('H', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('H', i_ind))
                arr_ret.add(('K', i_ind - 1))
        elif a_ind == 'E':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('G', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'F':
            if i_ind in [2, 10]:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
            else:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
                arr_ret.add(('B', i_ind - 2))
                arr_ret.add(('K', i_ind - 2))

        elif a_ind == 'G':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('E', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'H':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('D', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('D', i_ind))
                arr_ret.add(('K', i_ind - 1))

        elif a_ind == 'I':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('C', i_ind))

        elif a_ind == 'L':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('A', i_ind))

        elif a_ind == 'K':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('B', i_ind))

        last = 0
        for alf in 'ABCDEFGHIKL'[::2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'.lower()):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        last = 0
        for alf in 'ABCDEFGHIKL'[::-2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'.lower()):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        # diagonals
        #####################################################################
        if a_ind == 'F':
            new_i = i_ind + 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind + 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        #######################################################
        elif a_ind > 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        #########################################################################
        elif a_ind < 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

        return list(answ)


class BishopBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()

        arr_ret = set()

        if a_ind == 'A':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('L', 0 + i_ind))
        elif a_ind == 'B':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('K', i_ind))
        elif a_ind == 'C':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('I', i_ind))
        elif a_ind == 'D':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('H', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('H', i_ind))
                arr_ret.add(('K', i_ind - 1))
        elif a_ind == 'E':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('G', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'F':
            if i_ind in [2, 10]:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
            else:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
                arr_ret.add(('B', i_ind - 2))
                arr_ret.add(('K', i_ind - 2))

        elif a_ind == 'G':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('E', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'H':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('D', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('D', i_ind))
                arr_ret.add(('K', i_ind - 1))

        elif a_ind == 'I':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('C', i_ind))

        elif a_ind == 'L':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('A', i_ind))

        elif a_ind == 'K':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('B', i_ind))

        last = 0
        for alf in 'ABCDEFGHIKL'[2::2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'.lower()):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        last = 0
        for alf in 'ABCDEFGHIKL'[- 2::-2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'.lower()):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        # diagonals
        #####################################################################
        if a_ind == 'F':
            new_i = i_ind + 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind + 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        #######################################################
        elif a_ind > 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        #########################################################################
        elif a_ind < 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

        return list(answ)


class KingWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        answ.add((a_ind, i_ind + 1))
        answ.add((a_ind, i_ind - 1))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))
        elif a_ind > 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))

        elif a_ind < 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in list('PRNBQK'.lower()):
                arr_ret.append(pos)

        return arr_ret


class KingBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        answ.add((a_ind, i_ind + 1))
        answ.add((a_ind, i_ind - 1))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))
        elif a_ind > 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))

        elif a_ind < 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))

        arr_ret = []
        for pos in answ:
            try:
                if field[pos] not in list('PRNBQK'):
                    arr_ret.append(pos)
            except:
                pass

        return arr_ret


class KnightWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        if a_ind == 'A':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
        if a_ind == 'B':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))

        if a_ind == 'C':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))

        if a_ind == 'D':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'E':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'G':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))

        if a_ind == 'H':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'I':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'K':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'L':
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in 'PRNBQK'.lower():
                arr_ret.append(pos)

        return arr_ret


class KnightBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        if a_ind == 'A':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
        if a_ind == 'B':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))

        if a_ind == 'C':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))

        if a_ind == 'D':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'E':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'G':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))

        if a_ind == 'H':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'I':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'K':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'L':
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in 'PRNBQK':
                arr_ret.append(pos)

        return arr_ret


class QueenWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        arr1 = parce_pos(RookWhite().get_all_movies(a_ind, i_ind, field))
        arr2 = parce_pos(BishopWhite().get_all_movies(a_ind, i_ind, field))
        return arr1 + arr2


class QueenBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        arr1 = parce_pos(RookBlack().get_all_movies(a_ind, i_ind, field))
        arr2 = parce_pos(BishopBlack().get_all_movies(a_ind, i_ind, field))
        return arr1 + arr2


def parce_pos(arr):
    arr_ret = []
    for pos in arr:
        if check_pos_on_field(*pos):
            arr_ret.append(pos)

    return arr_ret


def check_pos_on_field(a_ind, i_ind):
    if a_ind == 'A':
        return 1 <= i_ind <= 6
    elif a_ind == 'B':
        return 1 <= i_ind <= 7
    elif a_ind == 'C':
        return 1 <= i_ind <= 8
    elif a_ind == 'D':
        return 1 <= i_ind <= 9
    elif a_ind == 'E':
        return 1 <= i_ind <= 10
    elif a_ind == 'F':
        return 1 <= i_ind <= 11
    elif a_ind == 'L':
        return 1 <= i_ind <= 6
    elif a_ind == 'K':
        return 1 <= i_ind <= 7
    elif a_ind == 'I':
        return 1 <= i_ind <= 8
    elif a_ind == 'H':
        return 1 <= i_ind <= 9
    elif a_ind == 'G':
        return 1 <= i_ind <= 10

def check_figure_attack_white(field: dict):
    figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                   'N': KnightBlack,
                   'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                   'q': QueenWhite}
    arr_ret = set()

    for pos, f in field.items():
        ind_i_from, ind_j_from = pos
        if field[pos] != '.':
            movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
            for move in movies:
                if field[move] in 'PRNBQK'.lower():
                    arr_ret.add(move)

    return arr_ret


def check_figure_attack_black(field: dict):
    figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                   'N': KnightBlack,
                   'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                   'q': QueenWhite}
    arr_ret = set()
    for pos, f in field.items():
        ind_i_from, ind_j_from = pos
        if field[pos] != '.':
            movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
            for move in movies:
                if field[move] in 'PRNBQK':
                    arr_ret.add(move)

    return arr_ret





def input_to_move(player, F):
    field = F.field
    while True:
        # ввели позицию фигуры
        if player == 'black':
            print('уязвимые позиции', check_figure_attack_black(field))
        else:
            print('уязвимые позиции', check_figure_attack_white(field))
        while True:
            try:
                inp = input('FROM: ').split()

                ind_i_from, ind_j_from = inp[0].upper(), int(inp[1])
                # hod = a, b
                if field[(ind_i_from, ind_j_from)] in list('prnbqk') and player == 'white':
                    break
                elif field[(ind_i_from, ind_j_from)] in list('prnbqk'.upper()) and player == 'black':
                    break
                else:
                    print('Это не ваша фигура')
            except:
                pass
        # вводим позицию хода
        figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                       'N': KnightBlack,
                       'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                       'q': QueenWhite}
        # check_mat(player, field, figure_dict)
        movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
        F1 = F.field.copy()
        for pos in movies:
            F1[pos] = '*'
        Field.print_field_copy(F1)
        print('Возможные ходы')
        print(*movies)

        try:
            inp = input('TO: ').split()

            ind_i_to, ind_j_to = inp[0].upper(), int(inp[1])

            # ind_i_to = abs(int(b) - 8)
            # ind_j_to = list('ABCDEFGH').index(a.upper())

            # print(movies)
            if (ind_i_to, ind_j_to) in movies:
                field[(ind_i_to, ind_j_to)] = field[(ind_i_from, ind_j_from)]
                field[(ind_i_from, ind_j_from)] = '.'
                break
            else:
                print('Такой ход невозможен')
        except:
            pass


def Chess():
    f = Field()
    player = 'white'
    while True:

        f.print_field()
        print(player, 'move')
        input_to_move(player, f)

        if 'k' not in f.field.values():
            f.print_field()
            print('BLACK WIN')
            break

        if 'K' not in f.field.values():
            f.print_field()
            print('WHITE WIN')
            break

        if player == 'white':
            player = 'black'
        else:
            player = 'white'


if __name__ == '__main__':
    Chess()
