# -*- coding: utf-8 -*-


class Variables(object):

    def __init__(self):
        self.path = '/home/eduardo/Área de trabalho/nietzscheHumanAllTooHuman.txt'
        self.n_cat = 10
        self.root = '/home/eduardo/Área de trabalho'
        self.fileid = 'nietzscheHumanAllTooHuman.txt'
        self.corpus_root = '/media/KINGSTON/IC/Nltk/Projeto/fase6/PlaintextTest'
        self.spec_fileid = 'fileid1.txt'
        self.concise_raw_text = 'plain! a -text- b\ntesting test safely 1 c biggest big big women\n'
        self.concise_stopwords = ' a\n \n b\n\n c\n'
        self.concise_text_list = ['plain', 'a', 'text', 'b', 'testing', 'test', 'safely', '1', 'c', 'biggest', 'big', 'big', 'women']
        self.concise_stopwords_list = ['a', 'b', 'c']
        self.text_list_free_from_stopwords = ['plain', 'text', 'testing', 'test', 'safely', 'biggest', 'big', 'big', 'women']
        self.lemmatized_list = ['plain', 'text', 'test', 'test', 'safely', 'big', 'big', 'big', 'woman']
        self.wordtypes_list = ['big', 'test', 'plain', 'safely', 'text', 'woman']   
        self.temporary_directory = '/tmp'
        self.categories_content = [['big', 'big', 'big'],  ['test', 'test'],  ['plain'],  ['safely'],  ['text'],  ['woman']]
