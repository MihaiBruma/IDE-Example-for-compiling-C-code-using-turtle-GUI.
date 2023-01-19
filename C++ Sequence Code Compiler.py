from turtle import bgcolor, circle, \
    goto, write, fillcolor, pensize, \
    pencolor, pendown, penup, \
    begin_fill, end_fill, onclick, \
    done, shape, shapesize,textinput,bye,clear,speed

bgcolor("royal blue")
shape("triangle")
shapesize(1.5)

def Rerun():
    shape("arrow")
    penup()
    goto(750, -390)
    pencolor("dark green")
    pensize(5)
    pendown()
    circle(15)
    penup()


def CompileResult(x, y):
    goto(-460, 400)
    pencolor("dark green")
    pendown()
    write("~ done", font=("Times New Roman", 20, "bold"))
    penup()
    penup()
    pencolor("white")
    fillcolor("black")
    goto(-500, -300)
    pendown()
    speed(3)
    begin_fill()
    goto(500, -300)
    goto(500, -470)
    goto(-500, -470)
    goto(-500, -300)
    end_fill()
    penup()
    goto(-470, -450)
    pencolor("white")
    write("Product is = 19\n" \
          "Product1 is = 54\n" \
          "MAX is = 7\n" \
          "MAX is = 10\n" \
          "Absolute value is = 10\n"
          "\n"
          "...Program finished with exit code 0",
          font=("Consolas", 11, "bold"))
    goto(600, -395)
    pencolor("dark red")
    write(">>> Rerun", font=("Times new roman", 20, "bold"))
    Rerun()

password = textinput("User - Name Password","Enter your User - Name passwod")
if password == '12345':
    txt = textinput("Start - Stop", "Ready to start ?\t Type: Yes / No ")
    if txt == 'yes' or txt == 'Yes' or txt == 'YES':
        penup()
        goto(-700, 430)
        pendown()
        pencolor("white")
        write("WELCOME USER !", font=("segoe script", 35, "bold", "italic"), align="center")
        penup()
        goto(0, 400)
        pendown()
        write("#---This is a DEMO for C++ code sequence---#", font=("Times New Roman", 25, "bold"), align="center")
        penup()
        goto(-500, 370)
        fillcolor("blue")
        pencolor("white")
        pendown()
        begin_fill()
        goto(500, 370)
        goto(500, -270)
        goto(-500, -270)
        goto(-500, 370)
        end_fill()
        penup()
        goto(0, -250)
        pencolor("white")
        pendown()
        write("/*\n" \
              "Preprocessor\n"
              "MACRO - no calculations\n" \
              "*/\n" \
              "#include <cstdio>\n" \
              "#include <cstdlib>\n" \
              "#include <stdint-gcc.h>\n" \
              "#define X 14\n"
              "#define Multiply(a,b) a*b // MACRO - Substitution text\n" \
              "#define Multiply1(x,y) (x)*(y)\n" \
              "#define MAX(a,b) a>b ? a:b\n" \
              "#define ABS_Value(val) ((val<0) ? (-val):(val))\n" \
              "\n" \
              "int main(void){\n" \
              "\n" \
              "int8_t iParam1 = 4 , iParam2 = 6 , val =-10;\n" \
              "printf(''Product is = %d\\n'',Multiply(iParam1+2 , iParam2+3)); //4+2*3+6 = 19\n"
              "printf(''Product1 is = %d\\n'',Multiply1(iParam1+2 , iParam2+3)); // 6*9 = 54\n" \
              "printf(''MAX is = %d\\n'',MAX(iParam1++ , iParam2++));\n" \
              "printf(''MAX is = %d\\n'',MAX(++iParam1 , ++iParam2));\n" \
              "printf(''Absolute value is = %d\\n'',ABS_Value(val));\n" \
              "\n" \
              "return 0;\n" \
              "}\n",
              font=("Consolas", 15), align="center")
        penup()
        goto(-700, 400)
        pencolor("dark red")
        pendown()
        write(">>> Click on cursor to compile ", font=("Times New Roman", 20, "bold"), align="center")
        penup()
        goto(-500, 430)
        fillcolor("dark green")
        pencolor("white")
        pendown()
        begin_fill()
        goto(-470, 415)
        goto(-500, 400)
        goto(-500, 430)
        end_fill()
        goto(-470, 415)
        penup()
        onclick(CompileResult)
        done()
    elif txt == 'no' or txt == 'No' or txt == 'NO':
        shapesize(1)
        pencolor("white")
        goto(0, 0)
        write(">>> Have a Nice Day ", font=("Times New Roman", 20, "bold"), align="center")
        done()
        clear()
        bye()
elif password != '12345':
    shapesize(1)
    pencolor("white")
    goto(0, 0)
    write(">>> Wrong password, Have a Nice Day ", font=("Times New Roman", 20, "bold"), align="center")
    done()
else :
    done()
    bye()