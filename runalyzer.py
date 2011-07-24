from nltkAnalyzer import TextRequirementProcessor
from stopwords import STOPWORDS

def txt_analyzer(txt_file, number_of_cat):
    trp = TextRequirementProcessor(txt_file, number_of_cat)
    corpus_root, fileid = trp.split_path(txt_file)
    raw_text = trp.search_fileid(corpus_root, fileid)
    text_no_punct_list, stopwords_list = trp.list_raw_txt_file(raw_text, STOPWORDS)
    text_alpha_no_punct_stopword_list = trp.split_stopwords(text_no_punct_list, stopwords_list)
    lemmatized_list_by_verb_noun_adj_adv = trp.lemmatize_text_as_list(text_alpha_no_punct_stopword_list)
    categories_directory, boolean_for_directory_test, tmp_root, tmp_folderid = trp.create_temp_directory
    wordtype_categories = trp.list_wordtypes_from_lemmatized_list(lemmatized_list_by_verb_noun_adj_adv, number_of_cat)
    category_tmp_file_list, boolean_for_file_test = trp.create_temp_files_named_by_wordtypes(wordtype_categories, categories_directory)
    category_tmp_file_content, boolean_for_content_test = trp.assign_temp_files_content(wordtype_categories, lemmatized_list_by_verb_noun_adj_adv)
    category_tmp_file_list, boolean_for_check_content_file_test = trp.assign_temp_content_to_temp_files(category_tmp_file_content, category_tmp_file_list)
    reader, boolean_for_categories_test = trp.create_categorized_corpus(categories_directory)
    trp.tabulate_categorized_words(reader, number_of_cat)
    trp.plot_results(lemmatized_list_by_verb_noun_adj_adv, number_of_cat)
    boolean_for_file_test = trp.delete_temporary_files(category_tmp_file_list)
    boolean_for_directory_test = trp.remove_categories_directory(categories_directory, tmp_root, tmp_folderid)
    
    
