import os



class gloable:
    variable_count = 0
    function_count = 0
    constant_count = 0
    total_LOC = 0
    rating = 0
    total_Memory = 0
    total_Calls = 0
    project_Calls = 0
    project_Memeory = 0
    file_Type = "none"
    int_var = []
    float_var = []
    double_var = []
    sturct_var = []
    short_var = []
    long_var = []
    char_var = []
    bool_var = []
    byte = []


    def putCount(self, type, value):
        if type == 'variable':
            self.variable_count = value
        elif type == 'function':
            self.function_count = value
        elif type == 'constant':
            self.constant_count = value

    def getCount(self, type):
        if type == 'variable':
            return self.variable_count
        elif type == 'function':
            return self.function_count
        elif type == 'constant':
            return self.constant_count

    def addVar(self, type, value):
        if type == '':
            return


class key_words:
    c_key_words = ["auto", "double", "int", "struct", "break", "else", "long", "switch", "case", "enum", "register", "typedef", "char", "extern", "return",
                   "union", "const", "float", "short", "unsigned", "continue", "for", "signed", "void", "default", "goto", "sizeof", "volatile", "do", "if", "static", "while"]
    java_key_words = ["abstract", "boolean", "break", "byte", "case", "catch", "char", "class", "continue", "default", "do", "double", "else", "extends", "false", "final", "finally", "float", "for", "if", "implements", "import", "instanceof",
                      "int", "interface", "long", "new", "null", "package", "private", "protected", "public", "return", "short", "static", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "try", "true", "void", "while"]
    cpp_key_words = ["Asm", "auto", "bool", "break", "case", "catch", "char", "class", "const_cast", "continue", "default", "delete", "do", "double", "else", "enum", "dynamic_cast", "extern", "false", "float", "for", "union", "unsigned", "using", "friend", "goto", "if", "inline", "int", "long", "mutable",
                     "virtual", "namespace", "new", "operator", "private", "protected", "public", "register", "void", "reinterpret_cast", "return", "short", "signed", "sizeof", "static", "static_cast", "volatile", "struct", "switch", "template", "this", "throw", "true", "try", "typedef", "typeid", "unsigned", "wchar_t", "while"]


class gloable_classes:
    gloable_obj = gloable()
    key_words_obj = key_words()


def setupGloable(module):
    module.class_gloable = gloable_classes()
    return module
