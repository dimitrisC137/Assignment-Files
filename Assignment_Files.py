import os
import shutil

CACHE = "cache"
FILE = "files"
PATH = os.path.join(os.getcwd(), FILE, CACHE)

def clean_cache():
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    elif os.path.exists(PATH):
        shutil.rmtree(PATH)
        os.makedirs(PATH)


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    shutil.unpack_archive(zip_file_path, cache_dir_path)


def cached_files():
    list_caches_files = os.listdir(PATH)
    new_abs_list_caches_files = []
    for item in list_caches_files:
        new_abs_list_caches_files += [os.path.join(PATH, item)]
    return new_abs_list_caches_files


def password_location(new_abs_list_caches_files): 
    location = False
    for file in new_abs_list_caches_files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    location = True
                    password = line.split()[1]
                    return password
                else:
                    location = False


if __name__ == "__main__":  
    clean_cache()
    cache_zip('c:/Users/Dimitris/Documents/Winc/files/data.zip', 'c:/Users/winke/Documents/Winc/files/cache')
    new_abs_list_caches_files = (cached_files())
    password_location(new_abs_list_caches_files)