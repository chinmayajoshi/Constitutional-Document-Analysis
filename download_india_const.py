import os
from pathlib import Path, PurePosixPath

if __name__ == "__main__":
    try:
        to_be_downloaded = True
        indian_constition_download_link = 'https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2023/05/2023050195.pdf'
        dir_path = "./Indian Constitution/data"

        # check directory
        if Path(dir_path).is_dir() != True:
            os.system("mkdir data")
            print("Directory created")
        else: print("Directory already exists")

        # check file
        file_path = "./Indian Constitution/data/India.pdf"
        my_file = Path(file_path)

        if my_file.is_file():
            ext = PurePosixPath(my_file).suffix
            if ext == '.pdf':
                to_be_downloaded = False
                print("File Exists")
            else:
                print(f"File exists present with extention {ext}")
        else: 
            print("File does not exist")

        # download if required 
        if to_be_downloaded:
            os.system(f"curl -o {file_path} {indian_constition_download_link}")
            print(f"Downloaded the file at {my_file}")

    except Exception as e:
        print(f"Exception occurred: {e}")