from bot.agents.categorize_file import get_categories
import logging
import sys

handler = logging.StreamHandler(sys.stderr)
logging.basicConfig(level=logging.INFO, handlers=[handler])

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
            
            logging.info(f'Processing {file}: {idx} of {len(self.all_files)}')
            categories = get_categories(self.app_summary, self.categories(), file)
            
            self.upsert_store(categories, file)