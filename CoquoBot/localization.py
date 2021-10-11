import localizations as locs

class Dictionary():
    def __init__(self, loc: dict):
        self.__localizations = loc

    def get_localization(self, key: str) -> str:
        if key not in self.__localizations:
            return key
        
        ret = self.__localizations[key]
        if len(ret) == 0:
            return '!Text not found!'
        
        return ret
    
    def get_localization_format(self, key: str, *args) -> str:
        if key not in self.__localizations:
            return f'{key}'
        
        ret = self.__localizations[key].format(*args)
        if len(ret) == 0:
            return f'-{key}-'
        
        return ret
    
    def has_key(self, key: str) -> bool:
        return key in self.__localizations

class Localization:
    def __init__(self):
        english = Dictionary(locs.EN)
        self.__teardown = english
        self.__dictionaries = {
            'cat': Dictionary(locs.CAT),
            'es': Dictionary(locs.ES),
            'en': english,
            'en-US': english,
            'en-GB': english,
        }

    def get_text(self, lang: str, key: str) -> str:
        lang_dic = self.__get_dictionary(lang)
        if lang_dic.has_key(key):
            return lang_dic.get_localization(key)
        
        return self.__teardown.get_localization(key)

    def get_text_format(self, lang: str, key: str, *args) -> str:
        lang_dic = self.__get_dictionary(lang)
        if lang_dic.has_key(key):
            return lang_dic.get_localization_format(key, *args)
        
        return self.__teardown.get_localization_format(key, *args)
    
    def __get_dictionary(self, lang: str) -> Dictionary:
        if lang not in self.__dictionaries:
            return self.__teardown
        
        return self.__dictionaries[lang]

