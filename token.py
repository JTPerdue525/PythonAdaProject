#token.py

class Token:

    
    def __init__(self, value, id, keyword):
        self.value = value
        self.ID = id
        self.keyword = keyword

    def setvalue(self, v):
        value = v

    def returnvalue(self):
        return self.value

    def setid(self, id):
        self.ID = id

    def returnid(self):
        return self.ID

    def setkeyword(self, kw):
        self.keyword = kw

    def returnkeyword(self):
        return self.keyword

    def toString(self):
        return "Value: "+ str(self.value)+ "\nTypeID: "+ str(self.ID)+ "\nKeyword: "+ str(self.keyword)
    
    

BEGIN_KEYWORD = Token("begin",100,"begin_keyword")
END_KEYWORD =  Token("end",101,"end_keyword")
WHILE_KEYWORD = Token("while",102,"while_keyword")
IF_KEYWORD = Token("if",103,"if_keyword")
ELSE_KEYWORD = Token("else",104,"else_keyword")
ELSEIF_KEYWORD = Token("elseif",105,"elseif_keyword")
FOR_KEYWORD = Token("for",106,"for_keyword")
RETURN_KEYWORD = Token("return",107,"return_keyword")
BREAK_KEYWORD = Token("break",108,"break_keyword")
CONTINUE_KEYWORD = Token("continue",109,"continue_keyword")
FUNCTION_KEYWORD = Token("function",110,"function_keyword")
ASSIGNMENT_OPERATOR = Token("=",300,"assignment_operator")
LE_OPERATOR = Token("<=",301,"le_operator")
LT_OPERATOR = Token("<",302,"lt_operator")
GE_OPERATOR = Token(">=",303,"ge_operator")
GT_OPERATOR = Token(">",304,"gt_operator")
EQ_OPERATOR = Token("==",305,"eq_operator")
NE_OPERATOR = Token("!=",306, "ne_operator")
ADD_OPERATOR = Token("+",307,"add_operator")
SUB_OPERATOR = Token("-",308,"sub_operator")
MUL_OPERATOR = Token("*",309,"mul_operator")
DIV_OPERATOR = Token("/",310,"div_operator")
MOD_OPERATOR = Token("%",311,"mod_operator")
REV_DIV_OPERATOR = Token("\\",312,"rev_div_operator")
EXP_OPERATOR = Token("^",313,"exp_operator")
EACH_OPERATOR = Token(":",314,"each_operator")
LEFT_PARENTHESIS = Token("(",315,"left_parenthesis")
RIGHT_PARENTHESIS = Token(")",316,"right_parenthesis")
    
IDENTIFIER = Token("",200,"identifier")
INT_LITERAL = Token("",201,"int_literal")
FLOAT_LITERAL = Token("",202,"float_literal")
PRINT_FUNCTION = Token("print",500,"print_function")


test = BEGIN_KEYWORD.toString()
print(test)
