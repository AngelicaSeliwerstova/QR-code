
word=input()
cirillic=[chr(i) for i in range(ord('а'),ord('я')+1)]
def summary(letter):
    keys = ['1', '2', '4', '8', '16', '32']
    dicts = dict.fromkeys(keys, 0)
    posy=''
    for s in range(len(cirillic)):
        if cirillic[s]==letter:
            s+=1
            if s >= 32:
                s -= 32
                dicts['32'] += 1
                posy+='1'
            else:posy+='0'
            if s >= 16:
                s -= 16
                dicts['16'] += 1
                posy+='1'
            else:posy+='0'
            if s >= 8:
                s -= 8
                dicts['8'] += 1
                posy+='1'
            else:posy+='0'
            if s >= 4:
                s -= 4
                dicts['4'] += 1
                posy+='1'
            else:posy+='0'
            if s >= 2:
                s -= 2
                dicts['2'] += 1
                posy+='1'
            else:posy+='0'
            if s >= 1:
                s -= 1
                dicts['1']+=1
                posy+='1'
            else:posy+='0'
            break
    return (posy.zfill(6))[::-1]
def make_block(letter):
    bits=summary(letter)
    return [
        [int(bits[0]),int(bits[1])],
        [int(bits[2]),int(bits[3])],
        [int(bits[4]),int(bits[5])]
    ]
def empty_block():
    return [
        [0,0],
        [0,0],
        [0,0]
    ]
word=word[:6]
blocks=[]
for ch in word:
    if ch in cirillic:
        blocks.append(make_block(ch))
    else:
        blocks.append(empty_block())
while len(blocks)<6:
    blocks.append(empty_block())
data_matrix=[]
for inner_row in range(3):
    row=[]
    for block_index in range(3):
        row+=blocks[block_index][inner_row]
    data_matrix.append(row)
for inner_row in range(3):
    row=[]
    for block_index in range(3,6):
        row+=blocks[block_index][inner_row]
    data_matrix.append(row)
#итоговая матрица
for row in data_matrix:
    for val in row:
        print(val,end=' ')
    print()
anchor = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

matrix=[[0]*12 for _ in range(12)]
for i in range(5):
    for j in range(5):
        matrix[i][j]=anchor[i][j]
for i in range(6):
    for j in range(6):
        matrix[i+6][j+6]=data_matrix[i][j]
print()
for row in matrix:
    for val in row:
        print(val,end=' ')
    print()
from turtle import*
speed(0)
hideturtle()
tracer(0)
bgcolor('white')
size=40
start_x=-120
start_y=120
screensize(2000,2000)
def draw_square(x,y,size):
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    fillcolor('black')
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()
    penup()
def draw_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                x=start_x+j*size
                y=start_y-i*size
                draw_square(x,y,size)

fillcolor("black")
draw_matrix(matrix)

update()
done()
