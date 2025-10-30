from abc import ABC, abstractmethod


class ISearchable(ABC):
    
    
    @abstractmethod
    def search_by_criteria(self, criteria):
        pass
    
    @abstractmethod
    def search_by_name(self, name):
        pass
    
    @abstractmethod
    def get_all_sorted(self):
        pass