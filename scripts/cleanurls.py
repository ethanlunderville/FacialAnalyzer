import os

file1 = []

with open(f'{os.environ["FACEPROJECTDIR"]}/output/urls/urls', "r") as file1:
  with open(f'{os.environ["FACEPROJECTDIR"]}/output/urls/done', "r") as file2:
    file1 = file1.readlines()
    file2 = file2.readlines()
    for line in file2:
      if line in file1:
        file1.remove(line)

with open(f'{os.environ["FACEPROJECTDIR"]}/output/urls/urls', "w") as wfile1:
    wfile1.writelines(file1)