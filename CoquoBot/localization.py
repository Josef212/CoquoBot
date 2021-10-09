import abc
import localizations as locs

class Dictionary(metaclass=abc.ABCMeta):
    def __init__(self, loc: dict):
        self.__localizations = loc

    def get_localization(self, key: str) -> str:
        if key not in self.__localizations:
            return key
        
        return self.__localizations[key]
    
    def get_localization_format(self, key: str, *args) -> str:
        if key not in self.__localizations:
            return f'{key}'
        
        return self.__localizations[key].format(*args)
    
    def has_key(self, key: str) -> bool:
        return key in self.__localizations

class Localization:
    def __init__(self):
        english = Dictionary(locs.EN)
        self.__tear_down = english
        self.__dictionaries = {
            'cat': Dictionary(locs.CAT),
            # TODO: Add back es
            #'es': Dictionary(locs.ES),
            'en': english,
            'en-US': english,
            'en-GB': english,
        }

    def get_text(self, lang: str, key: str) -> str:
        lang_dic = self.__get_dictionary(lang)
        if lang_dic.has_key(key):
            return lang_dic.get_localization(key)
        
        return self.__tear_down.get_localization(key)

    def get_text_format(self, lang: str, key: str, *args) -> str:
        lang_dic = self.__get_dictionary(lang)
        if lang_dic.has_key(key):
            return lang_dic.get_localization_format(key, *args)
        
        return self.__tear_down.get_localization_format(key, *args)
    
    def __get_dictionary(self, lang: str) -> Dictionary:
        if lang not in self.__dictionaries:
            return self.__tear_down
        
        return self.__dictionaries[lang]

