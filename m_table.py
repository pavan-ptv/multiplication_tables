# multiplication table
LENGTH_OF_TABLE = []
MUL_TABLE = []


def m_table():
    number = int(input("specify the length of table:"))
    table_range = int(input(" enter the range of table:"))
    for i in range(0, number+1):
        LENGTH_OF_TABLE.append(i)
    print('length of table is :', LENGTH_OF_TABLE)
    for number in range(1, table_range+1):
        MUL_TABLE.append(number)
    print(MUL_TABLE)
    for j in MUL_TABLE:
        for k in LENGTH_OF_TABLE:
            yield f'{j} X {k} = {j * k}'


for m in m_table():
    print(m)
