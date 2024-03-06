#!/usr/bin/env python3

#my string
# count_sentences.py




class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        if self.value and self.value[-1] == '.':
            return True
        else:
            return False

    def is_question(self):
        if self.value and self.value[-1] == '?':
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value and self.value[-1] == '!':
            return True
        else:
            return False

    def count_sentences(self):
        if self.value:
            sentences = (self.value).split('.')
            return len(sentences)

       