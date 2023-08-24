python_hash_table = {
    'for': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, '
           'or a string).\n'
           'This is less like the for keyword in other programming languages, and works more like an iterator method '
           'as found in other object-orientated programming languages.\n'
           'With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.',
    'for_statement_example': 'fruits = ["apple", "banana", "cherry"]\n'
                             'for x in fruits:\n'
                             'print(x)',
    'while': 'With the while loop we can execute a set of statements as long as a condition is true.',
    'while_example': 'i = 1\n'
                     'while i < 6:\n'
                     'print(i)\n'
                     'i += 1\n',
    'tuple': 'Tuples are used to store multiple items in a single variable.\n'
             'Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are '
             'List, Set, and Dictionary, all with different qualities and usage.\n '
             'A tuple is a collection which is ordered and unchangeable.\n'
             'Tuples are written with round brackets.',
    'def': 'A function is a block of code which only runs when it is called.\n'
           'You can pass data, known as parameters, into a function.\n'
           'A function can return data as a result.',
    'list': 'Lists are used to store multiple items in a single variable.\n'
            'Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are '
            'Tuple, Set, and Dictionary, all with different qualities and usage.\n '
            'Lists are created using square brackets',
    'array': 'Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.',
    'generator': 'None',
    'dictionary': 'Dictionaries are used to store data values in key:value pairs.\n'
                  'A dictionary is a collection which is ordered*, changeable and do not allow duplicates.\n'
                  'As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are '
                  'unordered.\n '
                  'Dictionaries are written with curly brackets, and have keys and values',
    'lambda': 'A lambda function is a small anonymous function.\n'
              'A lambda function can take any number of arguments, but can only have one expression.',
    'Numbers': 'There are three numeric types in Python:\n'
           '* int\n'
           '* float\n'
           '* complex\n'
           'Variables of numeric types are created when you assign a value to them:',
    'str': 'Strings in python are surrounded by either single quotation marks, or double quotation marks.'
           '"hello" is the same as "hello".\n'
           'You can display a string literal with the print() function:',
    'bool': 'In programming you often need to know if an expression is True or False.\n'
            'You can evaluate any expression in Python, and get one of two answers, True or False.\n'
            'When you compare two values, the expression is evaluated and Python returns the Boolean answer:',
    'class': 'Python is an object oriented programming language.\n'
             'Almost everything in Python is an object, with its properties and methods.\n'
             'A Class is like an object constructor, or a "blueprint" for creating objects.',
    'polymorphism': 'The word "polymorphism" means "many forms", and in programming it refers to '
                     'methods/functions/operators with the same name that can be executed on many objects or classes',
    'inheritance': 'Inheritance allows us to define a class that inherits all the methods and properties from another '
                   'class.\n '
                   'Parent class is the class being inherited from, also called base class.\n'
                   'Child class is the class that inherits from another class, also called derived class.'

}

java_hash_table = {
    'string': 'Strings are the type of objects that can store the character of values. A string acts the same as an '
              'array of characters in Java. '

}

cpp_hash_table = {

}
# print(python_hash_table.get('for'))
counter = 0
a = 'Python is an object oriented programming language.\n Almost everything in Python is an object, ' \
    'with its properties and methods.\n A Class is like an object constructor, or a "blueprint" for creating objects. '
for i in a:
    a.count(i)
    counter += 1
print(counter)
