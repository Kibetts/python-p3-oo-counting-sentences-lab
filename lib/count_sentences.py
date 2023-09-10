#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = self.value.split('.')
        return len(sentences)

