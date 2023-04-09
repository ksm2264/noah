from ..agents.categorize_file import get_categories

class FileGrouping:
    def __init__(self, app_summary, all_files):
        
        self.app_summary = app_summary
        self.all_files = all_files
        
        self.store = {}

    def categories(self):
        
        return list(self.store.keys())

    def upsert_store(self, categories, file_name):

        for category in categories:
            if (category in self.categories()):
                self.store[category].append(file_name)
            else:
                self.store[category] = [file_name]

    def build_store(self):
    
        for idx, file in enumerate(self.all_files):
            
            print(f'Processing {file}: {idx} of {len(self.all_files)}')
            categories = get_categories(self.app_summary, self.categories(), file)
            
            self.upsert_store(categories, file)